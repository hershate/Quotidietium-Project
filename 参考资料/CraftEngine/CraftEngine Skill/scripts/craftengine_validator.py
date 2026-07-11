#!/usr/bin/env python3
"""
CraftEngine YAML 配置文件校验器
================================
基于 CraftEngine Wiki 内容构建，用于校验 CraftEngine 插件 YAML 配置文件。

校验范围:
  - 所有根键 (items, blocks, furniture, recipes, equipments, categories 等 15+ 种)
  - 深层字段类型、枚举值、必填项
  - 版本感知 (默认 1.21.2+)
  - 跨字段引用合法性

输出格式: JSON (错误列表) 和/或 纯文本
参考 Wiki: references/CraftEngine Wiki/

用法:
  python craftengine_validator.py <config.yml>
  python craftengine_validator.py <config.yml> --version 1.20.1
  python craftengine_validator.py <config.yml> --json     # 仅 JSON 输出
  python craftengine_validator.py <config.yml> --text     # 仅纯文本输出

错误码:
  0 - 校验通过 (无错误)
  1 - 校验完成 (有错误)
  2 - 参数错误
  3 - 文件读取失败
  4 - YAML 解析错误
"""

import yaml
import sys
import json
import os
import re
from typing import Any, Dict, List, Optional, Set, Tuple, Union

# =============================================================================
# 常量定义
# =============================================================================

VERSION = "1.1.0"
DEFAULT_MINECRAFT_VERSION = "1.21.2"

VALID_ROOT_KEYS = {
    "items", "blocks", "furniture", "recipes", "equipments",
    "categories", "loots", "vanilla_loots", "templates",
    "images", "sounds", "jukebox_songs", "paintings",
    "fonts", "lang", "i18n", "global_variables",
    "emojis", "emoji", "image",  # singular forms
    "config_factory", "item_updaters",
    "config_merges", "configured_feature", "translations",
    "namespace",  # 命名空间声明（如 namespace: my_mod）
    # 文本/数字/链式参数等参考模板中使用的特殊根键
    "custom",  # 自定义 MiniMessage 标签（文本格式模板）
    "functions", "broadcast_messages", "contextual_functions",  # 文本格式模板函数
    "providers",  # 数字格式提供者
    "translation",  # 翻译
    # 链式参数模板中的参数名根键
    "player", "block", "world", "entity", "server", "target",
    # 更新器模板（item 和 items 同时存在）
    "item",
}

# Fields from the template system that can appear in ANY configuration block
TEMPLATE_SYSTEM_FIELDS = {"template", "arguments", "overrides", "merges"}

VERSION_PREFIX = re.compile(r'^\$\$')
SECTION_IDENTIFIER = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*#[a-zA-Z0-9_]+$')
VERSION_CONDITION = re.compile(r'^\$\$[><]?=?\d+\.\d+(\.\d+)?(~[<>]?\d+\.\d+(\.\d+)?)?$|^\$\$fallback$')
SEPARATOR_DOUBLE_COLON = re.compile(r'::')

# Custom YAML loader that supports CraftEngine extended type tags
class CraftEngineLoader(yaml.FullLoader):
    """Custom YAML loader supporting CraftEngine extended type tags (!!long, !!float, !!byte, etc.)"""

CraftEngineLoader.add_constructor('tag:yaml.org,2002:long', lambda l, n: l.construct_scalar(n))
CraftEngineLoader.add_constructor('tag:yaml.org,2002:float', lambda l, n: float(l.construct_scalar(n)))
CraftEngineLoader.add_constructor('tag:yaml.org,2002:byte', lambda l, n: l.construct_scalar(n))
CraftEngineLoader.add_constructor('tag:yaml.org,2002:short', lambda l, n: l.construct_scalar(n))
CraftEngineLoader.add_constructor('tag:yaml.org,2002:null', lambda l, n: None)
CraftEngineLoader.add_constructor('tag:yaml.org,2002:ByteArray', lambda l, n: l.construct_scalar(n))
CraftEngineLoader.add_constructor('tag:yaml.org,2002:IntArray', lambda l, n: l.construct_scalar(n))
CraftEngineLoader.add_constructor('tag:yaml.org,2002:LongArray', lambda l, n: l.construct_scalar(n))
CraftEngineLoader.add_constructor('tag:yaml.org,2002:DoubleArray', lambda l, n: l.construct_scalar(n))
CraftEngineLoader.add_constructor('tag:yaml.org,2002:IntList', lambda l, n: l.construct_scalar(n))
CraftEngineLoader.add_constructor('tag:yaml.org,2002:LongList', lambda l, n: l.construct_scalar(n))
CraftEngineLoader.add_constructor('tag:yaml.org,2002:DoubleList', lambda l, n: l.construct_scalar(n))

# =============================================================================
# 错误类型定义
# =============================================================================

class ValidationError:
    """单个校验错误"""
    def __init__(self, path: str, error_type: str, message: str,
                 severity: str = "error", expected: str = None, actual: str = None):
        self.path = path
        self.error_type = error_type      # missing_field, wrong_type, invalid_enum, unknown_field, invalid_ref, etc.
        self.message = message
        self.severity = severity          # error, warning
        self.expected = expected
        self.actual = actual

    def to_dict(self) -> Dict:
        return {
            "path": self.path,
            "type": self.error_type,
            "message": self.message,
            "severity": self.severity,
            "expected": self.expected,
            "actual": self.actual,
        }

    def to_text(self) -> str:
        prefix = "[错误]" if self.severity == "error" else "[警告]"
        msg = f"{prefix} {self.path}: {self.message}"
        if self.expected:
            msg += f" (期望: {self.expected}"
            if self.actual:
                msg += f", 实际: {self.actual}"
            msg += ")"
        return msg


# =============================================================================
# Schema 定义 — 基于 CraftEngine Wiki
# =============================================================================

# --- 1. 物品 (items) Schema ---

ITEM_BEHAVIOR_TYPES = {
    "block_item", "ceiling_block_item", "wall_block_item", "ground_block_item",
    "double_high_block_item", "multi_high_block_item",
    "liquid_collision_block_item", "liquid_collision_furniture_item",
    "furniture_item", "compostable_item", "range_mining_item",
}

ITEM_BEHAVIOR_SCHEMA = {
    "block_item": {
        "required": ["type", "block"],
        "fields": {
            "type": {"type": "enum", "values": ["block_item"], "required": True},
            "block": {"type": "string_or_mapping", "required": True},
        }
    },
    "ceiling_block_item": {
        "required": ["type", "block"],
        "fields": {
            "type": {"type": "enum", "values": ["ceiling_block_item"], "required": True},
            "block": {"type": "string_or_mapping", "required": True},
        }
    },
    "wall_block_item": {
        "required": ["type", "block"],
        "fields": {
            "type": {"type": "enum", "values": ["wall_block_item"], "required": True},
            "block": {"type": "string_or_mapping", "required": True},
        }
    },
    "ground_block_item": {
        "required": ["type", "block"],
        "fields": {
            "type": {"type": "enum", "values": ["ground_block_item"], "required": True},
            "block": {"type": "string_or_mapping", "required": True},
        }
    },
    "double_high_block_item": {
        "required": ["type", "block"],
        "fields": {
            "type": {"type": "enum", "values": ["double_high_block_item"], "required": True},
            "block": {"type": "string_or_mapping", "required": True},
        }
    },
    "multi_high_block_item": {
        "required": ["type", "block"],
        "fields": {
            "type": {"type": "enum", "values": ["multi_high_block_item"], "required": True},
            "block": {"type": "string_or_mapping", "required": True},
        }
    },
    "liquid_collision_block_item": {
        "required": ["type", "block"],
        "fields": {
            "type": {"type": "enum", "values": ["liquid_collision_block_item"], "required": True},
            "block": {"type": "string_or_mapping", "required": True},
            "offset_y": {"type": "number", "required": False},
        }
    },
    "liquid_collision_furniture_item": {
        "required": ["type", "furniture"],
        "fields": {
            "type": {"type": "enum", "values": ["liquid_collision_furniture_item"], "required": True},
            "furniture": {"type": "string_or_mapping", "required": True},
            "rules": {"type": "mapping", "required": False},
            "ignore_placer": {"type": "boolean", "required": False},
            "ignore_entities": {"type": "boolean", "required": False},
        }
    },
    "furniture_item": {
        "required": ["type", "furniture"],
        "fields": {
            "type": {"type": "enum", "values": ["furniture_item"], "required": True},
            "furniture": {"type": "string_or_mapping", "required": True},
            "rules": {"type": "mapping", "required": False},
            "ignore_placer": {"type": "boolean", "required": False},
            "ignore_entities": {"type": "boolean", "required": False},
        }
    },
    "compostable_item": {
        "required": ["type"],
        "fields": {
            "type": {"type": "enum", "values": ["compostable_item"], "required": True},
        }
    },
    "range_mining_item": {
        "required": ["type"],
        "fields": {
            "type": {"type": "enum", "values": ["range_mining_item"], "required": True},
            "shape": {"type": "string", "required": False},
            "range": {"type": "list_of_string", "required": False},
            "check_durability": {"type": "boolean", "required": False},
        }
    },
}

ITEM_FURNITURE_RULES_ROTATION = ["any", "four", "eight", "sixteen", "north", "east", "west", "south"]
ITEM_FURNITURE_RULES_ALIGNMENT = ["any", "center", "half", "quarter", "corner"]

ITEM_FIELDS = {
    "material": {"type": "string", "required": False},
    "custom_model_data": {"type": "int", "required": False, "version": "any"},
    "item_model": {"type": "string", "required": False, "version": "1.21.2+"},
    "client_bound_material": {"type": "string", "required": False, "paid_only": True},
    "client_bound_model": {"type": "boolean", "required": False, "paid_only": True, "default": True},
    "texture": {"type": "string", "required": False},
    "textures": {"type": "list_of_string", "required": False},
    "models": {"type": "list", "required": False},
    "model": {"type": "string_or_mapping", "required": False},
    "legacy_model": {"type": "mapping", "required": False},
    "oversized_in_gui": {"type": "boolean", "required": False, "version": "1.21.6+", "default": True},
    "hand_animation_on_swap": {"type": "boolean", "required": False, "default": True},
    "swap_animation_scale": {"type": "number", "required": False, "version": "1.21.11+", "default": 1.0},
    "use_remainder": {"type": "string", "required": False, "version": "1.21.2+"},
    "category": {"type": "string_or_list", "required": False},
}

ITEM_DATA_FIELDS = {
    "item_name": {"type": "string", "required": False},
    "custom_name": {"type": "string", "required": False},
    "lore": {"type": "list", "required": False},
    "overwritable_lore": {"type": "list", "required": False, "paid_only": True},
    "insert_lore": {"type": "mapping_or_list", "required": False},
    "remove_lore": {"type": "string", "required": False},
    "overwritable_item_name": {"type": "string", "required": False, "paid_only": True},
    "unbreakable": {"type": "boolean", "required": False},
    "enchantment": {"type": "mapping", "required": False},
    "dyed_color": {"type": "string", "required": False},
    "custom_model_data": {"type": "int", "required": False},
    "hide_tooltip": {"type": "list_of_string", "required": False},
    "block_state": {"type": "string_or_mapping", "required": False},
    "attribute_modifiers": {"type": "list", "required": False},
    "food": {"type": "mapping", "required": False, "version": "1.20.5+"},
    "max_damage": {"type": "int", "required": False, "version": "1.20.5+"},
    "damage": {"type": "int", "required": False},
    "jukebox_playable": {"type": "string", "required": False, "version": "1.21+"},
    "item_model": {"type": "string", "required": False, "version": "1.21.2+"},
    "tooltip_style": {"type": "string", "required": False, "version": "1.21.2+"},
    "use_remainder": {"type": "string", "required": False, "version": "1.21.2+"},
    "trim": {"type": "mapping", "required": False},
    "equippable": {"type": "mapping", "required": False, "version": "1.21.2+"},
    "pdc": {"type": "mapping", "required": False},
    "profile": {"type": "string", "required": False},
    "painting_variant": {"type": "string", "required": False},
    "external": {"type": "mapping", "required": False},
    "nbt": {"type": "mapping", "required": False},
    "components": {"type": "mapping", "required": False, "version": "1.20.5+"},
    "remove_components": {"type": "list_of_string", "required": False, "version": "1.20.5+"},
}

ITEM_SETTINGS_FIELDS = {
    "fuel_time": {"type": "int", "required": False},
    "tags": {"type": "list_of_string", "required": False},
    "equipment": {"type": "mapping", "required": False},
    "repairable": {"type": "boolean_or_mapping", "required": False},
    "anvil_repair_item": {"type": "list", "required": False},
    "renameable": {"type": "boolean", "required": False, "default": True},
    "allowed_projectiles": {"type": "list_of_string", "required": False},
    "projectile": {"type": "mapping", "required": False},
    "dyeable": {"type": "boolean", "required": False},
    "food": {"type": "mapping", "required": False},
    "consume_replacement": {"type": "string", "required": False},
    "craft_remainder": {"type": "string_or_mapping", "required": False},
    "fuel_remainder": {"type": "string", "required": False},
    "invulnerable": {"type": "list_of_string", "required": False},
    "enchantable": {"type": "boolean", "required": False, "default": True},
    "compost_probability": {"type": "number", "required": False, "default": 0.5},
    "respect_repairable_component": {"type": "boolean", "required": False, "default": False},
    "dye_color": {"type": "string", "required": False},
    "firework_color": {"type": "string", "required": False},
    "ingredient_substitute": {"type": "list_of_string", "required": False},
    "hat_height": {"type": "number", "required": False},
    "keep_on_death_chance": {"type": "number", "required": False},
    "destroy_on_death_chance": {"type": "number", "required": False},
    "drop_display": {"type": "boolean_or_string", "required": False},
    "glow_color": {"type": "string", "required": False},
}

EQUIPMENT_SLOTS = ["head", "chest", "legs", "feet", "body", "saddle"]
INVULNERABLE_TYPES = ["lava", "fire", "fire_tick", "block_explosion", "entity_explosion", "lightning", "contact"]
DYE_COLORS = ["black", "dark_blue", "dark_green", "dark_aqua", "dark_red", "dark_purple", "gold", "gray", "dark_gray", "blue", "green", "aqua", "red", "light_purple", "yellow", "white"]

HIDE_TOOLTIP_OPTIONS = ["dyed_color", "enchantments", "attribute_modifiers", "unbreakable", "can_destroy", "can_place_on", "additional", "dyed", "trim", "food", "write", "stored_enchantments"]

# --- 2. 方块 (blocks) Schema ---

AUTO_STATE_GROUPS = [
    "solid", "note_block", "mushroom_stem", "red_mushroom_block", "brown_mushroom_block",
    "mushroom", "tintable_leaves", "waterlogged_tintable_leaves", "non_tintable_leaves",
    "waterlogged_non_tintable_leaves", "leaves", "waterlogged_leaves",
    "lower_tripwire", "higher_tripwire", "tripwire",
    "sapling", "pressure_plate", "cactus", "sugar_cane",
    "weeping_vine", "twisting_vine", "cave_vine", "kelp", "chorus",
]

PROPERTY_TYPES = {
    "boolean": {"values": ["true", "false"]},
    "int": {"type_param": "range"},
    "string": {"type_param": "values"},
    "direction": {"values": ["east", "south", "west", "north", "up", "down"]},
    "horizontal_direction": {"values": ["north", "south", "west", "east"]},
    "axis": {"values": ["x", "y", "z"]},
    "single_block_half": {"values": ["top", "bottom"]},
    "double_block_half": {"values": ["upper", "lower"]},
    "hinge": {"values": ["left", "right"]},
    "slab_type": {"values": ["top", "bottom", "double"]},
    "stairs_shape": {"values": ["straight", "inner_left", "inner_right", "outer_left", "outer_right"]},
    "sofa_shape": {"values": ["straight", "inner_left", "inner_right"]},
    "anchor_type": {"values": ["floor", "wall", "ceiling"]},
}

BLOCK_SETTINGS_FIELDS = {
    "hardness": {"type": "number", "required": False, "default": 2.0},
    "resistance": {"type": "number", "required": False, "default": 2.0},
    "push_reaction": {"type": "enum", "values": ["NORMAL", "DESTROY", "BLOCK", "IGNORE", "PUSH_ONLY"], "required": False, "default": "NORMAL"},
    "map_color": {"type": "int", "required": False, "default": 0},
    "burnable": {"type": "boolean", "required": False, "default": False},
    "fire_spread_chance": {"type": "int", "required": False, "default": 0},
    "burn_chance": {"type": "int", "required": False, "default": 0},
    "item": {"type": "string", "required": False},
    "replaceable": {"type": "boolean", "required": False, "default": False},
    "is_redstone_conductor": {"type": "boolean", "required": False},
    "is_suffocating": {"type": "boolean", "required": False},
    "is_view_blocking": {"type": "boolean", "required": False},
    "sounds": {"type": "mapping", "required": False},
    "require_correct_tools": {"type": "boolean", "required": False, "default": False},
    "respect_tool_component": {"type": "boolean", "required": False, "default": False},
    "correct_tools": {"type": "list_of_string", "required": False},
    "incorrect_tool_dig_speed": {"type": "number", "required": False, "default": 0.3},
    "tags": {"type": "list_of_string", "required": False},
    "client_bound_tags": {"type": "list_of_string", "required": False},
    "instrument": {"type": "string", "required": False, "default": "harp"},
    "fluid_state": {"type": "enum", "values": ["empty", "water"], "required": False, "default": "empty"},
    "support_shape": {"type": "string", "required": False},
    "bounce_restitution": {"type": "number", "required": False, "default": 0.0, "version": "1.21.2+"},
    "friction": {"type": "number", "required": False, "default": 0.6},
    "jump_factor": {"type": "number", "required": False, "default": 1.0},
    "speed_factor": {"type": "number", "required": False, "default": 1.0},
    "luminance": {"type": "int", "required": False, "default": 0},
    "can_occlude": {"type": "boolean", "required": False},
    "block_light": {"type": "int", "required": False},
    "propagate_skylight": {"type": "boolean", "required": False},
}

BLOCK_BEHAVIOR_TYPES = {
    "crop_block", "stem_block", "attached_stem_block", "bush_block", "sapling_block",
    "vertical_crop_block", "falling_block", "concrete_powder_block", "bouncing_block",
    "strippable_block", "sturdy_base_block", "budding_block", "snowy_block",
    "drop_experience_block", "drop_exp_block",  # drop_exp_block 是丢经验方块的简写别名
    "display_item_block", "item_frame_block",
    "simple_particle_block", "wall_torch_particle_block", "tint_source_block",
    "directional_attached_block", "face_attached_horizontal_directional_block",
    "hangable_block", "hanging_block", "liquid_flowable_block", "near_liquid_block",
    "on_liquid_block", "door_block", "trapdoor_block", "fence_block", "fence_gate_block",
    "button_block", "pressure_plate_block", "stairs_block", "slab_block",
    "double_high_block", "multi_high_block", "simple_storage_block", "drawer_block",
    "seat_block", "sofa_block", "stackable_block", "lamp_block", "toggleable_lamp_block",
    "chime_block", "change_over_time_block", "spreading_block", "surface_spreading_block",
    "decay_block", "grass_block", "leaves_block",
}

BLOCK_BEHAVIOR_SCHEMA = {
    "crop_block": {
        "fields": {
            "type": {"type": "enum", "values": ["crop_block"], "required": True},
            "grow_speed": {"type": "number", "required": False},
            "light_requirement": {"type": "int", "required": False},
            "max_light_requirement": {"type": "int", "required": False},
            "spawn_light_requirement": {"type": "int", "required": False},
            "max_spawn_light_requirement": {"type": "int", "required": False},
            "is_bone_meal_target": {"type": "boolean", "required": False},
            "bone_meal_age_bonus": {"type": "mapping", "required": False},
        }
    },
    "falling_block": {
        "fields": {
            "type": {"type": "enum", "values": ["falling_block"], "required": True},
            "hurt_entities": {"type": "boolean", "required": False},
            "hurt_amount": {"type": "int", "required": False},
            "landing_sound": {"type": "string", "required": False},
        }
    },
    "strippable_block": {
        "fields": {
            "type": {"type": "enum", "values": ["strippable_block"], "required": True},
            "stripped": {"type": "string", "required": True},
        }
    },
    "door_block": {
        "fields": {
            "type": {"type": "enum", "values": ["door_block"], "required": True},
        }
    },
    "trapdoor_block": {
        "fields": {
            "type": {"type": "enum", "values": ["trapdoor_block"], "required": True},
        }
    },
    "fence_block": {
        "fields": {
            "type": {"type": "enum", "values": ["fence_block"], "required": True},
        }
    },
    "fence_gate_block": {
        "fields": {
            "type": {"type": "enum", "values": ["fence_gate_block"], "required": True},
        }
    },
    "stairs_block": {
        "fields": {
            "type": {"type": "enum", "values": ["stairs_block"], "required": True},
        }
    },
    "slab_block": {
        "fields": {
            "type": {"type": "enum", "values": ["slab_block"], "required": True},
        }
    },
    "lamp_block": {
        "fields": {
            "type": {"type": "enum", "values": ["lamp_block"], "required": True},
        }
    },
    "toggleable_lamp_block": {
        "fields": {
            "type": {"type": "enum", "values": ["toggleable_lamp_block"], "required": True},
        }
    },
    "seat_block": {
        "fields": {
            "type": {"type": "enum", "values": ["seat_block"], "required": True},
            "seat_height": {"type": "number", "required": False},
        }
    },
    "simple_storage_block": {
        "fields": {
            "type": {"type": "enum", "values": ["simple_storage_block"], "required": True},
            "title": {"type": "string", "required": False},
            "rows": {"type": "int", "required": False},
        }
    },
    "drawer_block": {
        "fields": {
            "type": {"type": "enum", "values": ["drawer_block"], "required": True},
        }
    },
    "bouncing_block": {
        "fields": {
            "type": {"type": "enum", "values": ["bouncing_block"], "required": True},
            "bounce_percent": {"type": "number", "required": False, "default": 1.0},
            "fall_damage_multiplier": {"type": "number", "required": False},
            "sync_to_client": {"type": "boolean", "required": False},
        }
    },
    "sapling_block": {
        "fields": {
            "type": {"type": "enum", "values": ["sapling_block"], "required": True},
        }
    },
    "bush_block": {
        "fields": {
            "type": {"type": "enum", "values": ["bush_block"], "required": True},
            "max_stack": {"type": "int", "required": False},
            "grow_speed": {"type": "number", "required": False},
        }
    },
    "wall_torch_particle_block": {
        "fields": {
            "type": {"type": "enum", "values": ["wall_torch_particle_block"], "required": True},
        }
    },
    "tint_source_block": {
        "fields": {
            "type": {"type": "enum", "values": ["tint_source_block"], "required": True},
            "tint_color": {"type": "string", "required": False},
        }
    },
    "directional_attached_block": {
        "fields": {
            "type": {"type": "enum", "values": ["directional_attached_block"], "required": True},
        }
    },
    "near_liquid_block": {
        "fields": {
            "type": {"type": "enum", "values": ["near_liquid_block"], "required": True},
        }
    },
    "on_liquid_block": {
        "fields": {
            "type": {"type": "enum", "values": ["on_liquid_block"], "required": True},
        }
    },
    "concrete_powder_block": {
        "fields": {
            "type": {"type": "enum", "values": ["concrete_powder_block"], "required": True},
            "solid_block": {"type": "string", "required": True},
        }
    },
    "drop_experience_block": {
        "fields": {
            "type": {"type": "enum", "values": ["drop_experience_block"], "required": True},
            "min_exp": {"type": "int", "required": False},
            "max_exp": {"type": "int", "required": False},
        }
    },
    "display_item_block": {
        "fields": {
            "type": {"type": "enum", "values": ["display_item_block"], "required": True},
        }
    },
    "item_frame_block": {
        "fields": {
            "type": {"type": "enum", "values": ["item_frame_block"], "required": True},
            "glowing": {"type": "boolean", "required": False},
            "invisible": {"type": "boolean", "required": False},
        }
    },
    "simple_particle_block": {
        "fields": {
            "type": {"type": "enum", "values": ["simple_particle_block"], "required": True},
        }
    },
    "leaves_block": {
        "fields": {
            "type": {"type": "enum", "values": ["leaves_block"], "required": True},
        }
    },
    "sofa_block": {
        "fields": {
            "type": {"type": "enum", "values": ["sofa_block"], "required": True},
        }
    },
    "stackable_block": {
        "fields": {
            "type": {"type": "enum", "values": ["stackable_block"], "required": True},
            "max_stack": {"type": "int", "required": False},
        }
    },
    "change_over_time_block": {
        "fields": {
            "type": {"type": "enum", "values": ["change_over_time_block"], "required": True},
        }
    },
    "spreading_block": {
        "fields": {
            "type": {"type": "enum", "values": ["spreading_block"], "required": True},
        }
    },
    "decay_block": {
        "fields": {
            "type": {"type": "enum", "values": ["decay_block"], "required": True},
        }
    },
    "grass_block": {
        "fields": {
            "type": {"type": "enum", "values": ["grass_block"], "required": True},
        }
    },
    "surface_spreading_block": {
        "fields": {
            "type": {"type": "enum", "values": ["surface_spreading_block"], "required": True},
            "spread_chance": {"type": "number", "required": False},
        }
    },
    "face_attached_horizontal_directional_block": {
        "fields": {
            "type": {"type": "enum", "values": ["face_attached_horizontal_directional_block"], "required": True},
        }
    },
    "button_block": {
        "fields": {
            "type": {"type": "enum", "values": ["button_block"], "required": True},
            "press_time": {"type": "int", "required": False, "default": 20},
        }
    },
    "pressure_plate_block": {
        "fields": {
            "type": {"type": "enum", "values": ["pressure_plate_block"], "required": True},
        }
    },
    "vertical_crop_block": {
        "fields": {
            "type": {"type": "enum", "values": ["vertical_crop_block"], "required": True},
            "grow_speed": {"type": "number", "required": False},
        }
    },
    "stem_block": {
        "fields": {
            "type": {"type": "enum", "values": ["stem_block"], "required": True},
            "grow_speed": {"type": "number", "required": False},
        }
    },
    "attached_stem_block": {
        "fields": {
            "type": {"type": "enum", "values": ["attached_stem_block"], "required": True},
        }
    },
    "hanging_block": {
        "fields": {
            "type": {"type": "enum", "values": ["hanging_block"], "required": True},
        }
    },
    "hangable_block": {
        "fields": {
            "type": {"type": "enum", "values": ["hangable_block"], "required": True},
        }
    },
    "liquid_flowable_block": {
        "fields": {
            "type": {"type": "enum", "values": ["liquid_flowable_block"], "required": True},
        }
    },
    "near_liquid_block": {
        "fields": {
            "type": {"type": "enum", "values": ["near_liquid_block"], "required": True},
        }
    },
    "on_liquid_block": {
        "fields": {
            "type": {"type": "enum", "values": ["on_liquid_block"], "required": True},
        }
    },
    "snowy_block": {
        "fields": {
            "type": {"type": "enum", "values": ["snowy_block"], "required": True},
        }
    },
    "sturdy_base_block": {
        "fields": {
            "type": {"type": "enum", "values": ["sturdy_base_block"], "required": True},
        }
    },
    "budding_block": {
        "fields": {
            "type": {"type": "enum", "values": ["budding_block"], "required": True},
        }
    },
    "directional_attached_block": {
        "fields": {
            "type": {"type": "enum", "values": ["directional_attached_block"], "required": True},
        }
    },
    "double_high_block": {
        "fields": {
            "type": {"type": "enum", "values": ["double_high_block"], "required": True},
        }
    },
    "multi_high_block": {
        "fields": {
            "type": {"type": "enum", "values": ["multi_high_block"], "required": True},
            "height": {"type": "int", "required": False},
        }
    },
    "chime_block": {
        "fields": {
            "type": {"type": "enum", "values": ["chime_block"], "required": True},
        }
    },
}

# --- 3. 家具 (furniture) Schema ---

FURNITURE_SETTINGS_FIELDS = {
    "item": {"type": "string", "required": False},
    "hit_times": {"type": "int", "required": False},
    "sounds": {"type": "mapping", "required": False},
    "adventure_mode_breaking": {"type": "boolean", "required": False},
    "correct_tools": {"type": "list_of_string", "required": False},
}

FURNITURE_ELEMENT_TYPES = {"item_display", "text_display", "item", "armor_stand", "better_model", "model_engine"}

FURNITURE_ELEMENT_COMMON_FIELDS = {
    "type": {"type": "enum", "values": list(FURNITURE_ELEMENT_TYPES), "required": False},
    "item": {"type": "string", "required": False},
    "text": {"type": "string", "required": False},
    "model": {"type": "string", "required": False},
    "display_transform": {"type": "enum", "values": ["none", "third_person_left_hand", "third_person_right_hand",
        "first_person_left_hand", "first_person_right_hand", "head", "gui", "ground", "fixed", "on_shelf"], "required": False},
    "billboard": {"type": "enum", "values": ["fixed", "vertical", "horizontal", "center"], "required": False},
    "position": {"type": "string", "required": False},
    "translation": {"type": "string", "required": False},
    "pitch": {"type": "number", "required": False},
    "yaw": {"type": "number", "required": False},
    "scale": {"type": "number_or_string", "required": False},
    "rotation": {"type": "string_or_number", "required": False},
    "glow_color": {"type": "string", "required": False},
    "brightness": {"type": "mapping", "required": False},
    "view_range": {"type": "number", "required": False, "default": 1.0},
    "shadow_radius": {"type": "number", "required": False},
    "shadow_strength": {"type": "number", "required": False},
    "apply_dyed_color": {"type": "boolean", "required": False, "default": True},
    "tint_source": {"type": "list_of_string", "required": False},
    "small": {"type": "boolean", "required": False},
    "sight_trace": {"type": "boolean", "required": False},
    "line_width": {"type": "int", "required": False},
    "background_color": {"type": "string", "required": False},
    "text_opacity": {"type": "int", "required": False},
    "has_shadow": {"type": "boolean", "required": False},
    "is_see_through": {"type": "boolean", "required": False},
    "use_default_background_color": {"type": "boolean", "required": False},
    "alignment": {"type": "enum", "values": ["center", "left", "right"], "required": False},
}

FURNITURE_HITBOX_TYPES = {"interaction", "shulker", "happy_ghast", "custom"}

FURNITURE_HITBOX_COMMON = {
    "type": {"type": "enum", "values": list(FURNITURE_HITBOX_TYPES), "required": True},
    "position": {"type": "string", "required": False, "default": "0,0,0"},
    "scale": {"type": "number", "required": False, "default": 1},
    "can_use_item_on": {"type": "boolean", "required": False, "default": True},
    "can_be_hit_by_projctile": {"type": "boolean", "required": False, "default": True},
    "blocks_building": {"type": "boolean", "required": False, "default": True},
    "interactive": {"type": "boolean", "required": False},
    "invisible": {"type": "boolean", "required": False},
    "seats": {"type": "list", "required": False},
    "width": {"type": "number", "required": False, "default": 1},
    "height": {"type": "number", "required": False, "default": 2},
    "direction": {"type": "enum", "values": ["up", "down", "north", "west", "east", "south"], "required": False},
    "peek": {"type": "int", "required": False, "default": 0},
    "interaction_entity": {"type": "boolean", "required": False},
    "hard_collision": {"type": "boolean", "required": False, "default": True},
    "entity_type": {"type": "string", "required": False, "default": "slime"},
}

FURNITURE_VARIANT_FIELDS = {
    "loot_spawn_offset": {"type": "string", "required": False},
    "entity_culling": {"type": "boolean_or_mapping", "required": False},
    "elements": {"type": "list", "required": False},
    "hitboxes": {"type": "list", "required": False},
    "blueprint": {"type": "string", "required": False},
}

FURNITURE_BEHAVIOR_TYPES = {"display_item_furniture", "glowing_furniture", "simple_storage_furniture"}

# --- 4. 配方 (recipes) Schema ---

RECIPE_TYPES = {"shaped", "shapeless", "smelting", "blasting", "smoking",
                "campfire_cooking", "stonecutting", "smithing_transform",
                "smithing_trim", "shaped_transform", "brewing"}

RECIPE_CATEGORIES_SMELTING = ["food", "blocks", "misc"]
RECIPE_CATEGORIES_CRAFTING = ["building", "redstone", "equipment", "misc"]

RECIPE_COMMON_FIELDS = {
    "type": {"type": "enum", "values": list(RECIPE_TYPES), "required": True},
    "group": {"type": "string", "required": False},
    "category": {"type": "string", "required": False},
    "result": {"type": "mapping", "required": True},
    "conditions": {"type": "list", "required": False, "paid_only": True},
    "functions": {"type": "list", "required": False, "paid_only": True},
    "unlock_on_ingredient_obtained": {"type": "boolean", "required": False},
}

RECIPE_TYPE_SPECIFIC = {
    "shaped": {
        "required": ["type", "pattern", "ingredients", "result"],
        "fields": {
            "pattern": {"type": "list_of_string", "required": True},
            "ingredients": {"type": "mapping", "required": True},
            "result": {"type": "mapping", "required": True},
        }
    },
    "shapeless": {
        "required": ["type", "ingredients", "result"],
        "fields": {
            "ingredients": {"type": "list", "required": True},
            "result": {"type": "mapping", "required": True},
        }
    },
    "smelting": {
        "required": ["type", "ingredient", "result"],
        "fields": {
            "ingredient": {"type": "string", "required": True},
            "result": {"type": "mapping", "required": True},
            "experience": {"type": "number", "required": False},
            "time": {"type": "int", "required": False, "default": 200},
        }
    },
    "blasting": {"extends": "smelting"},
    "smoking": {"extends": "smelting"},
    "campfire_cooking": {"extends": "smelting"},
    "stonecutting": {
        "required": ["type", "ingredient", "result"],
        "fields": {
            "ingredient": {"type": "string", "required": True},
            "result": {"type": "mapping", "required": True},
        }
    },
    "smithing_transform": {
        "required": ["type", "base", "result"],
        "fields": {
            "template_type": {"type": "string", "required": False},
            "base": {"type": "string", "required": True},
            "addition": {"type": "string", "required": False},
            "result": {"type": "mapping", "required": True},
            "merge_components": {"type": "boolean", "required": False, "default": True},
            "transform_processors": {"type": "list", "required": False},
        }
    },
    "smithing_trim": {
        "required": ["type"],
        "fields": {
            "template_type": {"type": "string", "required": False},
            "base": {"type": "string", "required": False},
            "addition": {"type": "string", "required": False},
            "pattern": {"type": "string", "required": False, "version": "1.21.5+"},
        }
    },
    "shaped_transform": {
        "required": ["type", "pattern", "ingredients", "result"],
        "fields": {
            "pattern": {"type": "list_of_string", "required": True},
            "ingredients": {"type": "mapping", "required": True},
            "result": {"type": "mapping", "required": True},
            "transform_processors": {"type": "list", "required": False},
        }
    },
    "brewing": {
        "required": ["type", "ingredient", "result"],
        "fields": {
            "ingredient": {"type": "string", "required": True},
            "container": {"type": "string", "required": False},
            "result": {"type": "mapping", "required": True},
        }
    },
}

RECIPE_RESULT_FIELDS = {
    "id": {"type": "string", "required": True},
    "count": {"type": "int", "required": False, "default": 1},
    "post_processors": {"type": "list", "required": False},
}

# --- 5. 装备 (equipments) Schema ---

EQUIPMENT_TYPES = {"component", "trim"}

EQUIPMENT_PRESET_MODELS = [
    "humanoid", "humanoid_leggings", "wings", "wolf_body", "horse_body",
    "llama_body", "pig_saddle", "strider_saddle", "camel_saddle",
    "horse_saddle", "donkey_saddle", "mule_saddle", "skeleton_horse_saddle",
    "zombie_horse_saddle", "happy_ghast_body", "camel_husk_saddle", "nautilus_body",
]

# --- 6. 分类 (categories) Schema ---

CATEGORY_FIELDS = {
    "name": {"type": "string", "required": True},
    "lore": {"type": "list", "required": False},
    "hidden": {"type": "boolean", "required": False, "default": False},
    "priority": {"type": "int", "required": False},
    "icon": {"type": "string", "required": True},
    "conditions": {"type": "list", "required": False},
    "list": {"type": "list_of_string", "required": False},
    "all_items": {"type": "boolean", "required": False, "default": False},
}

# --- 7. 事件 (events) Schema ---

EVENT_TRIGGERS_ITEM = ["break", "right_click", "left_click", "consume", "pick_up", "attack"]
EVENT_TRIGGERS_BLOCK = ["break", "place", "right_click", "left_click", "step"]
EVENT_TRIGGERS_FURNITURE = ["break", "place", "right_click"]

FUNCTION_TYPES = {
    "cancel_event", "run", "command", "message", "actionbar", "title",
    "open_window", "break_block", "place_block", "update_block_property",
    "transform_block", "drop_loot", "update_interaction_tick",
    "set_count", "set_food", "set_saturation", "swing_hand",
    "particle", "potion_effect", "remove_potion_effect",
    "leveler_exp", "set_cooldown", "remove_cooldown",
    "play_sound", "cast_mythic_skill", "spawn_furniture",
    "remove_furniture", "replace_furniture", "rotate_furniture",
    "teleport", "toast", "damage", "set_variable",
    "merchant_trade", "remove_entity", "if_else", "when",
    "damage_item", "cycle_block_property", "set_exp", "set_level",
    "play_totem_animation", "close_inventory", "clear_item",
    "heal", "spawn_mythic_mob",
}

FUNCTION_COMMON = {
    "type": {"type": "enum", "values": list(FUNCTION_TYPES), "required": True},
    "conditions": {"type": "list", "required": False},
}

# --- 8. 条件 (conditions) Schema ---

CONDITION_TYPES = {
    "any_of", "all_of", "inverted", "falling_block", "survives_explosion",
    "has_item", "match_item", "match_block_property", "match_block",
    "match_entity", "match_furniture_variant", "enchantment",
    "table_bonus", "random", "permission", "expression",
    "string_equals", "string_contains", "regex", "is_null",
    "hand", "on_cooldown", "worldguard:region", "distance",
    "has_player", "inventory_has_item", "is_bedrock_player", "test_flag",
}

# --- 9. 模板 (templates) Schema ---

ARGUMENT_EXTENDED_TYPES = {"condition", "when", "to_upper_case", "to_lower_case",
                           "self_increase_int", "expression"}

# --- 10. 唱片机 (jukebox_songs) Schema ---

JUKEBOX_SONG_FIELDS = {
    "sound": {"type": "string", "required": False},
    "comparator_output": {"type": "int", "required": False},
    "duration": {"type": "int", "required": False},
    "range": {"type": "int", "required": False},
}

# --- 11. 画 (paintings) Schema ---

PAINTING_FIELDS = {
    "width": {"type": "int", "required": False},
    "height": {"type": "int", "required": False},
    "title": {"type": "string", "required": False},
    "author": {"type": "string", "required": False},
    "admin_tab": {"type": "boolean", "required": False},
}

# --- 12. 全局变量 (global_variables) Schema ---

GLOBAL_VARIABLE_FIELDS = {
    "value": {"type": "any", "required": True},
}


# =============================================================================
# 校验引擎
# =============================================================================

class ConfigValidator:
    """CraftEngine 配置文件校验器"""

    def __init__(self, mc_version: str = DEFAULT_MINECRAFT_VERSION):
        self.errors: List[ValidationError] = []
        self.mc_version = mc_version
        # Cache for cross-reference validation
        self.defined_items: Set[str] = set()
        self.defined_blocks: Set[str] = set()
        self.defined_furniture: Set[str] = set()
        self.defined_recipes: Set[str] = set()
        self.defined_categories: Set[str] = set()
        self.defined_templates: Set[str] = set()

    def add_error(self, path: str, error_type: str, message: str,
                  severity: str = "error", expected: str = None, actual: str = None):
        self.errors.append(ValidationError(path, error_type, message, severity, expected, actual))

    def _validate_version_condition(self, key: str, path: str):
        """校验版本条件 $$ 格式"""
        if VERSION_PREFIX.match(key):
            if not VERSION_CONDITION.match(key):
                self.add_error(path, "invalid_syntax",
                               f"版本条件 '{key}' 格式无效，期望格式: $$1.21.2, $$>=1.21.2, $$1.20.1~1.21.4, $$fallback",
                               severity="warning")
            return True
        return False

    def _check_section_identifier(self, section_id: str) -> tuple:
        """检查并拆分节标识符，返回 (base_key, identifier) 或 (section_id, None)"""
        if "#" in section_id:
            parts = section_id.split("#", 1)
            return parts[0], parts[1]
        return section_id, None

    def _validate_section_identifiers(self, data: dict):
        """校验所有节标识符的唯一性"""
        seen_identifiers = {}  # base_key -> set of identifiers
        for root_key in data:
            if VERSION_PREFIX.match(str(root_key)):
                continue
            if "#" in str(root_key):
                base_key, identifier = self._check_section_identifier(root_key)
                if base_key in seen_identifiers:
                    if identifier in seen_identifiers[base_key]:
                        self.add_error(f"(root).{root_key}", "duplicate_identifier",
                                       f"节标识符 '{identifier}' 在根键 '{base_key}' 中重复",
                                       severity="warning")
                    else:
                        seen_identifiers[base_key].add(identifier)
                else:
                    seen_identifiers[base_key] = {identifier}

    def _check_version(self, version_req: Optional[str]) -> bool:
        """检查版本要求是否满足"""
        if version_req is None or version_req == "any":
            return True
        # Simple version check: "1.21.2+" means mc_version >= "1.21.2"
        if version_req.endswith("+"):
            req_ver = version_req[:-1]
            return self._compare_versions(self.mc_version, req_ver) >= 0
        return True

    def _compare_versions(self, v1: str, v2: str) -> int:
        """比较版本号, 返回 -1/0/1"""
        try:
            parts1 = [int(x) for x in v1.split(".")]
            parts2 = [int(x) for x in v2.split(".")]
            for i in range(max(len(parts1), len(parts2))):
                p1 = parts1[i] if i < len(parts1) else 0
                p2 = parts2[i] if i < len(parts2) else 0
                if p1 < p2:
                    return -1
                elif p1 > p2:
                    return 1
            return 0
        except (ValueError, IndexError):
            return 0

    def _check_type(self, value: Any, expected_type: str, path: str) -> bool:
        """检查值类型"""
        type_checks = {
            "string": lambda v: isinstance(v, str),
            "int": lambda v: isinstance(v, int),
            "number": lambda v: isinstance(v, (int, float)),
            "boolean": lambda v: isinstance(v, bool),
            "list": lambda v: isinstance(v, list),
            "mapping": lambda v: isinstance(v, dict),
            "list_of_string": lambda v: isinstance(v, list) and all(isinstance(x, str) for x in v),
            "list_of_mapping": lambda v: isinstance(v, list) and all(isinstance(x, dict) for x in v),
            "string_or_mapping": lambda v: isinstance(v, (str, dict)),
            "string_or_list": lambda v: isinstance(v, (str, list)),
            "boolean_or_mapping": lambda v: isinstance(v, (bool, dict)),
            "boolean_or_string": lambda v: isinstance(v, (bool, str)),
            "mapping_or_list": lambda v: isinstance(v, (dict, list)),
            "number_or_string": lambda v: isinstance(v, (int, float, str)),
            "string_or_number": lambda v: isinstance(v, (str, int, float)),
            "any": lambda v: True,
        }
        checker = type_checks.get(expected_type)
        if checker is None:
            return True  # Unknown type, skip check
        return checker(value)

    def _check_enum(self, value: Any, enum_values: List[str], path: str) -> bool:
        """检查枚举值"""
        if not isinstance(value, str):
            return True
        if value in enum_values:
            return True
        self.add_error(
            path, "invalid_enum",
            f"字段值 '{value}' 不是有效的枚举值",
            expected=f"{{{', '.join(enum_values)}}}",
            actual=value
        )
        return False

    def validate_file(self, filepath: str) -> List[Dict]:
        """校验 YAML 配置文件"""
        self.errors = []

        # 解析 YAML
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.add_error("(file)", "read_error", f"无法读取文件: {e}")
            return self._get_results()

        try:
            data = yaml.load(content, Loader=CraftEngineLoader)
        except yaml.YAMLError as e:
            self.add_error("(yaml)", "yaml_parse_error", f"YAML 解析错误: {e}")
            return self._get_results()

        if not isinstance(data, dict):
            self.add_error("(root)", "invalid_root", "配置文件根节点必须是一个映射 (dict)")
            return self._get_results()

        # 第一遍: 收集所有定义 (用于交叉引用校验)
        self._collect_definitions(data)

        # 第一遍: 校验高级语法
        self._validate_section_identifiers(data)

        # 第二遍: 校验每个配置块
        for root_key, root_value in data.items():
            # 跳过版本条件键 ($$1.21.2 等)
            if VERSION_PREFIX.match(root_key):
                continue
            self._validate_root_key(root_key, root_value, "")

        return self._get_results()

    def _get_results(self) -> List[Dict]:
        """获取校验结果"""
        return [e.to_dict() for e in self.errors]

    def _collect_definitions(self, data: dict):
        """第一遍收集: 收集所有定义的 ID 用于交叉引用"""
        for root_key, root_value in data.items():
            if VERSION_PREFIX.match(root_key) or not isinstance(root_value, dict):
                continue
            if root_key in ("items", "blocks", "furniture", "recipes", "categories", "templates"):
                for item_id in root_value.keys():
                    if VERSION_PREFIX.match(str(item_id)):
                        continue
                    clean_id, _ = self._check_section_identifier(str(item_id))
                    if root_key == "items":
                        self.defined_items.add(clean_id)
                    elif root_key == "blocks":
                        self.defined_blocks.add(clean_id)
                    elif root_key == "furniture":
                        self.defined_furniture.add(clean_id)
                    elif root_key == "recipes":
                        self.defined_recipes.add(clean_id)
                    elif root_key == "categories":
                        self.defined_categories.add(clean_id)
                    elif root_key == "templates":
                        self.defined_templates.add(clean_id)

    def _validate_root_key(self, key: str, value: Any, base_path: str):
        """校验根键"""
        path = f"{base_path}{key}"

        # 校验版本条件键格式
        if self._validate_version_condition(key, path):
            return

        # 检查节标识符
        base_key, _ = self._check_section_identifier(key)

        if base_key not in VALID_ROOT_KEYS:
            self.add_error(path, "unknown_root_key", f"未知的根键 '{base_key}' (原键: '{key}')")
            return

        # 简单声明型根键（如 namespace: my_mod）允许非 dict 值
        if base_key in ("namespace",):
            if not isinstance(value, str):
                self.add_error(path, "wrong_type", f"根键 '{key}' 的值应为字符串 (namespace 声明)")
            return

        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", f"根键 '{key}' 的值应为映射 (dict)")
            return

        # 根据根键类型进行专项校验
        validators = {
            "items": self._validate_items,
            "blocks": self._validate_blocks,
            "furniture": self._validate_furniture,
            "recipes": self._validate_recipes,
            "equipments": self._validate_equipments,
            "categories": self._validate_categories,
            "loots": self._validate_loot_tables,
            "vanilla_loots": self._validate_vanilla_loots,
            "templates": self._validate_templates,
            "jukebox_songs": self._validate_jukebox_songs,
            "paintings": self._validate_paintings,
            "global_variables": self._validate_global_variables,
        }

        validator = validators.get(base_key)
        if validator:
            for item_id, item_value in value.items():
                if VERSION_PREFIX.match(str(item_id)):
                    continue
                clean_id, _ = self._check_section_identifier(str(item_id))
                validator(clean_id, item_value, f"{path}.")

    # =========================================================================
    # 物品校验
    # =========================================================================

    def _validate_items(self, item_id: str, value: Any, base_path: str):
        """校验单个物品"""
        path = f"{base_path}{item_id}"

        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", f"物品 '{item_id}' 的值应为映射")
            return

        # 校验字段
        for field_name, field_value in value.items():
            field_path = f"{path}.{field_name}"

            # 跳过版本条件键和模板系统字段
            if VERSION_PREFIX.match(field_name):
                continue
            if field_name.startswith("$$"):
                continue
            if field_name in TEMPLATE_SYSTEM_FIELDS:
                continue

            # 检查字段是否在 schema 中
            schema = ITEM_FIELDS.get(field_name)

            if field_name == "data":
                self._validate_item_data(field_value, field_path)
            elif field_name == "client_bound_data":
                if field_value is None:
                    self.add_error(field_path, "paid_only", "字段 'client_bound_data' 为付费版专属（值为空占位符）",
                                   severity="warning")
                elif isinstance(field_value, dict):
                    self._validate_item_data(field_value, field_path, is_client_bound=True)
                else:
                    self.add_error(field_path, "wrong_type", "client_bound_data 应为映射或空")
            elif field_name == "settings":
                self._validate_item_settings(field_value, field_path)
            elif field_name == "behavior" or field_name == "behaviors":
                self._validate_item_behavior(field_value, field_path)
            elif field_name == "model" or field_name == "legacy_model":
                self._validate_item_model(field_value, field_path, field_name)
            elif field_name == "events":
                self._validate_events(field_value, field_path, "item")
            elif schema:
                if schema.get("paid_only"):
                    self.add_error(field_path, "paid_only", f"字段 '{field_name}' 为付费版专属")
                if not self._check_type(field_value, schema["type"], field_path):
                    self.add_error(field_path, "wrong_type", f"字段 '{field_name}' 类型错误",
                                   expected=schema["type"], actual=type(field_value).__name__)
                if field_name == "category" and isinstance(field_value, str):
                    if field_value not in self.defined_categories:
                        self.add_error(field_path, "invalid_ref", f"分类 '{field_value}' 未在 categories 中定义")
                if schema.get("version") and not self._check_version(schema.get("version")):
                    self.add_error(field_path, "version_mismatch", f"字段 '{field_name}' 需要 {schema['version']}，当前版本 {self.mc_version}", severity="warning")
            else:
                self.add_error(field_path, "unknown_field", f"物品字段 '{field_name}' 在 Wiki 中未找到")

        # material 在 CraftEngine 中并非严格必填：
        # - 家具/方块变体的展示实体子物品不需要 material（仅作渲染引用）
        # - 使用 template 或 behavior 时可隐式提供材质
        # 因此当 material 缺失时不报错，仅在有时校验其格式
        for field_name, field_value in value.items():
            if field_name == "material" and not isinstance(field_value, str):
                self.add_error(f"{path}.material", "wrong_type", "material 应为字符串")

    def _validate_item_data(self, value: Any, path: str, is_client_bound: bool = False):
        """校验物品数据"""
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "data 应为映射")
            return

        for field_name, field_value in value.items():
            field_path = f"{path}.{field_name}"

            if VERSION_PREFIX.match(field_name):
                continue

            # 处理 data 内的节标识符: conditional#1, conditional#2 等
            base_field, identifier = self._check_section_identifier(field_name)
            if identifier:
                # 有节标识符，根据基础字段名处理
                if base_field == "conditional":
                    # conditional#1/#2 是递归条件数据块
                    if is_client_bound:
                        self._validate_item_data(field_value, field_path, is_client_bound=True)
                    else:
                        self.add_error(field_path, "paid_only",
                                       f"字段 '{field_name}' (conditional) 仅在 client_bound_data 下可用",
                                       severity="warning")
                else:
                    schema = ITEM_DATA_FIELDS.get(base_field)
                    if not schema:
                        self.add_error(field_path, "unknown_field",
                                       f"data 字段 '{field_name}' (基础名 '{base_field}') 在 Wiki 中未找到")
                continue

            schema = ITEM_DATA_FIELDS.get(field_name)
            if field_name == "conditional":
                if not is_client_bound:
                    self.add_error(field_path, "paid_only", "'conditional' 仅在 client_bound_data 下可用，且为付费版专属",
                                   severity="warning")
                self._validate_item_data(field_value, field_path, is_client_bound)
                continue

            if schema:
                if schema.get("paid_only") and not is_client_bound:
                    self.add_error(field_path, "paid_only", f"字段 '{field_name}' 为付费版专属")
                if not self._check_type(field_value, schema["type"], field_path):
                    self.add_error(field_path, "wrong_type", f"字段 '{field_name}' 类型错误",
                                   expected=schema["type"], actual=type(field_value).__name__)
                if schema.get("version") and not self._check_version(schema.get("version")):
                    self.add_error(field_path, "version_mismatch", f"字段 '{field_name}' 需要 {schema['version']}",
                                   severity="warning")
            else:
                self.add_error(field_path, "unknown_field", f"data 字段 '{field_name}' 在 Wiki 中未找到")

    def _validate_item_settings(self, value: Any, path: str):
        """校验物品设置"""
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "settings 应为映射")
            return

        for field_name, field_value in value.items():
            field_path = f"{path}.{field_name}"

            if field_name in TEMPLATE_SYSTEM_FIELDS:
                continue
            if VERSION_PREFIX.match(field_name):
                continue

            schema = ITEM_SETTINGS_FIELDS.get(field_name)

            if schema:
                if not self._check_type(field_value, schema["type"], field_path):
                    self.add_error(field_path, "wrong_type", f"settings 字段 '{field_name}' 类型错误",
                                   expected=schema["type"], actual=type(field_value).__name__)
                # 专项校验
                if field_name == "invulnerable" and isinstance(field_value, list):
                    for v in field_value:
                        if v not in INVULNERABLE_TYPES:
                            self.add_error(f"{field_path}[{v}]", "invalid_enum",
                                           f"免疫类型 '{v}' 无效", expected=f"{{{', '.join(INVULNERABLE_TYPES)}}}")
                if field_name == "glow_color" and isinstance(field_value, str):
                    self._check_enum(field_value, DYE_COLORS, field_path)
                if field_name == "tags" and isinstance(field_value, list):
                    for tag in field_value:
                        if isinstance(tag, str) and ":" not in tag and not tag.startswith("#"):
                            self.add_error(f"{field_path}[{tag}]", "invalid_format",
                                           f"标签 '{tag}' 应为 'namespace:tag' 或 '#namespace:tag' 格式", severity="warning")
                if field_name == "equipment" and isinstance(field_value, dict):
                    if "asset_id" not in field_value:
                        self.add_error(f"{field_path}", "missing_field", "equipment 需要 'asset_id' 字段")
                    if "slot" in field_value and field_value["slot"] not in EQUIPMENT_SLOTS:
                        self.add_error(f"{field_path}.slot", "invalid_enum",
                                       f"装备槽位 '{field_value['slot']}' 无效", expected=f"{{{', '.join(EQUIPMENT_SLOTS)}}}")
            else:
                self.add_error(field_path, "unknown_field", f"settings 字段 '{field_name}' 在 Wiki 中未找到")

    def _validate_item_behavior(self, value: Any, path: str):
        """校验物品行为"""
        if isinstance(value, list):
            for i, b in enumerate(value):
                self._validate_single_item_behavior(b, f"{path}[{i}]")
        elif isinstance(value, dict):
            self._validate_single_item_behavior(value, path)
        else:
            self.add_error(path, "wrong_type", "behavior 应为映射或列表")

    def _validate_single_item_behavior(self, value: dict, path: str):
        """校验单个物品行为"""
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "行为应为映射")
            return

        if "type" not in value:
            self.add_error(path, "missing_field", "行为缺少 'type' 字段")
            return

        bt = value["type"]
        if bt not in ITEM_BEHAVIOR_TYPES:
            self.add_error(f"{path}.type", "invalid_enum", f"物品行为类型 '{bt}' 无效",
                           expected=f"{{{', '.join(sorted(ITEM_BEHAVIOR_TYPES))}}}")
            return

        schema = ITEM_BEHAVIOR_SCHEMA.get(bt)
        if schema:
            for field_name, field_value in value.items():
                field_path = f"{path}.{field_name}"
                field_schema = schema["fields"].get(field_name)
                if field_schema:
                    if not self._check_type(field_value, field_schema["type"], field_path):
                        self.add_error(field_path, "wrong_type", f"字段 '{field_name}' 类型错误",
                                       expected=field_schema["type"])
                    if field_schema.get("values") and isinstance(field_value, str):
                        self._check_enum(field_value, field_schema["values"], field_path)
                else:
                    self.add_error(field_path, "unknown_field", f"行为 '{bt}' 的字段 '{field_name}' 未定义")

            # 校验必填字段
            if "rules" in value and isinstance(value["rules"], dict):
                for variant, rules in value["rules"].items():
                    if isinstance(rules, dict):
                        if "rotation" in rules and rules["rotation"] not in ITEM_FURNITURE_RULES_ROTATION:
                            self.add_error(f"{path}.rules.{variant}.rotation", "invalid_enum",
                                           f"旋转配置 '{rules['rotation']}' 无效")
                        if "alignment" in rules and rules["alignment"] not in ITEM_FURNITURE_RULES_ALIGNMENT:
                            self.add_error(f"{path}.rules.{variant}.alignment", "invalid_enum",
                                           f"对齐配置 '{rules['alignment']}' 无效")

    def _validate_item_model(self, value: Any, path: str, model_type: str):
        """校验物品模型"""
        if isinstance(value, str):
            # 简化路径写法
            return
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", f"{model_type} 应为字符串或映射")
            return

    # =========================================================================
    # 方块校验
    # =========================================================================

    def _validate_blocks(self, block_id: str, value: Any, base_path: str):
        """校验单个方块"""
        path = f"{base_path}{block_id}"

        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", f"方块 '{block_id}' 的值应为映射")
            return

        # 检查: state 或 states（建议有，但某些行为型方块可以不显式定义）
        has_state = "state" in value
        has_states = "states" in value
        has_properties = "properties" in value
        if not has_state and not has_states:
            if has_properties:
                # 使用 properties 的方块需要 behavior 配合
                if "behavior" not in value and "behaviors" not in value:
                    self.add_error(path, "missing_field",
                                   "方块有 'properties' 但缺少 'behavior' (properties 需要 behavior 配合)")
            else:
                # 没有 state/states/properties 的纯行为方块，降级为警告
                self.add_error(path, "missing_field",
                               "方块缺少 'state' 或 'states' 字段 (行为型方块可忽略此警告)",
                               severity="warning")

        for field_name, field_value in value.items():
            field_path = f"{path}.{field_name}"

            if VERSION_PREFIX.match(field_name):
                continue

            if field_name == "state":
                self._validate_block_state(field_value, field_path)
            elif field_name == "states":
                self._validate_block_states(field_value, field_path)
            elif field_name == "settings":
                self._validate_block_settings(field_value, field_path)
            elif field_name == "behavior" or field_name == "behaviors":
                self._validate_block_behavior(field_value, field_path)
            elif field_name == "loot":
                self._validate_loot_table(field_value, field_path)
            elif field_name == "events":
                self._validate_events(field_value, field_path, "block")
            elif field_name == "properties":
                self._validate_block_properties(field_value, field_path)
            elif field_name == "namespace":
                pass  # 命名空间声明，直接接受
            else:
                self.add_error(field_path, "unknown_field", f"方块字段 '{field_name}' 在 Wiki 中未找到")

    def _validate_block_state(self, value: Any, path: str):
        """校验单状态"""
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "state 应为映射")
            return

        for field_name, field_value in value.items():
            field_path = f"{path}.{field_name}"
            if field_name == "auto_state":
                if isinstance(field_value, str):
                    if field_value not in AUTO_STATE_GROUPS:
                        self.add_error(field_path, "invalid_enum", f"auto_state '{field_value}' 无效",
                                       expected=f"{{{', '.join(AUTO_STATE_GROUPS)}}}")
                elif isinstance(field_value, dict):
                    atype = field_value.get("type")
                    if atype and atype not in AUTO_STATE_GROUPS:
                        self.add_error(field_path, "invalid_enum", f"auto_state type '{atype}' 无效")
            elif field_name == "state":
                if not isinstance(field_value, str):
                    self.add_error(field_path, "wrong_type", "state 值应为字符串")
            elif field_name in ("model", "models"):
                pass  # 模型字段结构复杂，浅层校验
            elif field_name in ("texture", "textures"):
                pass  # 简化模型，单张/多张纹理
            elif field_name == "transparent":
                if not isinstance(field_value, bool):
                    self.add_error(field_path, "wrong_type", "transparent 应为布尔值")
            elif field_name == "entity_renderer":
                self._validate_entity_renderer(field_value, field_path)
            elif field_name == "id":
                if not isinstance(field_value, int):
                    self.add_error(field_path, "wrong_type", "id 应为整数")
            else:
                self.add_error(field_path, "unknown_field", f"state 字段 '{field_name}' 在 Wiki 中未找到")

    def _validate_block_states(self, value: Any, path: str):
        """校验多状态"""
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "states 应为映射")
            return

        for section in ("properties", "appearances", "variants"):
            if section in value:
                if section == "properties":
                    self._validate_block_properties(value[section], f"{path}.properties")

    def _validate_block_properties(self, value: Any, path: str):
        """校验方块属性"""
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "properties 应为映射")
            return

        for prop_name, prop_value in value.items():
            prop_path = f"{path}.{prop_name}"
            if not isinstance(prop_value, dict):
                # 简写格式: open: false 等价于 open: { type: boolean, default: false }
                # 接受 boolean/string/int 类型的简写值
                if isinstance(prop_value, (bool, str, int, float)):
                    continue
                self.add_error(prop_path, "wrong_type", f"属性 '{prop_name}' 应为映射或标量简写值")
                continue
            if "type" not in prop_value:
                # 空映射或只有默认值的属性（如 open: {}），使用默认类型 int 或无类型
                if prop_value:
                    self.add_error(prop_path, "missing_field", f"属性 '{prop_name}' 缺少 'type' 字段",
                                   severity="warning")
                continue
            ptype = prop_value["type"]
            if ptype not in PROPERTY_TYPES:
                self.add_error(f"{prop_path}.type", "invalid_enum", f"属性类型 '{ptype}' 不在 Wiki 定义的 13 种类型中",
                               expected=f"{{{', '.join(PROPERTY_TYPES.keys())}}}")

    def _validate_block_settings(self, value: Any, path: str):
        """校验方块设置"""
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "settings 应为映射")
            return

        for field_name, field_value in value.items():
            field_path = f"{path}.{field_name}"

            if field_name in TEMPLATE_SYSTEM_FIELDS:
                continue

            schema = BLOCK_SETTINGS_FIELDS.get(field_name)

            if schema:
                if not self._check_type(field_value, schema["type"], field_path):
                    self.add_error(field_path, "wrong_type", f"方块设置 '{field_name}' 类型错误",
                                   expected=schema["type"])
                if schema.get("values") and isinstance(field_value, str):
                    self._check_enum(field_value, schema["values"], field_path)
                if field_name == "push_reaction" and isinstance(field_value, str):
                    self._check_enum(field_value, ["NORMAL", "DESTROY", "BLOCK", "IGNORE", "PUSH_ONLY"], field_path)
                if field_name == "fluid_state" and isinstance(field_value, str):
                    self._check_enum(field_value, ["empty", "water"], field_path)
            else:
                self.add_error(field_path, "unknown_field", f"方块设置字段 '{field_name}' 在 Wiki 中未找到")

    def _validate_block_behavior(self, value: Any, path: str):
        """校验方块行为"""
        if isinstance(value, list):
            for i, b in enumerate(value):
                self._validate_single_block_behavior(b, f"{path}[{i}]")
        elif isinstance(value, dict):
            self._validate_single_block_behavior(value, path)
        else:
            self.add_error(path, "wrong_type", "behavior 应为映射或列表")

    def _validate_single_block_behavior(self, value: dict, path: str):
        """校验单个方块行为"""
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "行为应为映射")
            return
        if "type" not in value:
            self.add_error(path, "missing_field", "行为缺少 'type' 字段")
            return

        bt = value["type"]
        if bt not in BLOCK_BEHAVIOR_TYPES:
            self.add_error(f"{path}.type", "invalid_enum", f"方块行为类型 '{bt}' 无效",
                           expected=f"{{{', '.join(sorted(BLOCK_BEHAVIOR_TYPES))}}}")

    def _validate_entity_renderer(self, value: Any, path: str):
        """校验实体渲染器"""
        if isinstance(value, list):
            for i, v in enumerate(value):
                self._validate_entity_renderer_single(v, f"{path}[{i}]")
        elif isinstance(value, dict):
            self._validate_entity_renderer_single(value, path)

    def _validate_entity_renderer_single(self, value: dict, path: str):
        """校验单个实体渲染器元素"""
        if not isinstance(value, dict):
            return
        # 常见字段检查与 furniture element 类似
        for f in ("type", "item", "text", "translation", "position", "scale", "rotation", "billboard"):
            if f in value and f == "billboard" and isinstance(value[f], str):
                self._check_enum(value[f], ["fixed", "vertical", "horizontal", "center"], f"{path}.{f}")

    # =========================================================================
    # 家具校验
    # =========================================================================

    def _validate_furniture(self, furniture_id: str, value: Any, base_path: str):
        """校验单个家具"""
        path = f"{base_path}{furniture_id}"

        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", f"家具 '{furniture_id}' 的值应为映射")
            return

        for field_name, field_value in value.items():
            field_path = f"{path}.{field_name}"

            if field_name == "settings":
                self._validate_furniture_settings(field_value, field_path)
            elif field_name == "variants":
                self._validate_furniture_variants(field_value, field_path)
            elif field_name == "behavior" or field_name == "behaviors":
                self._validate_furniture_behavior(field_value, field_path)
            elif field_name == "loot":
                self._validate_loot_table(field_value, field_path)
            elif field_name == "events":
                self._validate_events(field_value, field_path, "furniture")
            else:
                self.add_error(field_path, "unknown_field", f"家具字段 '{field_name}' 在 Wiki 中未找到")

    def _validate_furniture_settings(self, value: Any, path: str):
        """校验家具设置"""
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "furniture settings 应为映射")
            return
        for field_name in value:
            if field_name not in FURNITURE_SETTINGS_FIELDS:
                self.add_error(f"{path}.{field_name}", "unknown_field", f"家具设置字段 '{field_name}' 在 Wiki 中未找到")

    def _validate_furniture_variants(self, value: Any, path: str):
        """校验家具变体"""
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "variants 应为映射")
            return

        for variant_name, variant_value in value.items():
            var_path = f"{path}.{variant_name}"
            if not isinstance(variant_value, dict):
                continue

            for field_name, field_value in variant_value.items():
                field_path = f"{var_path}.{field_name}"
                if field_name == "elements" and isinstance(field_value, list):
                    for i, elem in enumerate(field_value):
                        self._validate_furniture_element(elem, f"{field_path}[{i}]")
                elif field_name == "hitboxes" and isinstance(field_value, list):
                    for i, hb in enumerate(field_value):
                        self._validate_furniture_hitbox(hb, f"{field_path}[{i}]")
                elif field_name == "entity_culling":
                    if isinstance(field_value, dict):
                        if "view_distance" in field_value and not isinstance(field_value["view_distance"], (int, float)):
                            self.add_error(f"{field_path}.view_distance", "wrong_type", "view_distance 应为数字")
                        if "ray_tracing" in field_value and not isinstance(field_value["ray_tracing"], bool):
                            self.add_error(f"{field_path}.ray_tracing", "wrong_type", "ray_tracing 应为布尔值")

    def _validate_furniture_element(self, value: Any, path: str):
        """校验家具元素"""
        if not isinstance(value, dict):
            return
        etype = value.get("type")
        if etype and etype not in FURNITURE_ELEMENT_TYPES:
            self.add_error(f"{path}.type", "invalid_enum", f"元素类型 '{etype}' 无效",
                           expected=f"{{{', '.join(FURNITURE_ELEMENT_TYPES)}}}")
        for field_name in value:
            if field_name not in FURNITURE_ELEMENT_COMMON_FIELDS:
                self.add_error(f"{path}.{field_name}", "unknown_field", f"元素字段 '{field_name}' 在 Wiki 中未找到")

    def _validate_furniture_hitbox(self, value: Any, path: str):
        """校验家具判定箱"""
        if not isinstance(value, dict):
            return
        htype = value.get("type")
        if htype and htype not in FURNITURE_HITBOX_TYPES:
            self.add_error(f"{path}.type", "invalid_enum", f"判定箱类型 '{htype}' 无效",
                           expected=f"{{{', '.join(FURNITURE_HITBOX_TYPES)}}}")

        if htype == "shulker" and "direction" in value:
            self._check_enum(value["direction"], ["up", "down", "north", "west", "east", "south"], f"{path}.direction")

        # 检查 seats 格式
        if "seats" in value and isinstance(value["seats"], list):
            for i, seat in enumerate(value["seats"]):
                if isinstance(seat, str):
                    parts = seat.split()
                    if len(parts) > 2:
                        self.add_error(f"{path}.seats[{i}]", "invalid_format",
                                       f"座位格式应为 'x,y,z yaw' 或 'x,y,z'", actual=seat, severity="warning")

    def _validate_furniture_behavior(self, value: Any, path: str):
        """校验家具行为"""
        if isinstance(value, dict):
            bt = value.get("type")
            if bt and bt not in FURNITURE_BEHAVIOR_TYPES:
                self.add_error(f"{path}.type", "invalid_enum", f"家具行为类型 '{bt}' 无效",
                               expected=f"{{{', '.join(FURNITURE_BEHAVIOR_TYPES)}}}")

    # =========================================================================
    # 配方校验
    # =========================================================================

    def _validate_recipes(self, recipe_id: str, value: Any, base_path: str):
        """校验单个配方"""
        path = f"{base_path}{recipe_id}"

        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", f"配方 '{recipe_id}' 的值应为映射")
            return

        if "type" not in value:
            self.add_error(path, "missing_field", "配方缺少 'type' 字段 (必填)")
            return

        rtype = value["type"]
        if rtype not in RECIPE_TYPES:
            self.add_error(f"{path}.type", "invalid_enum", f"配方类型 '{rtype}' 无效",
                           expected=f"{{{', '.join(RECIPE_TYPES)}}}")
            return

        # 获取对应类型的 schema
        type_schema = RECIPE_TYPE_SPECIFIC.get(rtype)
        if type_schema and "extends" in type_schema:
            type_schema = RECIPE_TYPE_SPECIFIC.get(type_schema["extends"])

        if type_schema:
            for field_name in type_schema.get("required", []):
                if field_name not in value:
                    self.add_error(path, "missing_field", f"配方 '{rtype}' 缺少必填字段 '{field_name}'")

        # 校验 category
        if "category" in value:
            cat = value["category"]
            if rtype in ("smelting", "blasting", "smoking", "campfire_cooking"):
                if cat not in RECIPE_CATEGORIES_SMELTING:
                    self.add_error(f"{path}.category", "invalid_enum", f"烧炼配方 category '{cat}' 无效",
                                   expected=f"{{{', '.join(RECIPE_CATEGORIES_SMELTING)}}}")
            elif rtype in ("shaped", "shapeless", "shaped_transform"):
                if cat not in RECIPE_CATEGORIES_CRAFTING:
                    self.add_error(f"{path}.category", "invalid_enum", f"合成配方 category '{cat}' 无效",
                                   expected=f"{{{', '.join(RECIPE_CATEGORIES_CRAFTING)}}}")

        # 校验 result
        if "result" in value and isinstance(value["result"], dict):
            result = value["result"]
            if "id" not in result:
                self.add_error(f"{path}.result", "missing_field", "result 缺少 'id' 字段")
            if "visual_result" in value:
                self.add_error(f"{path}.visual_result", "paid_only", "visual_result 为付费版专属")

    # =========================================================================
    # 装备校验
    # =========================================================================

    def _validate_equipments(self, equip_id: str, value: Any, base_path: str):
        """校验装备"""
        path = f"{base_path}{equip_id}"
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "equipments 应为映射")
            return
        if "type" in value and value["type"] not in EQUIPMENT_TYPES:
            self.add_error(f"{path}.type", "invalid_enum", f"装备类型 '{value['type']}' 无效")

    # =========================================================================
    # 分类校验
    # =========================================================================

    def _validate_categories(self, cat_id: str, value: Any, base_path: str):
        """校验分类"""
        path = f"{base_path}{cat_id}"
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "categories 应为映射")
            return
        for field_name, field_value in value.items():
            field_path = f"{path}.{field_name}"
            schema = CATEGORY_FIELDS.get(field_name)
            if schema:
                if not self._check_type(field_value, schema["type"], field_path):
                    self.add_error(field_path, "wrong_type", f"分类字段 '{field_name}' 类型错误")
                if field_name == "list" and isinstance(field_value, list):
                    for item_ref in field_value:
                        if isinstance(item_ref, str) and item_ref.startswith("#"):
                            cref = item_ref[1:]
                            if cref not in self.defined_categories:
                                self.add_error(f"{field_path}[{item_ref}]", "invalid_ref",
                                               f"引用的子分类 '{cref}' 未定义，可能来自其他包，将被跳过", severity="warning")
            else:
                self.add_error(field_path, "unknown_field", f"分类字段 '{field_name}' 在 Wiki 中未找到")

    # =========================================================================
    # 战利品表校验
    # =========================================================================

    def _validate_loot_table(self, value: Any, path: str):
        """校验战利品表"""
        if not isinstance(value, dict) and not isinstance(value, str):
            self.add_error(path, "wrong_type", "loot 应为字符串或映射")
            return

        if isinstance(value, dict):
            if "pools" in value and isinstance(value["pools"], list):
                for i, pool in enumerate(value["pools"]):
                    if isinstance(pool, dict) and "entries" in pool:
                        for j, entry in enumerate(pool["entries"]):
                            if isinstance(entry, dict):
                                etype = entry.get("type")
                                if etype and etype not in ("item", "furniture_item", "exp", "alternatives"):
                                    self.add_error(f"{path}.pools[{i}].entries[{j}].type", "invalid_enum",
                                                   f"战利品条目类型 '{etype}' 无效")

    def _validate_loot_tables(self, loot_id: str, value: Any, base_path: str):
        """校验顶级 loots"""
        self._validate_loot_table(value, f"{base_path}{loot_id}")

    def _validate_vanilla_loots(self, loot_id: str, value: Any, base_path: str):
        """校验原版战利品覆盖"""
        path = f"{base_path}{loot_id}"
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "vanilla_loots 应为映射")
            return

        # 校验 vanilla_loots 必填字段
        if "type" not in value:
            self.add_error(path, "missing_field", "vanilla_loots 缺少 'type' 字段 (必填)")
        elif value["type"] not in ("block", "entity", "chest", "fishing", "gift"):
            self.add_error(f"{path}.type", "invalid_enum",
                           f"vanilla_loots type '{value.get('type')}' 无效",
                           expected="{block, entity, chest, fishing, gift}")

        if "target" not in value:
            self.add_error(path, "missing_field", "vanilla_loots 缺少 'target' 字段 (必填)")

        if "loot" in value:
            self._validate_loot_table(value["loot"], f"{path}.loot")

    # =========================================================================
    # 模板校验
    # =========================================================================

    def _validate_templates(self, tmpl_id: str, value: Any, base_path: str):
        """校验模板"""
        path = f"{base_path}{tmpl_id}"
        if not isinstance(value, dict):
            self.add_error(path, "wrong_type", "templates 应为映射")

    # =========================================================================
    # 事件校验
    # =========================================================================

    def _validate_events(self, value: Any, path: str, context_type: str):
        """校验事件配置"""
        if isinstance(value, list):
            for i, event in enumerate(value):
                self._validate_single_event(event, f"{path}[{i}]", context_type)
        elif isinstance(value, dict):
            for trigger, functions in value.items():
                self._validate_event_trigger(trigger, f"{path}.{trigger}", context_type)
                if isinstance(functions, list):
                    for j, func in enumerate(functions):
                        self._validate_function(func, f"{path}.{trigger}[{j}]")

    def _validate_single_event(self, event: dict, path: str, context_type: str):
        """校验单个事件"""
        if not isinstance(event, dict):
            return
        trigger = event.get("on")
        if trigger:
            triggers = {
                "item": EVENT_TRIGGERS_ITEM,
                "block": EVENT_TRIGGERS_BLOCK,
                "furniture": EVENT_TRIGGERS_FURNITURE,
            }.get(context_type, [])
            if isinstance(trigger, str) and trigger not in triggers:
                self.add_error(f"{path}.on", "invalid_enum", f"事件触发器 '{trigger}' 对于 {context_type} 无效")

    def _validate_event_trigger(self, trigger: str, path: str, context_type: str):
        """校验事件触发器"""
        triggers = {
            "item": EVENT_TRIGGERS_ITEM,
            "block": EVENT_TRIGGERS_BLOCK,
            "furniture": EVENT_TRIGGERS_FURNITURE,
        }.get(context_type, [])
        if trigger not in triggers:
            self.add_error(path, "invalid_enum", f"触发器 '{trigger}' 对于 {context_type} 无效",
                           expected=f"{{{', '.join(triggers)}}}")

    def _validate_function(self, func: dict, path: str):
        """校验函数"""
        if not isinstance(func, dict):
            return
        if "type" not in func:
            self.add_error(path, "missing_field", "函数缺少 'type' 字段")
            return
        ftype = func["type"]
        if ftype not in FUNCTION_TYPES:
            self.add_error(f"{path}.type", "invalid_enum", f"函数类型 '{ftype}' 无效")

        # 专项参数校验
        if ftype == "command" and "command" not in func:
            self.add_error(path, "missing_field", "command 函数缺少 'command' 字段")
        if ftype == "message" and "message" not in func:
            self.add_error(path, "missing_field", "message 函数缺少 'message' 字段")
        if ftype == "particle" and "particle" not in func:
            self.add_error(path, "missing_field", "particle 函数缺少 'particle' 字段")
        if ftype == "set_cooldown" and "time" not in func:
            self.add_error(path, "missing_field", "set_cooldown 函数缺少 'time' 字段")
        if ftype == "play_sound" and "sound" not in func:
            self.add_error(path, "missing_field", "play_sound 函数缺少 'sound' 字段")
        if ftype == "spawn_mythic_mob" and "mob" not in func:
            self.add_error(path, "missing_field", "spawn_mythic_mob 函数缺少 'mob' 字段")
        if ftype == "cast_mythic_skill" and "skill" not in func:
            self.add_error(path, "missing_field", "cast_mythic_skill 函数缺少 'skill' 字段")
        if ftype == "set_variable" and "name" not in func:
            self.add_error(path, "missing_field", "set_variable 函数缺少 'name' 字段")
        if ftype == "toast" and ("toast" not in func or "icon" not in func):
            self.add_error(path, "missing_field", "toast 函数缺少 'toast' 或 'icon' 字段")

        # 函数内嵌条件校验
        if "conditions" in func and isinstance(func["conditions"], list):
            for i, cond in enumerate(func["conditions"]):
                self._validate_condition(cond, f"{path}.conditions[{i}]")

    # =========================================================================
    # 条件校验
    # =========================================================================

    def _validate_condition(self, cond: dict, path: str):
        """校验条件"""
        if not isinstance(cond, dict):
            return
        if "type" not in cond:
            self.add_error(path, "missing_field", "条件缺少 'type' 字段")
            return
        ctype = cond["type"]
        # 支持 ! 前缀取反
        clean_type = ctype.lstrip("!")
        if clean_type not in CONDITION_TYPES:
            self.add_error(f"{path}.type", "invalid_enum", f"条件类型 '{ctype}' 不在 Wiki 定义的 27+ 种条件类型中",
                           expected=f"{{{', '.join(sorted(CONDITION_TYPES))}}}")

        # 专项校验
        if clean_type == "permission" and "permission" not in cond:
            self.add_error(path, "missing_field", "permission 条件缺少 'permission' 字段")
        if clean_type == "random" and "value" not in cond:
            self.add_error(path, "missing_field", "random 条件缺少 'value' 字段")
        if clean_type == "match_item" and "id" not in cond:
            self.add_error(path, "missing_field", "match_item 条件缺少 'id' 字段")
        if clean_type in ("any_of", "all_of") and "terms" not in cond:
            self.add_error(path, "missing_field", f"{clean_type} 条件缺少 'terms' 字段")
        if clean_type == "inverted" and "term" not in cond:
            self.add_error(path, "missing_field", "inverted 条件缺少 'term' 字段")
        if clean_type == "expression" and "expression" not in cond:
            self.add_error(path, "missing_field", "expression 条件缺少 'expression' 字段")
        if clean_type == "worldguard:region" and "regions" not in cond:
            self.add_error(path, "missing_field", "worldguard:region 条件缺少 'regions' 字段")

    # =========================================================================
    # 其他配置类型
    # =========================================================================

    def _validate_jukebox_songs(self, song_id: str, value: Any, base_path: str):
        """校验唱片机曲目"""
        pass  # 结构简单，基本类型校验即可

    def _validate_paintings(self, paint_id: str, value: Any, base_path: str):
        """校验画"""
        pass

    def _validate_global_variables(self, var_id: str, value: Any, base_path: str):
        """校验全局变量"""
        path = f"{base_path}{var_id}"
        if isinstance(value, dict):
            # dict 格式的全局变量，校验内部字段
            for field_name, field_value in value.items():
                schema = GLOBAL_VARIABLE_FIELDS.get(field_name)
                if schema and not self._check_type(field_value, schema["type"], f"{path}.{field_name}"):
                    self.add_error(f"{path}.{field_name}", "wrong_type", f"全局变量字段 '{field_name}' 类型错误")


# =============================================================================
# 主入口
# =============================================================================

def print_text_report(errors: List[Dict], filepath: str):
    """纯文本格式输出"""
    if not errors:
        print(f"✅ 校验通过! '{filepath}' 未发现错误。")
        return

    error_count = sum(1 for e in errors if e["severity"] == "error")
    warning_count = sum(1 for e in errors if e["severity"] == "warning")

    print(f"❌ 发现 {error_count} 个错误, {warning_count} 个警告 — '{filepath}':")
    print()

    for e in errors:
        prefix = "[错误]" if e["severity"] == "error" else "[警告]"
        print(f"  {prefix} {e['path']}")
        print(f"      {e['message']}")
        if e["expected"]:
            print(f"      期望: {e['expected']}")
        if e["actual"]:
            print(f"      实际: {e['actual']}")
        print()


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="CraftEngine YAML 配置文件校验器 v" + VERSION,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python craftengine_validator.py config.yml
  python craftengine_validator.py config.yml --version 1.20.1
  python craftengine_validator.py config.yml --json
  python craftengine_validator.py config.yml --text
  python craftengine_validator.py *.yml --json > errors.json
        """
    )
    parser.add_argument("files", nargs="+", help="要校验的 YAML 文件路径")
    parser.add_argument("--version", default=DEFAULT_MINECRAFT_VERSION, help=f"Minecraft 版本 (默认: {DEFAULT_MINECRAFT_VERSION})")
    parser.add_argument("--json", action="store_true", help="输出 JSON 格式")
    parser.add_argument("--text", action="store_true", help="输出纯文本格式 (默认)")
    parser.add_argument("--output", "-o", help="输出到文件 (默认输出到 stdout)")

    args = parser.parse_args()

    # 默认输出模式
    if not args.json and not args.text:
        args.text = True

    validator = ConfigValidator(mc_version=args.version)
    all_results = {}
    has_errors = False

    for filepath in args.files:
        if not os.path.exists(filepath):
            print(f"错误: 文件不存在 '{filepath}'", file=sys.stderr)
            has_errors = True
            continue

        errors = validator.validate_file(filepath)
        all_results[filepath] = errors

        if errors:
            has_errors = True

    # 输出
    output_lines = []

    if args.text:
        for filepath, errors in all_results.items():
            import io
            buf = io.StringIO()
            # Redirect print to capture
            old_stdout = sys.stdout
            sys.stdout = buf
            print_text_report(errors, filepath)
            sys.stdout = old_stdout
            output_lines.append(buf.getvalue())

    if args.json:
        output_lines.append(json.dumps(all_results, ensure_ascii=False, indent=2))

    output = "\n".join(output_lines)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
    else:
        try:
            print(output, end="")
        except UnicodeEncodeError:
            # Handle systems with non-UTF-8 encoding (e.g. Windows GBK)
            ascii_output = output.encode('ascii', 'replace').decode('ascii')
            print(ascii_output, end="")

    sys.exit(1 if has_errors else 0)


if __name__ == "__main__":
    main()
