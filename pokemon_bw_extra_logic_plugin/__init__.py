# Do not change anything about these imports unless you know what you do
import pkgutil
from typing import TYPE_CHECKING
from zipfile import ZipFile
if __name__ == '__main__':
    from data.api import PluginProtocol
else:
    from .data.api import PluginProtocol
try:
    from BaseClasses import ItemClassification, CollectionState
    if TYPE_CHECKING:
        from worlds.pokemon_bw.ndspy.rom import NintendoDSRom
        from worlds.pokemon_bw.rom import PokemonBWPatch
        from worlds.pokemon_bw.items import PokemonBWItem
        from worlds.pokemon_bw.locations import PokemonBWLocation
        from worlds.pokemon_bw.data import SpeciesData, ExtendedRule
        from worlds.pokemon_bw import PokemonBWWorld
    from worlds.pokemon_bw.plugins._dev import DEV
except ImportError:
    DEV = False


# This has to exactly be named "Plugin" and should inherit from "PluginProtocol"
class Plugin(PluginProtocol):

    name = "Pokemon BW Extra Logic Plugin"
    domain = "extra_logic"
    version = "1.2.0"
    author = "RadisNoir"


    # This is called during the patching process, after the main apworld did all its standard modifications to the rom.
    def patch(self):
        if DEV: return

        if not any(p.name == "Pokemon BW QoL Plugin" for p in self.all_plugins):
            for i in [12, 32, 308, 310, 642, 648, 652, 706, 866]:
                loaded_file = pkgutil.get_data(__name__, f"files/a057/{i:03d}")
                narc_file = self.get_from_narc("a/0/5/7", i)
                self.otpp_patch_array(narc_file, loaded_file)
            for i in [21, 67, 280, 353, 356, 385]:
                loaded_file = pkgutil.get_data(__name__, f"files/a003/{i:03d}")
                narc_file = self.get_from_narc("a/0/0/3", i)
                self.otpp_patch_array(narc_file, loaded_file)
            for i in [16, 62, 154, 155, 321]:
                loaded_file = pkgutil.get_data(__name__, f"files/a125/{i:03d}")
                narc_file = self.get_from_narc("a/1/2/5", i)
                self.otpp_patch_array(narc_file, loaded_file)

            if not self.get_option("hm_with_badges", False):
                loaded_file = pkgutil.get_data(__name__, f"files/a057/867_vanilla")
                narc_file = self.get_from_narc("a/0/5/7", 867)
                self.otpp_patch_array(narc_file, loaded_file)

            if self.get_option("hm_with_badges", False):
                loaded_file = pkgutil.get_data(__name__, f"files/a057/867_badgevanilla")
                narc_file = self.get_from_narc("a/0/5/7", 867)
                self.otpp_patch_array(narc_file, loaded_file)

        if self.get_option("add_rock_smash", False):
            for i in [70, 356, 363]:
                loaded_file = pkgutil.get_data(__name__, f"files/a008/add_rock_smash/{i:03d}")
                narc_file = self.get_from_narc("a/0/0/8", i)
                self.otpp_patch_array(narc_file, loaded_file)
            for i in [324, 348, 353, 370]:
                loaded_file = pkgutil.get_data(__name__, f"files/a125/add_rock_smash/{i:03d}")
                narc_file = self.get_from_narc("a/1/2/5", i)
                self.otpp_patch_array(narc_file, loaded_file)

        if self.get_option("add_ss_ticket", False):
            for i in [243, 246, 451]:
                loaded_file = pkgutil.get_data(__name__, f"files/a003/add_ss_ticket/{i:03d}")
                narc_file = self.get_from_narc("a/0/0/3", i)
                self.otpp_patch_array(narc_file, loaded_file)
            for i in [470, 476, 824]:
                loaded_file = pkgutil.get_data(__name__, f"files/a057/add_ss_ticket/{i:03d}")
                narc_file = self.get_from_narc("a/0/5/7", i)
                self.otpp_patch_array(narc_file, loaded_file)
            for i in [235, 238, 412]:
                loaded_file = pkgutil.get_data(__name__, f"files/a125/add_ss_ticket/{i:03d}")
                narc_file = self.get_from_narc("a/1/2/5", i)
                self.otpp_patch_array(narc_file, loaded_file)


    # This is called after generating all regions, regions connections, locations, and events
    def create_regions(self, catchable_species_data: dict[str, "SpeciesData"]):
        from worlds.pokemon_bw.items import PokemonBWItem
        from worlds.pokemon_bw.locations import PokemonBWLocation
        from worlds.pokemon_bw.data.items import tm_hm, classification
        from worlds.pokemon_bw.data.pokemon.movesets import table as moveset_table
        from worlds.pokemon_bw.data.locations.rules import can_use_surf, can_use_waterfall, can_use_dive, can_use_cut, can_use_strength, can_use_surf_or_strength, dark_cave, challengers_cave
        if DEV: return

        # Missing Connections
        self.world.regions["Route 3"].connect(
            self.world.regions["Striaton City"],
            "Route 3 to Striaton City",
            lambda state: state.has("Parcel", self.world.player)
        )
        self.world.regions["Nacrene City"].connect(
            self.world.regions["Route 3"],
            "Nacrene City to Route 3",
            lambda state: True
        )
        self.world.regions["Pinwheel Forest Outside"].connect(
            self.world.regions["Nacrene City"],
            "Pinwheel Forest Outside to Nacrene City",
            lambda state: True
        )
        self.world.regions["Pinwheel Forest West"].connect(
            self.world.regions["Pinwheel Forest Outside"],
            "Pinwheel Forest West to Pinwheel Forest Outside",
            lambda state: state.has("Loot Sack", self.world.player)
        )
        self.world.regions["Skyarrow Bridge"].connect(
            self.world.regions["Pinwheel Forest West"],
            "Skyarrow Bridge to Pinwheel Forest West",
            lambda state: state.has("Dragon Skull", self.world.player)
        )
        self.world.regions["Castelia City"].connect(
            self.world.regions["Skyarrow Bridge"],
            "Castelia City to Skyarrow Bridge",
            lambda state: True
        )
        self.world.regions["Route 4 South"].connect(
            self.world.regions["Castelia City"],
            "Route 4 South to Castelia City",
            lambda state: True
        )
        self.world.regions["Route 4 North"].connect(
            self.world.regions["Route 4 South"],
            "Route 4 North to Route 4 South",
            lambda state: state.has("Machine Part", self.world.player)
        )
        self.world.regions["Nimbasa City"].connect(
            self.world.regions["Route 4 North"],
            "Nimbasa City to Route 4 North",
            lambda state: True
        )
        self.world.regions["Driftveil Drawbridge"].connect(
            self.world.regions["Route 5"],
            "Driftveil Drawbridge to Route 5",
            lambda state: state.has("Tidal Bell", self.world.player)
        )
        self.world.regions["Route 16"].connect(
            self.world.regions["Nimbasa City"],
            "Route 16 to Nimbasa City",
            lambda state: True
        )
        self.world.regions["Marvelous Bridge"].connect(
            self.world.regions["Route 16"],
            "Marvelous Bridge to Route 16",
            lambda state: state.has("Blue Card", self.world.player)
        )
        self.world.regions["Challenger's Cave"].connect(
            self.world.regions["Route 9"],
            "Challenger's Cave Exit to Route 9",
            lambda state: challengers_cave(state, self.world)
        )
        self.world.regions["Wellspring Cave Entrance"].connect(
            self.world.regions["Route 3"],
            "Wellspring Cave Exit to Route 3",
            lambda state: True
        )
        self.world.regions["Liberty Garden"].connect(
            self.world.regions["Castelia City"],
            "Liberty Garden to Castelia City Ferry",
            lambda state: True
            )

        if self.get_option("add_rock_smash", False):
            self.world.rock_smash_species = set(name for name, data in moveset_table.items() if "TM94" in data.tm_hm_moves)
            def can_use_rock_smash(state: CollectionState, world: "PokemonBWWorld") -> bool:
                return state.has("TM94 Rock Smash", world.player) and state.has_any(world.rock_smash_species, world.player)

            tm_hm.tm["TM94 Rock Smash"] = tm_hm.tm["TM94 Rock Smash"]._replace(classification=classification.always_progression)  # This will make TM94 progression for all BW players in the multiworld

            self.world.regions["Wellspring Cave Entrance"].connect(
                self.world.regions["Challenger's Cave"],
                "Wellspring Cave to Challenger's Cave Warp",
                lambda state: can_use_rock_smash(state, self.world) and dark_cave(state, self.world)
            )
            self.world.regions["Challenger's Cave"].connect(
                self.world.regions["Wellspring Cave Entrance"],
                "Challenger's Cave to Wellspring Cave Warp",
                lambda state: can_use_rock_smash(state, self.world) and dark_cave(state, self.world)
            )

            region = self.world.regions["Wellspring Cave Entrance"]
            location = PokemonBWLocation(self.world.player, "Rock Smash static Wellspring Cave", None, region)
            location.place_locked_item(PokemonBWItem("Dwebble", ItemClassification.progression, None, self.world.player))
            location.access_rule = lambda state: can_use_rock_smash(state, self.world)
            region.locations.append(location)

            region = self.world.regions["Challenger's Cave"]
            location = PokemonBWLocation(self.world.player, "Rock Smash static Challenger's Cave", None, region)
            location.place_locked_item(PokemonBWItem("Dwebble", ItemClassification.progression, None, self.world.player))
            location.access_rule = lambda state: can_use_rock_smash(state, self.world) and dark_cave(state, self.world)
            region.locations.append(location)

            region = self.world.regions["Route 13"]
            location = PokemonBWLocation(self.world.player, "Rock Smash static Route 13", None, region)
            location.place_locked_item(PokemonBWItem("Dwebble", ItemClassification.progression, None, self.world.player))
            location.access_rule = lambda state: can_use_rock_smash(state, self.world)
            region.locations.append(location)

            self.world.get_location("Wellspring Cave - 1F hidden item #1").access_rule = lambda state: can_use_rock_smash(state, self.world)
            self.world.get_location("Wellspring Cave - 1F north east item").access_rule = lambda state: can_use_rock_smash(state, self.world)
            self.world.get_location("Challenger's Cave - B1F south item").access_rule = lambda state: can_use_rock_smash(state, self.world)

            self.world.get_entrance("Route 13 south gate").access_rule = lambda state: can_use_rock_smash(state, self.world)
            self.world.get_entrance("Undella Town north gate").access_rule = lambda state: can_use_rock_smash(state, self.world)

        if self.get_option("hm_with_badges", False):
            def cut_with_trio_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
                return old_rule(state, world) and state.has("Trio Badge", world.player)
            self.modify_rule(can_use_cut, cut_with_trio_badge)

            def surf_with_quake_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
                return old_rule(state, world) and state.has("Quake Badge", world.player)
            self.modify_rule(can_use_surf, surf_with_quake_badge)
            self.modify_rule(can_use_waterfall, surf_with_quake_badge)
            self.modify_rule(can_use_dive, surf_with_quake_badge)

            def strength_with_bolt_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
                return old_rule(state, world) and state.has("Bolt Badge", world.player)
            self.modify_rule(can_use_strength, strength_with_bolt_badge)

            def waterfall_with_freeze_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
                return old_rule(state, world) and state.has("Freeze Badge", world.player)
            self.modify_rule(can_use_waterfall, waterfall_with_freeze_badge)

            def dive_with_legend_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
                return old_rule(state, world) and state.has("Legend Badge", world.player)
            self.modify_rule(can_use_dive, dive_with_legend_badge)

            def surf_or_strength_with_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
                return surf_with_quake_badge(old_rule, state, world) or strength_with_bolt_badge(old_rule, state, world)
            self.modify_rule(can_use_surf_or_strength, surf_or_strength_with_badge)

            if self.get_option("add_rock_smash", False):
                def rock_smash_with_basic_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
                    return old_rule(state, world) and state.has("Basic Badge", world.player)
                self.modify_rule(can_use_rock_smash, rock_smash_with_basic_badge)

        if self.get_option("add_ss_ticket", False):
            self.world.regions["P2 Laboratory"].connect(
                self.world.regions["Liberty Garden"],
                "P2 Lab to Liberty Garden Ferry",
                lambda state: state.has("Liberty Pass", self.world.player)
            )
            self.world.regions["Liberty Garden"].connect(
                self.world.regions["P2 Laboratory"],
                "Liberty Garden to P2 Lab Ferry",
                lambda state: True
                )
            self.world.regions["Liberty Garden"].connect(
                self.world.regions["Undella Town"],
                "Liberty Garden to Undella Town Ferry",
                lambda state: state.has("S.S. Ticket", self.world.player)
            )
            self.world.regions["Undella Town"].connect(
                self.world.regions["Liberty Garden"],
                "Undella Town to Liberty Garden Ferry",
                lambda state: state.has("S.S. Ticket", self.world.player) and state.has("Liberty Pass", self.world.player)
            )

    # This is called after generating the item pool of a world and placing all locked items (e.g. gym badges in gym rewards)
    def create_items(self, item_pool: list["PokemonBWItem"]):
        if DEV: return

        # Add S.S. Ticket
        if self.get_option("add_ss_ticket", False):
            for i in range(len(item_pool)):
                item = item_pool[i]
                if item.classification == ItemClassification.filler:
                    item_pool[i] = self.new_item("S.S. Ticket", ItemClassification.progression)
                    break


# Just run this python script and it will pack this plugin into an apworld file for you.
# Note that any file or folder that contains "_temp" in its name will be ignored and the archipelago.json that's
# bundled will be overwritten.
if __name__ == '__main__':
    from data.build import build

    build(Plugin.name, Plugin.version, Plugin.author)
