
```yml
miner_sandwich:
  itemname: <gradient:#F69D84:#FAD98D>Miner's Sandwich
  material: PAPER
  Components:
    food:
      nutrition: 8
      saturation: 12.8
      can_always_eat: true
    consumable:
      consume_seconds: 5
      animation: EAT
      sound: entity.generic.eat
      has_consume_particles: true
      on_consume_effects:
        - type: apply_effects
          effects:
            minecraft:haste:
              duration: 3600
              amplifier: 0
              ambient: true
              show_particles: true
              show_icon: true
          probability: 1.0
  Pack:
    generate_model: true
    parent_model: item/generated
    textures:
      - default/sandwich.png
      ```
