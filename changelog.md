# Pokémon BW AP Extra Logic Plugin

Changelog

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