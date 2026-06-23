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
        from worlds.pokemon_bw.data import SpeciesData, ExtendedRule
        from worlds.pokemon_bw import PokemonBWWorld
    from worlds.pokemon_bw.plugins._dev import DEV
except ImportError:
    DEV = False


# This has to exactly be named "Plugin" and should inherit from "PluginProtocol"
class Plugin(PluginProtocol):

    name = "Pokemon BW Extra Logic Plugin"
    domain = "extra_logic"
    version = "1.0.0"
    author = "RadisNoir"


    # This is called during the patching process, after the main apworld did all its standard modifications to the rom.
    def patch(self):
        if DEV: return

        if self.get_option("add_rock_smash", False):
            for i in [TO DETERMINE]:
                if any(p.name == "Pokemon BW QoL Plugin" for p in self.all_plugins):  # To be handled by the QoL plugin
                    continue
                else:
                    loaded_file = pkgutil.get_data(__name__, f"files/a125/blind_trainers/{i:03d}")
                narc_file = self.get_from_narc("a/1/2/5", i)
                self.otpp_patch_array(narc_file, loaded_file)

        if self.get_option("hm_with_badges", False):
            for i in [TO DETERMINE]:
                if any(p.name == "Pokemon BW QoL Plugin" for p in self.all_plugins):
                    continue
                else:
                    loaded_file = pkgutil.get_data(__name__, f"files/a125/blind_trainers/{i:03d}")
                narc_file = self.get_from_narc("a/1/2/5", i)
                self.otpp_patch_array(narc_file, loaded_file)

        if self.get_option("add_ss_ticket", False):
            for i in [TO DETERMINE]:
                if any(p.name == "Pokemon BW QoL Plugin" for p in self.all_plugins):
                    continue
                else:
                    loaded_file = pkgutil.get_data(__name__, f"files/a125/blind_trainers/{i:03d}")
                narc_file = self.get_from_narc("a/1/2/5", i)
                self.otpp_patch_array(narc_file, loaded_file)

    # This is called pretty much at the beginning of generating the world.
    def generate_early(self):
        from worlds.pokemon_bw.data.locations.rules import can_use_surf, can_use_waterfall, can_use_dive, can_use_cut, can_use_strength, can_use_surf_or_strength
        if DEV: return

        if self.get_option("add_rock_smash", False):
            def can_use_rock_smash("ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:  # Not sure I need that since it's a new rule
                return state.has("TM94 Rock Smash", world.player) and state.has_any(world.rock_smash_species, world.player)

            def can_use_surf_or_rock_smash("ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
                return can_use_surf(state, world) or can_use_rock_smash(state, world)

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
                return can_use_surf(state, world) or can_use_strength(state, world)
            self.modify_rule(can_use_surf_or_strength, surf_or_strength_with_badge)

            if self.get_option("add_rock_smash", False):
                def rock_smash_with_basic_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
                    return old_rule(state, world) and state.has("Basic Badge", world.player)
                self.modify_rule(can_use_rock_smash, rock_smash_with_basic_badge)
            else
                continue

    # This is called after generating all regions, regions connections, locations, and events
    def create_regions(self, catchable_species_data: dict[str, "SpeciesData"]):
        from worlds.pokemon_bw.data.locations.rules import challengers_cave
        if DEV: return

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

        if self.get_option("add_rock_smash", False):
            self.world.regions["Wellspring Cave Entrance"].connect(
                self.world.regions["Challenger's Cave"],
                "Wellspring Cave to Challenger's Cave Warp",
                lambda state: can_use_rock_smash(state, world)
            )
            self.world.regions["Challenger's Cave"].connect(
                self.world.regions["Wellspring Cave"],
                "Challenger's Cave to Wellspring Cave Warp",
                lambda state: can_use_rock_smash(state, world) and challengers_cave(state, world)
            )
            self.world.regions["Undella Town"].connect(  # Probably not good, need to change the old connection. How to put locations in there?
                self.world.regions["Route 13"],
                "Route 13 South",
                lambda state: can_use_rock_smash(state, world)
            )
            self.world.regions["Route 13"].connect(
                self.world.regions["Undella Town"],
                "Route 13 North",
                lambda state: can_use_rock_smash(state, world)
            )

    # This is called after generating the item pool of a world and placing all locked items (e.g. gym badges in gym rewards)
    def create_items(self, item_pool: list["PokemonBWItem"]):
        if DEV: return

        # Add S.S. Ticket
        if self.get_option("add_ss_ticket", False):
            for i in range(len(item_pool)):
                item = item_pool[i]
                if item.name == "S.S. Ticket":
                    item.classification = ItemClassification.progression
            for i in range(len(item_pool)):
                item = item_pool[i]
                if item.classification == ItemClassification.filler:
                    item_pool[i] = self.new_item("S.S. Ticket")
                    break

        # Add Rock Smash
        if self.get_option("add_rock_smash", False):
            for i in range(len(item_pool)):
                item = item_pool[i]
                if item.name == "TM94 Rock Smash":
                    item.classification = ItemClassification.progression


# Just run this python script and it will pack this plugin into an apworld file for you.
# Note that any file or folder that contains "_temp" in its name will be ignored and the archipelago.json that's
# bundled will be overwritten.
if __name__ == '__main__':
    from data.build import build

    build(Plugin.name, Plugin.version, Plugin.author)
