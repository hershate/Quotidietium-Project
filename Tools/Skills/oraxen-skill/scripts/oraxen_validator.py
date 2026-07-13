#!/usr/bin/env python3
"""
Oraxen YAML 配置文件校验器
================================
基于 Oraxen Docs Origin (官方 Wiki) 内容构建，用于校验 Oraxen 插件 YAML 配置文件。

校验范围:
  - 物品根字段 (displayname, material, Pack, Components, Mechanics 等)
  - 废弃字段检测 (itemname -> displayname 等)
  - Pack / Components / Mechanics 字段合法性
  - 方块机制 (noteblock / stringblock / chorusblock / shaped_block / furniture)
  - 家具配置 (type / barrier / hitbox / seat / storage / light / evolution)
  - 配方类型 (docs 声明目前仅支持 shaped)
  - 可染色材质限制 (POTION / LEATHER_HORSE_ARMOR)
  - 不兼容机制组合 (backpack + backpack_cosmetic 等)
  - 枚举值合法性 (furniture type / storage type / slot / tool_types 等)

输出格式: JSON (错误列表) 和/或 纯文本
参考 Wiki: references/Oraxen Docs Origin/

用法:
  python oraxen_validator.py <config.yml>
  python oraxen_validator.py <config.yml> --json
  python oraxen_validator.py <config.yml> --text
  python oraxen_validator.py *.yml --json > errors.json

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
from typing import Any, Dict, List, Optional, Set, Tuple

# =============================================================================
# 常量定义 (严格基于 Oraxen Docs Origin)
# =============================================================================

VERSION = "1.0.0"
DEFAULT_MINECRAFT_VERSION = "1.21.2"

# --- 物品根字段 (Getting Started.md / Components.md) ---
# docs 中物品配置的标准顶层字段
VALID_ITEM_FIELDS: Set[str] = {
    "displayname", "material", "color", "lore", "Pack", "Components",
    "Mechanics", "ItemFlags", "AttributeModifiers", "PotionEffects",
    "excludeFromInventory", "unstackable", "injectID",
}

# 废弃/已更名的字段 -> 正确字段名
# docs 统一使用 displayname；itemname 为旧版字段 (Components.md 部分示例残留，但
# Getting Started.md / 绝大多数 docs 均用 displayname)
DEPRECATED_FIELDS: Dict[str, str] = {
    "itemname": "displayname",
}

# --- Pack 字段 (Appearance & Models.md) ---
VALID_PACK_FIELDS: Set[str] = {
    "generate_model", "parent_model", "model", "textures",
    "pulling_models", "charged_model", "blocking_model", "cast_model",
    "gui_model", "oversized_in_gui", "hand_animation_on_swap",
    "swap_animation_scale", "damaged_models", "custom_model_data",
}

# docs 中出现的 parent_model 值 (Appearance & Models.md)
VALID_PARENT_MODELS: Set[str] = {
    "item/handheld", "item/generated", "block/cube", "block/cube_all",
    "block/cube_column", "block/template_single_face", "item/generated",
}

# --- Components 字段 (Components.md, 1.20.5+) ---
VALID_COMPONENTS: Set[str] = {
    "durability", "food", "consumable", "tool", "equippable",
    "jukebox_playable", "item_model", "max_stack_size", "damage_resistant",
    "fire_resistant", "glider", "tooltip_style", "item_name",
    "custom_model_data", "enchantable", "attribute_modifiers",
    "consumable_v2",  # 1.21.2+ consumable 重命名候选
}

# --- Mechanics 列表 (mechanics.yml.md: 44 个机制分 5 类) ---
# 杂项 (Miscellaneous) - 9
MECHANICS_MISC: Set[str] = {
    "commands", "armor_effects", "consumable", "consumable_potion_effects",
    "custom", "itemtype", "soulbound", "backpack", "music_disc", "misc",
}
# 游戏机制 (Gameplay) - 13
MECHANICS_GAMEPLAY: Set[str] = {
    "custom_block_sounds", "noteblock", "stringblock", "chorusblock",
    "shaped_block", "block", "furniture", "durability", "efficiency",
    "repair", "food", "toggle_light",
}
# 战斗 (Combat) - 7
MECHANICS_COMBAT: Set[str] = {
    "lifeleech", "bleeding", "thor", "energyblast", "fireball",
    "witherskull", "knockback_strike", "spear_lunge",
}
# 农耕 (Farming) - 6
MECHANICS_FARMING: Set[str] = {
    "bigmining", "harvesting", "smelting", "watering", "bottledexp",
    "bedrockbreak",
}
# 装饰 (Cosmetic) - 5
MECHANICS_COSMETIC: Set[str] = {
    "aura", "backpack_cosmetic", "hat", "skin", "skinnable",
}

ALL_VALID_MECHANICS: Set[str] = (
    MECHANICS_MISC | MECHANICS_GAMEPLAY | MECHANICS_COMBAT
    | MECHANICS_FARMING | MECHANICS_COSMETIC
)

# 方块类机制 (不能在同一物品上组合) - mechanics.yml.md "Incompatible Combinations"
BLOCK_MECHANICS: Set[str] = {
    "noteblock", "stringblock", "chorusblock", "shaped_block", "block",
}

# --- 家具相关枚举 (Furniture/Overview.md / Display Entities.md) ---
VALID_FURNITURE_TYPES: Set[str] = {
    "DISPLAY_ENTITY", "ITEM_FRAME", "GLOW_ITEM_FRAME", "ARMOR_STAND",
}
# storage 类型 (ChorusBlock.md / furniture storage)
VALID_STORAGE_TYPES: Set[str] = {
    "STORAGE", "PERSONAL", "ENDERCHEST", "DISPOSAL", "SHULKER",
}
# backpack_cosmetic slot (Backpack Cosmetic.md)
VALID_COSMETIC_SLOTS: Set[str] = {
    "HEAD", "CHEST", "LEGS", "FEET", "HAND", "OFF_HAND", "INVENTORY",
}
# equippable slot (Components.md)
VALID_EQUIPPABLE_SLOTS: Set[str] = {
    "HEAD", "CHEST", "LEGS", "FEET", "HAND", "OFF_HAND",
}
# 全局 tool_types (mechanics.yml.md)
VALID_TOOL_TIER: Set[str] = {
    "WOODEN", "STONE", "IRON", "GOLDEN", "DIAMOND", "NETHERITE",
}
# best_tools 工具类型 (blocks docs)
VALID_TOOL_TYPES: Set[str] = {
    "PICKAXE", "AXE", "SHEARS", "SHOVEL", "HOE", "SWORD",
}
# shaped_block 类型 (ShapedBlock.md)
VALID_SHAPED_BLOCK_TYPES: Set[str] = {
    "STAIR", "SLAB", "DOOR", "TRAPDOOR", "GRATE", "BULB",
}

# --- 可染色材质 (Dyeable Items.md) ---
# docs 明确: "based on POTION and LEATHER_HORSE_ARMOR"
VALID_DYEABLE_MATERIALS: Set[str] = {"POTION", "LEATHER_HORSE_ARMOR"}

# --- 配方类型 (Recipes.md) ---
# docs 明确: "for the moment only shaped recipes are supported"
VALID_RECIPE_TYPES: Set[str] = {"shaped"}

# --- 不兼容机制组合 (mechanics.yml.md "Incompatible Combinations") ---
# 每组内的机制不能同时出现在同一物品的 Mechanics 下
INCOMPATIBLE_GROUPS: List[Set[str]] = [
    {"backpack", "backpack_cosmetic"},
    # 多个方块机制不能组合: {"noteblock","stringblock","chorusblock","shaped_block","block"}
    # (下方单独处理: 同一物品出现 >=2 个方块机制即报错)
]

# --- 各 Mechanic 物品级子字段 (Item Abilities docs) ---
# 用于检测明显非法的子字段名 (非穷举, 仅收录 docs 明确记载的字段)
MECHANIC_SUBFIELDS: Dict[str, Set[str]] = {
    # Combat.md
    "thor": {"lightning_bolts_amount", "random_location_variation", "delay", "charges"},
    "lifeleech": {"amount"},
    "bleeding": {"chance", "duration", "damage_per_interval", "interval"},
    "energyblast": {"delay", "length", "damage", "charges", "particle"},
    "witherskull": {"charged", "delay", "charges"},
    "fireball": {"delay", "yield", "speed", "charges"},
    "knockback_strike": {
        "required_hits", "knockback_horizontal", "knockback_vertical",
        "reset_time", "play_sound", "sound_type", "sound_volume",
        "sound_pitch", "particle",
    },
    "spear_lunge": {
        "active_model", "intermediate_models", "smooth_frames",
        "charge_ticks", "lunge_velocity", "max_range", "damage",
        "min_damage", "knockback", "hitbox_radius", "min_charge_percent",
        "charge_slowdown", "max_hold_ticks", "max_targets",
        "particles", "sounds",
    },
    # Farming.md
    "harvesting": {"cooldown", "radius", "height", "lower_item_durability"},
    "bigmining": {"radius", "depth", "vein_miner", "blocks"},
    "smelting": {"enabled", "play_sound"},
    "bottledexp": {"ratio"},
    "bedrockbreak": {"hardness", "probability"},
    "watering": {"filledCanItem", "emptyCanItem"},
    # Miscellaneous.md
    "backpack": {"rows", "title", "open_sound", "close_sound"},
    "backpack_cosmetic": {
        "slot", "model", "offset", "scale", "view_distance",
        "hide_in_spectator", "small", "visible_to_self",
    },
    "food": {"hunger", "saturation", "replacement", "effect_probability", "effects"},
    "consumable": {"effects"},
    "consumable_potion_effects": set(),  # 动态键为药水效果名
    "soulbound": {"lose_chance", "enabled"},
    "durability": {"value"},
    "efficiency": {"amount"},
    "repair": {"ratio", "fixed_amount"},
    "aura": {"type", "particle"},
    "itemtype": {"value"},
    "toggle_light": {"light", "toggle_light"},
    "misc": {
        "breaks_from_cactus", "burns_in_fire", "burns_in_lava",
        "disable_vanilla_interactions", "can_strip_logs",
        "piglins_ignore_when_equipped", "compostable", "allow_in_vanilla_recipes",
    },
    "skin": {"consume"},
    "skinnable": set(),  # 空对象
    "hat": {"enabled"},
    "music_disc": {"song"},
    "armor_effects": set(),  # 动态键为药水效果名
    "commands": {"cooldown", "permission", "one_usage", "console", "player", "opped_player"},
    "custom": set(),  # 动态子键
}

# aura 有效类型 (Miscellaneous.md)
VALID_AURA_TYPES: Set[str] = {"simple", "ring", "helix"}

# ItemFlags 枚举 (Getting Started.md 提及)
VALID_ITEM_FLAGS: Set[str] = {
    "HIDE_ATTRIBUTES", "HIDE_ENCHANTS", "HIDE_DESTROYS", "HIDE_UNBREAKABLE",
    "HIDE_PLACED_ON", "HIDE_ADDITIONAL_TOOLTIP", "HIDE_ARMOR_TRIM",
}

# furniture light 范围 (Overview.md: must be between 1 and 15)
FURNITURE_LIGHT_MIN = 1
FURNITURE_LIGHT_MAX = 15


# =============================================================================
# 错误类型定义
# =============================================================================

class ValidationError:
    """校验错误"""

    def __init__(self, path: str, error_type: str, message: str,
                 severity: str = "error", suggestion: str = ""):
        self.path = path
        self.error_type = error_type
        self.message = message
        self.severity = severity  # error / warning
        self.suggestion = suggestion

    def to_dict(self) -> Dict:
        d = {
            "path": self.path,
            "type": self.error_type,
            "severity": self.severity,
            "message": self.message,
        }
        if self.suggestion:
            d["suggestion"] = self.suggestion
        return d

    def to_text(self) -> str:
        prefix = "错误" if self.severity == "error" else "警告"
        line = f"[{prefix}] {self.path} ({self.error_type}): {self.message}"
        if self.suggestion:
            line += f"\n        建议: {self.suggestion}"
        return line


# =============================================================================
# 校验器
# =============================================================================

class OraxenValidator:
    """Oraxen YAML 配置校验器"""

    def __init__(self, mc_version: str = DEFAULT_MINECRAFT_VERSION):
        self.mc_version = mc_version
        self.errors: List[ValidationError] = []
        self.defined_items: Set[str] = set()

    # ------------------------------------------------------------------
    # 辅助
    # ------------------------------------------------------------------
    def add_error(self, path: str, error_type: str, message: str,
                  severity: str = "error", suggestion: str = ""):
        self.errors.append(ValidationError(
            path, error_type, message, severity, suggestion
        ))

    def _is_commented_block(self, data: Any) -> bool:
        """YAML 解析后注释已丢失; 此函数用于检测全文件是否仅含注释 (data is None)"""
        return data is None

    def _check_enum(self, value: Any, enum_values: Set[str], path: str,
                    label: str) -> bool:
        if value not in enum_values:
            self.add_error(
                path, "invalid_enum",
                f"无效的 {label}: '{value}' (合法值: {sorted(enum_values)})",
            )
            return False
        return True

    def _check_int_range(self, value: Any, lo: int, hi: int, path: str,
                         label: str) -> bool:
        if not isinstance(value, int) or isinstance(value, bool):
            self.add_error(
                path, "invalid_type",
                f"{label} 应为整数 ({lo}-{hi}), 实际: {type(value).__name__}",
            )
            return False
        if value < lo or value > hi:
            self.add_error(
                path, "out_of_range",
                f"{label} 越界: {value} (合法范围: {lo}-{hi})",
            )
            return False
        return True

    # ------------------------------------------------------------------
    # 主入口
    # ------------------------------------------------------------------
    def validate_file(self, filepath: str) -> List[Dict]:
        self.errors = []
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            self.add_error("(file)", "read_error", f"无法读取文件: {e}")
            return self._get_results()

        # .md 文件: 提取 ```yaml 代码块逐个校验 (Oraxen Template 为文档内嵌 YAML)
        if filepath.lower().endswith(".md"):
            return self._validate_markdown(filepath, content)

        return self._validate_yaml_text(content)

    def _validate_yaml_text(self, content: str) -> List[Dict]:
        """校验纯 YAML 文本"""
        try:
            data = yaml.safe_load(content)
        except yaml.YAMLError as e:
            self.add_error("(yaml)", "yaml_parse_error", f"YAML 解析错误: {e}")
            return self._get_results()

        if self._is_commented_block(data):
            return self._get_results()

        if not isinstance(data, dict):
            self.add_error("(root)", "invalid_root",
                           "配置文件根节点必须是一个映射 (dict)")
            return self._get_results()

        for item_id, item_value in data.items():
            self._validate_item(str(item_id), item_value, "")
        return self._get_results()

    def _validate_markdown(self, filepath: str, content: str) -> List[Dict]:
        """从 Markdown 文件提取 ```yaml 代码块并逐个校验"""
        self.errors = []
        # 匹配 ```yaml ... ``` 或 ```yml ... ```
        pattern = re.compile(r"```ya?ml\n(.*?)```", re.DOTALL)
        blocks = pattern.findall(content)
        if not blocks:
            # 无 YAML 代码块, 跳过 (纯说明文档)
            return self._get_results()

        fname = os.path.basename(filepath)
        # 物品结构指示字段: 出现任一即视为可校验的物品配置块
        item_indicators = VALID_ITEM_FIELDS | ALL_VALID_MECHANICS | {"Pack", "Components", "Mechanics"}

        for idx, block in enumerate(blocks, 1):
            try:
                data = yaml.safe_load(block)
            except yaml.YAMLError:
                # 单块解析失败: 跳过 (可能是片段, 不影响整体)
                continue
            if not isinstance(data, dict):
                continue
            # 过滤: 仅校验看起来是物品/机制配置的块 (含已知字段或机制名)
            # 检查顶层键 或 二层值是否含物品指示字段
            looks_like_config = False
            for k, v in data.items():
                if k in item_indicators:
                    looks_like_config = True
                    break
                if isinstance(v, dict) and any(
                    sub in item_indicators for sub in v.keys()
                ):
                    looks_like_config = True
                    break
            if not looks_like_config:
                continue  # 跳过纯示例片段 (如 offset: {x,y,z})

            sub = OraxenValidator(self.mc_version)
            results = sub._validate_yaml_text(block)
            for r in results:
                r["path"] = f"{fname}#block{idx}:{r['path']}"
                self.errors.append(ValidationError(
                    r["path"], r["type"], r["message"],
                    r.get("severity", "error"), r.get("suggestion", "")
                ))
        return self._get_results()

    def _get_results(self) -> List[Dict]:
        return [e.to_dict() for e in self.errors]

    # ------------------------------------------------------------------
    # 物品校验
    # ------------------------------------------------------------------
    def _validate_item(self, item_id: str, value: Any, base_path: str):
        path = f"{base_path}{item_id}"
        if not isinstance(value, dict):
            self.add_error(path, "invalid_type",
                           f"物品配置应为映射 (dict), 实际: {type(value).__name__}")
            return

        # 收集物品 ID (用于交叉引用)
        self.defined_items.add(item_id)

        # 检测废弃字段 (itemname 等)
        for field, replacement in DEPRECATED_FIELDS.items():
            if field in value:
                self.add_error(
                    f"{path}.{field}", "deprecated_field",
                    f"使用了废弃字段 '{field}'",
                    suggestion=f"改用 '{replacement}' (docs 统一使用 {replacement})",
                )

        # 检查未知根字段 (仅当未命中废弃字段时, 避免重复报错)
        for key in value.keys():
            if key in DEPRECATED_FIELDS:
                continue  # 已报废弃
            if key not in VALID_ITEM_FIELDS:
                # 容忍一些 docs 中出现但未收录的边角字段 (severity=warning)
                self.add_error(
                    f"{path}.{key}", "unknown_field",
                    f"未知物品字段 '{key}' (未在 docs 中记载)",
                    severity="warning",
                    suggestion=f"合法字段: {sorted(VALID_ITEM_FIELDS)}",
                )

        # 校验各部分
        if "Pack" in value:
            self._validate_pack(value["Pack"], f"{path}.Pack")
        if "Components" in value:
            self._validate_components(value["Components"], f"{path}.Components")
        if "Mechanics" in value:
            self._validate_mechanics(value["Mechanics"], f"{path}.Mechanics", item_id)
        if "ItemFlags" in value:
            self._validate_item_flags(value["ItemFlags"], f"{path}.ItemFlags")
        if "color" in value:
            self._validate_color(value, f"{path}")

    # ------------------------------------------------------------------
    # Pack 校验
    # ------------------------------------------------------------------
    def _validate_pack(self, value: Any, path: str):
        if not isinstance(value, dict):
            self.add_error(path, "invalid_type", "Pack 应为映射 (dict)")
            return
        for key in value.keys():
            if key not in VALID_PACK_FIELDS:
                self.add_error(
                    f"{path}.{key}", "unknown_field",
                    f"未知 Pack 字段 '{key}' (未在 Appearance & Models.md 中记载)",
                    severity="warning",
                )
        if "parent_model" in value:
            pm = value["parent_model"]
            if isinstance(pm, str) and pm not in VALID_PARENT_MODELS:
                # parent_model 可能是自定义路径; 仅当看起来像标准值时才报
                if "/" not in pm and ":" not in pm:
                    self.add_error(
                        f"{path}.parent_model", "invalid_enum",
                        f"未知 parent_model: '{pm}'",
                        severity="warning",
                        suggestion=f"docs 记载值: {sorted(VALID_PARENT_MODELS)}",
                    )

    # ------------------------------------------------------------------
    # Components 校验
    # ------------------------------------------------------------------
    def _validate_components(self, value: Any, path: str):
        if not isinstance(value, dict):
            self.add_error(path, "invalid_type", "Components 应为映射 (dict)")
            return
        for key in value.keys():
            if key not in VALID_COMPONENTS:
                self.add_error(
                    f"{path}.{key}", "unknown_field",
                    f"未知 Components 字段 '{key}' (未在 Components.md 中记载)",
                    severity="warning",
                )
        # equippable.slot 枚举
        if "equippable" in value and isinstance(value["equippable"], dict):
            if "slot" in value["equippable"]:
                self._check_enum(
                    value["equippable"]["slot"], VALID_EQUIPPABLE_SLOTS,
                    f"{path}.equippable.slot", "equippable slot",
                )

    # ------------------------------------------------------------------
    # Mechanics 校验
    # ------------------------------------------------------------------
    def _validate_mechanics(self, value: Any, path: str, item_id: str):
        if not isinstance(value, dict):
            self.add_error(path, "invalid_type", "Mechanics 应为映射 (dict)")
            return

        present = set(value.keys())

        # 1. 检查不兼容组合: backpack + backpack_cosmetic
        for group in INCOMPATIBLE_GROUPS:
            combo = present & group
            if len(combo) >= 2:
                self.add_error(
                    path, "incompatible_combination",
                    f"不兼容机制组合: {sorted(combo)} (mechanics.yml.md 明确禁止同时使用)",
                    suggestion="将二者分别配置在不同物品上",
                )

        # 2. 检查多个方块机制组合 (>=2 个即报错)
        block_combos = present & BLOCK_MECHANICS
        if len(block_combos) >= 2:
            self.add_error(
                path, "incompatible_combination",
                f"多个方块机制不可共存: {sorted(block_combos)}",
                suggestion="一个物品只能有一个方块机制 (noteblock/stringblock/chorusblock/shaped_block)",
            )

        # 3. 逐个校验机制
        for mech_name, mech_value in value.items():
            self._validate_single_mechanic(mech_name, mech_value, f"{path}.{mech_name}")

    def _validate_single_mechanic(self, name: str, value: Any, path: str):
        if name not in ALL_VALID_MECHANICS:
            self.add_error(
                path, "unknown_mechanic",
                f"未知机制 '{name}' (未在 mechanics.yml.md 44 个机制中)",
                severity="warning",
            )
            return

        if value is None:
            return  # 空机制 (如 skinnable: {}) 合法
        if not isinstance(value, dict):
            # 某些机制可能是列表 (如 armor_effects: - SPEED:1)
            return

        # 方块机制单独详细校验
        if name in BLOCK_MECHANICS:
            self._validate_block_mechanic(name, value, path)
        elif name == "furniture":
            self._validate_furniture(value, path)
        elif name == "backpack_cosmetic":
            self._validate_backpack_cosmetic(value, path)

        # 子字段合法性 (docs 记载的字段集合)
        valid_subs = MECHANIC_SUBFIELDS.get(name)
        if valid_subs is not None and len(valid_subs) > 0:
            for sub in value.keys():
                if sub not in valid_subs:
                    self.add_error(
                        f"{path}.{sub}", "unknown_field",
                        f"机制 '{name}' 的未知子字段 '{sub}' (未在 Item Abilities docs 中记载)",
                        severity="warning",
                    )

        # aura.type 枚举
        if name == "aura" and "type" in value:
            self._check_enum(value["type"], VALID_AURA_TYPES, f"{path}.type", "aura type")

    # ------------------------------------------------------------------
    # 方块机制校验 (noteblock / stringblock / chorusblock / shaped_block)
    # ------------------------------------------------------------------
    def _validate_block_mechanic(self, name: str, value: Any, path: str):
        if not isinstance(value, dict):
            return

        # custom_variation: docs 从 1 开始 (NoteBlock.md 等)
        if "custom_variation" in value:
            cv = value["custom_variation"]
            if isinstance(cv, int) and cv < 1:
                self.add_error(
                    f"{path}.custom_variation", "out_of_range",
                    f"custom_variation 应从 1 开始 (docs 示例均 >=1), 实际: {cv}",
                    severity="warning",
                )

        # best_tools 枚举
        if "best_tools" in value:
            bt = value["best_tools"]
            if isinstance(bt, list):
                for t in bt:
                    self._check_enum(t, VALID_TOOL_TYPES, f"{path}.best_tools", "best_tools")
            elif isinstance(bt, str):
                self._check_enum(bt, VALID_TOOL_TYPES, f"{path}.best_tools", "best_tools")

        # shaped_block.type 枚举
        if name == "shaped_block" and "type" in value:
            self._check_enum(value["type"], VALID_SHAPED_BLOCK_TYPES,
                             f"{path}.type", "shaped_block type")

        # storage.type 枚举
        if "storage" in value and isinstance(value["storage"], dict):
            if "type" in value["storage"]:
                self._check_enum(value["storage"]["type"], VALID_STORAGE_TYPES,
                                 f"{path}.storage.type", "storage type")

    # ------------------------------------------------------------------
    # 家具校验 (Furniture/Overview.md / Display Entities.md)
    # ------------------------------------------------------------------
    def _validate_furniture(self, value: Any, path: str):
        if not isinstance(value, dict):
            return
        if "type" in value:
            self._check_enum(value["type"], VALID_FURNITURE_TYPES,
                             f"{path}.type", "furniture type")
        # light: docs "must be between 1 and 15"
        if "light" in value:
            self._check_int_range(
                value["light"], FURNITURE_LIGHT_MIN, FURNITURE_LIGHT_MAX,
                f"{path}.light", "furniture light",
            )
        # storage.type
        if "storage" in value and isinstance(value["storage"], dict):
            if "type" in value["storage"]:
                self._check_enum(value["storage"]["type"], VALID_STORAGE_TYPES,
                                 f"{path}.storage.type", "storage type")

    # ------------------------------------------------------------------
    # backpack_cosmetic 校验 (Backpack Cosmetic.md)
    # ------------------------------------------------------------------
    def _validate_backpack_cosmetic(self, value: Any, path: str):
        if not isinstance(value, dict):
            return
        if "slot" in value:
            self._check_enum(value["slot"], VALID_COSMETIC_SLOTS,
                             f"{path}.slot", "backpack_cosmetic slot")

    # ------------------------------------------------------------------
    # ItemFlags 校验
    # ------------------------------------------------------------------
    def _validate_item_flags(self, value: Any, path: str):
        if isinstance(value, list):
            for f in value:
                if isinstance(f, str) and f not in VALID_ITEM_FLAGS:
                    self.add_error(
                        path, "invalid_enum",
                        f"未知 ItemFlags: '{f}'",
                        severity="warning",
                        suggestion=f"合法值: {sorted(VALID_ITEM_FLAGS)}",
                    )

    # ------------------------------------------------------------------
    # color / 可染色材质校验 (Dyeable Items.md)
    # ------------------------------------------------------------------
    def _validate_color(self, item: dict, path: str):
        # 仅当物品配置了 color 字段时, 检查 material 是否为可染色材质
        material = item.get("material")
        if isinstance(material, str) and material.startswith("LEATHER_"):
            if material not in VALID_DYEABLE_MATERIALS:
                self.add_error(
                    f"{path.replace('.color', '')}.material", "invalid_dyeable_material",
                    f"染色系统仅支持 POTION / LEATHER_HORSE_ARMOR (Dyeable Items.md), "
                    f"当前 material: '{material}'",
                    severity="warning",
                    suggestion="皮革护甲染色需较新版本 Oraxen 验证, 或改用 LEATHER_HORSE_ARMOR",
                )


# =============================================================================
# 配方文件校验 (独立, 因 Oraxen recipes/ 目录下文件结构不同)
# =============================================================================

def validate_recipe_file(filepath: str) -> List[Dict]:
    """校验配方文件 (Recipes.md: 目前仅支持 shaped)

    支持 .md (提取 ```yaml 块) 和 .yml/.yaml (直接解析)。
    """
    errors: List[ValidationError] = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        errors.append(ValidationError("(file)", "read_error", f"无法读取文件: {e}"))
        return [e.to_dict() for e in errors]

    def _check_data(data: Any, label: str):
        if not isinstance(data, dict):
            return
        for recipe_id, recipe_value in data.items():
            if not isinstance(recipe_value, dict):
                continue
            rtype = recipe_value.get("type")
            if rtype is not None and rtype not in VALID_RECIPE_TYPES:
                errors.append(ValidationError(
                    f"{label}:{recipe_id}.type", "unsupported_recipe_type",
                    f"docs (Recipes.md) 声明目前仅支持 shaped 配方, 当前: '{rtype}'",
                    severity="warning",
                    suggestion="该类型需较新版本 Oraxen 支持, 使用前请验证",
                ))

    if filepath.lower().endswith(".md"):
        pattern = re.compile(r"```ya?ml\n(.*?)```", re.DOTALL)
        for idx, block in enumerate(pattern.findall(content), 1):
            try:
                _check_data(yaml.safe_load(block), f"{os.path.basename(filepath)}#block{idx}")
            except yaml.YAMLError:
                continue
    else:
        try:
            _check_data(yaml.safe_load(content), filepath)
        except yaml.YAMLError as e:
            errors.append(ValidationError("(yaml)", "yaml_parse_error", f"YAML 解析错误: {e}"))

    return [e.to_dict() for e in errors]


# =============================================================================
# 报告输出
# =============================================================================

def print_text_report(errors: List[Dict], filepath: str):
    print(f"\n{'=' * 70}")
    print(f"文件: {filepath}")
    print(f"{'=' * 70}")
    if not errors:
        print("  校验通过, 无错误")
        return
    err_count = sum(1 for e in errors if e.get("severity") == "error")
    warn_count = sum(1 for e in errors if e.get("severity") == "warning")
    for e in errors:
        sev = e.get("severity", "error")
        prefix = "错误" if sev == "error" else "警告"
        print(f"  [{prefix}] {e.get('path')} ({e.get('type')}): {e.get('message')}")
        if e.get("suggestion"):
            print(f"          建议: {e.get('suggestion')}")
    print(f"\n  共 {err_count} 个错误, {warn_count} 个警告")


# =============================================================================
# 主入口
# =============================================================================

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Oraxen YAML 配置文件校验器 v" + VERSION,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python oraxen_validator.py config.yml
  python oraxen_validator.py config.yml --json
  python oraxen_validator.py *.yml --json > errors.json
  python oraxen_validator.py recipes/shaped.yml --recipe
        """
    )
    parser.add_argument("files", nargs="+", help="要校验的 YAML 文件路径")
    parser.add_argument("--version", default=DEFAULT_MINECRAFT_VERSION,
                        help=f"Minecraft 版本 (默认: {DEFAULT_MINECRAFT_VERSION})")
    parser.add_argument("--json", action="store_true", help="输出 JSON 格式")
    parser.add_argument("--text", action="store_true", help="输出纯文本格式 (默认)")
    parser.add_argument("--recipe", action="store_true",
                        help="按配方文件校验 (检查 recipe type 是否为 docs 支持的 shaped)")
    parser.add_argument("--output", "-o", help="输出到文件 (默认 stdout)")

    args = parser.parse_args()

    if not args.json and not args.text:
        args.text = True

    validator = OraxenValidator(mc_version=args.version)
    all_results: Dict[str, List[Dict]] = {}
    has_errors = False

    for filepath in args.files:
        if not os.path.exists(filepath):
            print(f"错误: 文件不存在 '{filepath}'", file=sys.stderr)
            has_errors = True
            continue
        if args.recipe:
            errors = validate_recipe_file(filepath)
        else:
            errors = validator.validate_file(filepath)
        all_results[filepath] = errors
        # 仅 error 级别计入 has_errors (warning 不影响退出码)
        if any(e.get("severity") == "error" for e in errors):
            has_errors = True

    output_lines: List[str] = []
    if args.text:
        for filepath, errors in all_results.items():
            import io
            buf = io.StringIO()
            old_stdout = sys.stdout
            sys.stdout = buf
            print_text_report(errors, filepath)
            sys.stdout = old_stdout
            output_lines.append(buf.getvalue())
    if args.json:
        output_lines.append(json.dumps(all_results, ensure_ascii=False, indent=2))

    output = "\n".join(output_lines)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
    else:
        try:
            print(output, end="")
        except UnicodeEncodeError:
            print(output.encode("ascii", "replace").decode("ascii"), end="")

    sys.exit(1 if has_errors else 0)


if __name__ == "__main__":
    main()
