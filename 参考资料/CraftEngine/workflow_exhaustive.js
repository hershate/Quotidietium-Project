export const meta = {
  name: 'exhaustive-craftengine-templates',
  description: 'Exhaustively enumerate ALL CraftEngine config types from wiki, create one template per type',
  phases: [
    { title: 'Items', detail: 'Create item behavior and data templates' },
    { title: 'Blocks', detail: 'Create all block behavior templates' },
    { title: 'BlockSetup', detail: 'Create block settings/states templates' },
    { title: 'Furniture', detail: 'Create furniture behavior templates' },
    { title: 'Models', detail: 'Create item model type templates' },
    { title: 'Other', detail: 'Create remaining reference templates' },
    { title: 'Index', detail: 'Create README' },
  ],
}

const BASE = 'f:/Github/repo/Quotidietium-Project/参考资料/CraftEngine'
const WIKI = BASE + '/CraftEngine Wiki'
const OUT = BASE + '/CraftEngine Template'

phase('Items')

// Item behaviors - 11 files
await parallel([
  function() { return agent('Read source at ' + WIKI + '/configuration/item/behaviors/block_item.md and write template to ' + OUT + '/物品/行为/block_item.yml. Include items root, behavior type block_item with block option. Follow Oraxen style with YAML comments. Use custom namespace.', { label: 'block_item', phase: 'Items' }) },
  function() { return agent('Read source at ' + WIKI + '/configuration/item/behaviors/ceiling_block_item.md and write template to ' + OUT + '/物品/行为/ceiling_block_item.yml. Include all documented options.', { label: 'ceiling_block_item', phase: 'Items' }) },
  function() { return agent('Read source at ' + WIKI + '/configuration/item/behaviors/wall_block_item.md and write template to ' + OUT + '/物品/行为/wall_block_item.yml.', { label: 'wall_block_item', phase: 'Items' }) },
  function() { return agent('Read source at ' + WIKI + '/configuration/item/behaviors/ground_block_item.md and write template to ' + OUT + '/物品/行为/ground_block_item.yml.', { label: 'ground_block_item', phase: 'Items' }) },
  function() { return agent('Read source at ' + WIKI + '/configuration/item/behaviors/double_high_block_item.md and write template to ' + OUT + '/物品/行为/double_high_block_item.yml.', { label: 'double_high_block_item', phase: 'Items' }) },
  function() { return agent('Read source at ' + WIKI + '/configuration/item/behaviors/multi_high_block_item.md and write template to ' + OUT + '/物品/行为/multi_high_block_item.yml.', { label: 'multi_high_block_item', phase: 'Items' }) },
  function() { return agent('Read source at ' + WIKI + '/configuration/item/behaviors/liquid_collision_block_item.md and write template to ' + OUT + '/物品/行为/liquid_collision_block_item.yml.', { label: 'liquid_collision_block_item', phase: 'Items' }) },
  function() { return agent('Read source at ' + WIKI + '/configuration/item/behaviors/liquid_collision_furniture_item.md and write template to ' + OUT + '/物品/行为/liquid_collision_furniture_item.yml.', { label: 'liquid_collision_furniture', phase: 'Items' }) },
  function() { return agent('Read source at ' + WIKI + '/configuration/item/behaviors/furniture_item.md and write template to ' + OUT + '/物品/行为/furniture_item.yml.', { label: 'furniture_item', phase: 'Items' }) },
  function() { return agent('Read source at ' + WIKI + '/configuration/item/behaviors/compostable_item.md and write template to ' + OUT + '/物品/行为/compostable_item.yml.', { label: 'compostable_item', phase: 'Items' }) },
  function() { return agent('Read source at ' + WIKI + '/configuration/item/behaviors/range_mining_item.md and write template to ' + OUT + '/物品/行为/range_mining_item.yml.', { label: 'range_mining_item', phase: 'Items' }) },
])

// Item data components + settings - 2 comprehensive files
await parallel([
  function() { return agent('Create comprehensive data components reference at ' + OUT + '/物品/数据组件/全部数据组件.yml. Read ' + WIKI + '/configuration/item/data.md. List EVERY documented component: item_name, custom_name, lore, overwritable_lore, insert_lore, remove_lore, overwritable_item_name, unbreakable, enchantment, dyed_color, custom_model_data, hide_tooltip, block_state, attribute_modifiers, food, max_damage, jukebox_playable, item_model, components, damage, trim, equippable, charged_projectile, debug_stick, external. Each with example. Use custom namespace. Oraxen style.', { label: 'data-components', phase: 'Items' }) },
  function() { return agent('Create comprehensive settings reference at ' + OUT + '/物品/设置/全部设置项.yml. Read ' + WIKI + '/configuration/item/settings.md. List EVERY setting: fuel_time, tags, equipment (with asset_id, client_bound_model, slot, camera_overlay, dispensable, damage_on_hurt, swappable, equip_on_interact), repairable, anvil_repair_item, renameable, allowed_projectiles, projectile (with display, sounds, ignore_infinity_enchantment, pickupable, remove_on_hit, gravity, velocity, damage, pierce_level), dyeable, enchantable, compost_probability, respect_repairable_component, dye_color, firework_color. Each with example. Use custom namespace. Oraxen style.', { label: 'settings', phase: 'Items' }) },
])

phase('Blocks')

// Block behaviors - 57 files in parallel
var bb = ['crop_block', 'stem_block', 'attached_stem_block', 'bush_block', 'sapling_block', 'vertical_crop_block', 'change_over_time_block', 'spreading_block', 'surface_spreading_block', 'decay_block', 'grass_block', 'leaves_block', 'door_block', 'trapdoor_block', 'fence_block', 'fence_gate_block', 'button_block', 'pressure_plate_block', 'stairs_block', 'slab_block', 'double_high_block', 'multi_high_block', 'falling_block', 'concrete_powder_block', 'bouncing_block', 'lamp_block', 'toggleable_lamp_block', 'chime_block', 'simple_storage_block', 'drawer_block', 'drop_experience_block', 'simple_particle_block', 'wall_torch_particle_block', 'tint_source_block', 'display_item_block', 'item_frame_block', 'seat_block', 'sofa_block', 'stackable_block', 'directional_attached_block', 'face_attached_horizontal_directional_block', 'hangable_block', 'hanging_block', 'liquid_flowable_block', 'near_liquid_block', 'on_liquid_block', 'snowy_block', 'strippable_block', 'sturdy_base_block', 'budding_block']

var blockTasks = []
for (var i = 0; i < bb.length; i++) {
  let name = bb[i]
  blockTasks.push(function() {
    return agent('Read source at ' + WIKI + '/configuration/block/behaviors/' + name + '.md if it exists. Write template to ' + OUT + '/方块/行为/' + name + '.yml. Include blocks root key, all documented config options, property requirements, and a complete example. Use custom namespace. Oraxen style with comments.', { label: name, phase: 'Blocks' })
  })
}
await parallel(blockTasks)

phase('BlockSetup')
await parallel([
  function() { return agent('Create block settings reference at ' + OUT + '/方块/设置/全部设置项.yml. Read ' + WIKI + '/configuration/block/settings.md. Cover: item, hardness, resistance, is_suffocating, is_redstone_conductor, instrument, map_color, luminance, sounds (break/step/place/hit/fall), correct_tools, tags, destroy_time, explosion_resistance, slipperiness, speed_factor, velocity_factor, jump_factor, burnable, requires_correct_tool, fluid_state, push_state, piston_behavior, lava_flammable, lava_occlusion, occlusion, no_collision, collision_box, has_collision, replaceable, replaceable_blocks, block_state_mappings. Each with example. Oraxen style.', { label: 'block-settings', phase: 'BlockSetup' }) },
  function() { return agent('Create states and properties reference at ' + OUT + '/方块/属性状态/属性与状态.yml. Read ' + WIKI + '/configuration/block/states.md and ' + WIKI + '/configuration/block/states/properties.md and ' + WIKI + '/configuration/block/states/entity_renderer.md. Cover: single-state (state, auto_state groups table, model config with path/generation/textures/texture/models list/transparent/rotation/uvlock), multi-state (states with properties/appearances/variants), property types (boolean/int/string/direction/horizontal_direction/axis/single_block_half/double_block_half/hinge/slab_type/stairs_shape/sofa_shape/anchor_type), hardcoded names (axis/waterlogged/facing/facing_clockwise/rotation), entity_renderer (item_display/text_display/item/armor_stand), variant matching rules. Oraxen style.', { label: 'block-states', phase: 'BlockSetup' }) },
])

phase('Furniture')
await parallel([
  function() { return agent('Create furniture behavior display_item_furniture at ' + OUT + '/家具/行为/display_item_furniture.yml. Read ' + WIKI + '/configuration/furniture/behaviors/display_item_furniture.md.', { label: 'display_item_furniture', phase: 'Furniture' }) },
  function() { return agent('Create furniture behavior glowing_furniture at ' + OUT + '/家具/行为/glowing_furniture.yml. Read ' + WIKI + '/configuration/furniture/behaviors/glowing_furniture.md.', { label: 'glowing_furniture', phase: 'Furniture' }) },
  function() { return agent('Create furniture behavior simple_storage_furniture at ' + OUT + '/家具/行为/simple_storage_furniture.yml. Read ' + WIKI + '/configuration/furniture/behaviors/simple_storage_furniture.md.', { label: 'simple_storage_furniture', phase: 'Furniture' }) },
  function() { return agent('Create furniture settings reference at ' + OUT + '/家具/设置/设置.yml. Read ' + WIKI + '/configuration/furniture/settings.md.', { label: 'furniture-settings', phase: 'Furniture' }) },
  function() { return agent('Create furniture variants reference at ' + OUT + '/家具/变体/变体配置.yml. Read ' + WIKI + '/configuration/furniture/variants.md. Cover: ground/wall/ceiling, elements, hitboxes, seats, entity_culling, display transform, billboard, glow_color, shadow.', { label: 'furniture-variants', phase: 'Furniture' }) },
])

phase('Models')
await parallel([
  function() { return agent('Create item model minecraft:model template at ' + OUT + '/物品/模型类型/minecraft_model.yml. Read ' + WIKI + '/configuration/item/models/model.md. Cover: type minecraft:model, path, generation (parent, textures), transformation (scale, translation, right_rotation, left_rotation), tint types (minecraft:constant, custom_model_data, dye, firework, grass, map_color, potion, team). Oraxen style.', { label: 'model-type', phase: 'Models' }) },
  function() { return agent('Create item model minecraft:condition template at ' + OUT + '/物品/模型类型/minecraft_condition.yml. Read ' + WIKI + '/configuration/item/models/condition.md. Cover: type, property (broken/carried/damaged/extended_view/fishing_rod_cast/selected/using_item/view_entity/has_selected_item/component/has_component/keybind_down/custom_model_data), on_false, on_true, transformation. Oraxen style.', { label: 'condition', phase: 'Models' }) },
  function() { return agent('Create item model minecraft:range_dispatch template at ' + OUT + '/物品/模型类型/minecraft_range_dispatch.yml. Read ' + WIKI + '/configuration/item/models/range_dispatch.md. Cover: type, property (crossbow_pull/bundle_fullness/cooldown/compass/count/damage/time/use_cycle/use_duration/custom_model_data), entries with threshold/model, fallback, transformation. Oraxen style.', { label: 'range-dispatch', phase: 'Models' }) },
  function() { return agent('Create item model minecraft:composite template at ' + OUT + '/物品/模型类型/minecraft_composite.yml. Read ' + WIKI + '/configuration/item/models/composite.md. Cover: type composite, models list, transformation. Oraxen style.', { label: 'composite', phase: 'Models' }) },
  function() { return agent('Create item model minecraft:select template at ' + OUT + '/物品/模型类型/minecraft_select.yml. Read ' + WIKI + '/configuration/item/models/select.md. Cover: type, property (charge_type/context_dimension/context_entity_type/display_context/main_hand/trim_material/block_state/component/custom_model_data/local_time), cases with when/model, fallback, transformation. Oraxen style.', { label: 'select', phase: 'Models' }) },
  function() { return agent('Create item model minecraft:special template at ' + OUT + '/物品/模型类型/minecraft_special.yml. Read ' + WIKI + '/configuration/item/models/special.md. Cover: type special, renderer types (trident/conduit/shield/decorated_pot/hanging_sign/standing_sign/head/player_head/chest/shulker_box/banner/bell/book/copper_golem_statue/end_cube). Oraxen style.', { label: 'special', phase: 'Models' }) },
  function() { return agent('Create simplified item model reference at ' + OUT + '/物品/模型类型/简化模型.yml. Read ' + WIKI + '/configuration/item/models.md. Cover: simplified patterns - texture (2D icon), textures (handheld), fishing rod, elytra, bow, crossbow, shield, models list, model path shortcut, legacy_model with overrides. Oraxen style.', { label: 'simplified-models', phase: 'Models' }) },
])

phase('Other')
await parallel([
  function() { return agent('Create number format reference at ' + OUT + '/其他配置/数字格式.yml. Read ' + WIKI + '/reference/number_format.md. Cover ALL: constant, uniform, expression, binomial, gaussian, skew_normal, log_normal, triangle, beta, weighted, exponential. Include shorthand forms. Oraxen style.', { label: 'number-format', phase: 'Other' }) },
  function() { return agent('Create text format reference at ' + OUT + '/其他配置/文本格式.yml. Read ' + WIKI + '/reference/text_format.md. Cover MiniMessage basics and ALL CraftEngine tags: shift, papi, viewer_papi, rel_papi, image, i18n, l10n, expr, arg, viewer_arg, global, bubble, nameplate, background. Include caution notes. Oraxen style.', { label: 'text-format', phase: 'Other' }) },
  function() { return agent('Create chain arguments reference at ' + OUT + '/其他配置/链式参数.yml. Read ' + WIKI + '/reference/text_format/chain_arguments.md. Cover all: player, block, world, entity, position, item, furniture with their properties tables. Oraxen style.', { label: 'chain-args', phase: 'Other' }) },
  function() { return agent('Create file conflict handler template at ' + OUT + '/其他配置/文件冲突配置.yml. Read ' + WIKI + '/reference/file_conflict.md. Cover match rules: all_of, any_of, inverted, filename, exact, parent_path_prefix, parent_path_suffix, contains, pattern. Cover resolutions: merge_json, retain_matching, conditional, merge_pack_mcmeta, merge_atlas, merge_font. Oraxen style.', { label: 'file-conflict', phase: 'Other' }) },
  function() { return agent('Create font config at ' + OUT + '/其他配置/字体配置.yml. Read ' + WIKI + '/configuration/font.md. Cover TTF, bitmap, unihex. Oraxen style.', { label: 'font', phase: 'Other' }) },
  function() { return agent('Create item updater template at ' + OUT + '/其他配置/物品更新器.yml. Read ' + WIKI + '/configuration/item/updater.md. Oraxen style.', { label: 'updater', phase: 'Other' }) },
])

phase('Index')
await agent('Create exhaustive README at ' + OUT + '/README.md. List ALL template files organized by directory. Document every CraftEngine root config key, behavior type, model type, settings key, data component. Reference the local wiki at ../CraftEngine%20Wiki/ for each. Use Chinese.', { label: 'readme', phase: 'Index' })

return { done: true }
