# Pokémon BW Extra Logic APworld Plugin
An optional APworld that adds new logic to the main BW APworld

This plugin is currently only comptabile with v0.3.35+ of the main BW APworld.

## Important Note
- The host MUST have the plugin installed before generating to ensure the logic of the main APworld is properly updated

## Features
- Adds some of the QoL plugin patches to ensure compatibility between the two plugins and prevent some sequence breaks
- `add_rock_smash` makes Rock Smash a field move and
  * Blocks the path between Undella Town and Route 13 with breakable rocks
  * Creates a connection between Wellspring Cave 1F and Challenger's Cave B1F
  * Makes `Wellspring Cave - 1F hidden item #1`, `Wellspring Cave - 1F north east item` and `Challenger's Cave - B1F south item` logically require Rock Smash
  * Adds a Dwebble encounter when breaking rocks
- `add_ss_ticket` puts the S.S. Ticket in the pool and
  * Adds a boat connection between P2 Laboratory and Liberty Garden that requires the Liberty Pass
  * Adds a second ferry that sails between Liberty Garden and Undella Town, requiring the Liberty Pass and the S.S. Ticket
    * The Victini event must be cleared to use the black ferry from Liberty Garden
- `hm_with_badges` makes
  * HM01 Cut require the Trio Badge
  * HM03 Surf require the Quake Badge
  * HM04 Strength require the Bolt Badge
  * HM05 Waterfall require the Freeze Badge
  * HM06 Dive require the Legend Badge
  * TM94 Rock Smash require the Basic Badge if `add_rock_smash` is on
- `move_strength_boulders` moves
  * The north boulder on Route 13 to create a new path to reach the Giant Chasm
  * The south boulder in the Dreamyard to create a new path to reach the Basement
  * The boulder in Dragonspiral Tower 2F and adds another one to make Strength required to reach the next floors
- `move_strength_boulders_vi_road`
  * Moves the boulder on Victory Road 4F Left Cavern to make Strength required to reach Pokémon League
  * Requires `move_strength_boulders` to be set to true
-`extra_cut_trees`
  * Puts the Loot Sack roadblock NPCs to the west side of Pinwheel Forest and adds cut trees in the middle path, making it possible to leave the Forest with Cut and the Dragon Skull
  * A Plasma grunt NPC will block the East path until Team Plasma leaves the Forest
  * A Petilil NPC will appear near the north exit after defeating Team Plasma to teleport the player back to the south entrance to avoid softlocks
- `extra_cut_trees_kyurem`
  * Adds cut trees just before the small pond in the Giant Chasm crater
  * This option can only be enabled if `extra_cut_trees` is set to true
- `add_rock_smash_musharna`
  * Adds breakable rocks on the northen side of the Dreamyard Basement
  * This option can only be enabled if `add_rock_smash` is set to true

## Instructions
- Download the latest release of the plugin APworld
- Place it in the `custom_worlds` folder of the Archipelago folder
- Restart the AP launcher
- Add the following options to the Black and White YAML under `plugin_options`:
```
  plugin_options:
    extra_logic:
      add_rock_smash: true
      add_ss_ticket: true
      hm_with_badges: true
```
- Set the options to true or false as seen fit and generate the seed as usual
  - When running the .apwhite/.apblack patch, the produced .nds file should include the features that have been activated.
