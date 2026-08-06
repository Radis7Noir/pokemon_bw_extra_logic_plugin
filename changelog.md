# Pokémon BW AP Extra Logic Plugin

Changelog

## v9
* Fixed Landorus appearing without Tornadus and Thundurus in the party
* Imported the updated field move patches from the QoL plugin

## v8
* Fixed Tornadus/Thundurus/Landorus cutscenes crashing the game when there are too many dark areas
  * As a consequence, the roamer is now a static encounter until a better fix is made
* Fixed the logic of the three locations near the entrance of Moor of Icirrus that can't be reached during winter without Surf
* Added `randomize_starting_town` as an option
  * Swaps the player's house with a house from another town
  * Valid choices are: "Nuvema Town", "Accumula Town", "Striaton City", "Nacrene City", "Castelia City", "Nimbasa City", "Driftveil City", "Mistralton City", "Icirrus City", "Opelucid City", "Lacunosa Town", "Undella Town"
  * `starting_town_blacklist` prevents the listed towns to be chosen as starting town if `randomize_starting_town` is activated
  * If Cynthia is selected as goal, "Lacunosa Town" and "Undella Town" cannot be selected as the starting town
  * If all towns are blacklisted or if there is no possible choice, the option will fall back to Nuvema Town
  * When Mistralton City is selected as the starting town, the Move reminder house is relocated in Nuvema Town (the logic for move evolution is updated accordingly)
  * When the starting town is not Nuvema Town, Mom will not give her first item. An added clerk NPC in Nuvema Town will hand it instead
* Adjusted multiple cutscenes to prevent sequence breaks with a random starting town

## v7
* Udated multiple patches to ensure compatibility with the QoL plugin
* Fixed logic related to dark_areas in multiple areas
## v6
* Fixed the logic in Abyssal Ruins as the Strength purple block can be pushed regardless of the badge requirement
* Fixed the Static Musharna logic with `add_rock_smash_musharna` not taking the `Consider static pokémon` modifier into account
* Dwebble from breakable rocks now take the `Consider static pokémon` modifier into account
* Added `dark_areas` as a YAML option
  * Turns all the listed areas dark and allows the use of Flash
  * `Require flash` makes all the darken areas logically require Flash
  * `_All` includes all areas
  * `_Random` has a 50% chance to include each area that is not already included
  * `[]` removes all darken areas
  * The full list of valid areas is available on the readme
  * Removing the option entirely will keep the default dark areas

## v5
* Fixed the logic of the plane connection incorrectly checking for Cut and the Pass instead of just the Pass

## v4
* Fixed the missing boulder change in Dragonspiral Tower 2F with `move_strength_boulders`
* Rewrote some parts of the plugin files for v0.3.37 of the main APworld (@Slimey)
* The plasma grunt in Pinwheel Forest East now disappears after defeating Team Plasma without reloading the map
* Added `add_pass`
  * Adds a plane connection between Mistralton City and Village Bridge that requires the (Maglev) Pass

## v3
* Added more missing connections between regions to make full use of the plugin options
* Added `move_strength_boulders`
  * Moves the north boulder on Route 13 to create a new path to reach the Giant Chasm
  * Moves the south boulder in the Dreamyard to create a new path to reach the Basement
  * Moves the boulder in Dragonspiral Tower 2F and adds another one to make Strength required to reach the next floors
* Added `move_strength_boulders_vi_road`
  * Moves the boulder on Victory Road 4F Left Cavern to make Strength required to reach Pokémon League
  * This option can only be enabled if `move_strength_boulders` is set to true
* Added `extra_cut_trees`
  * Puts the Loot Sack roadblock NPCs to the west side of Pinwheel Forest and adds cut trees in the middle path, making it possible to leave the Forest with Cut and the Dragon Skull
  * A Plasma grunt NPC will block the East path until Team Plasma leaves the Forest
  * A Petilil NPC will appear near the north exit after defeating Team Plasma to teleport the player back to the south entrance to avoid softlocks
* Added `extra_cut_trees_kyurem`
  * Adds cut trees just before the small pond in the Giant Chasm crater
  * This option can only be enabled if `extra_cut_trees` is set to true
* Added `add_rock_smash_musharna`
  * Adds breakable rocks on the northen side of the Dreamyard Basement
  * This option can only be enabled if `add_rock_smash` is set to true

## v2
* Added a missing connection between Challenger's Cave and Route 9
* Added a missing connection between Wellspring Cave and Route 3

## v1
* Added `add_rock_smash` option
  * Makes TM94 Rock Smash a field move
  * Blocks the path between Undella Town and Route 13 with breakable rocks
  * Creates a connection between Wellspring Cave 1F and Challenger's Cave B1F that requires Rock Smash
  * `Wellspring Cave - 1F hidden item #1`, `Wellspring Cave - 1F north east item` and `Challenger's Cave - B1F south item` logically require Rock Smash in addition to their previous access rule
  * Breakable rocks trigger an encounter against a lvl 15 Dwebble
* Added `add_ss_ticket` option
  * Adds a boat connection between P2 Laboratory and Liberty Garden that requires the Liberty Pass
  * Adds a second ferry that sails between Liberty Garden and Undella Town, requiring the Liberty Pass and the S.S. Ticket
    * The Victini event must be cleared to use the black ferry from Liberty Garden
* Added `hm_with_badges` option
  * Makes HM01 Cut require the Trio Badge
  * Makes HM03 Surf require the Quake Badge
  * Makes HM04 Strength require the Bolt Badge
  * Makes HM05 Waterfall require the Freeze Badge
  * Makes HM06 Dive require the Legend Badge
  * If `add_rock_smash` is on, makes TM94 Rock Smash require the Basic Badge
* Imported some of the QoL Plugin patches to ensure compatibility between the two plugins and prevent sequence breaks