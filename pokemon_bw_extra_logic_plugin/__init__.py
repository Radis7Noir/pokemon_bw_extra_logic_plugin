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
    version = "1.6.0"
    author = "RadisNoir"

    # This is called during the patching process, after the main apworld did all its standard modifications to the rom.
    def patch(self):
        if DEV: return

        if not any(p.name == "Pokemon BW QoL Plugin" for p in self.all_plugins):
            for i in [12, 32, 214, 308, 310, 510, 642, 648, 652, 706, 866]:
                loaded_file = pkgutil.get_data(__name__, f"files/a057/{i:03d}")
                narc_file = self.get_from_narc("a/0/5/7", i)
                self.otpp_patch_array(narc_file, loaded_file)
            for i in [21, 67, 112, 163, 271, 280, 353, 356, 385]:
                loaded_file = pkgutil.get_data(__name__, f"files/a003/{i:03d}")
                narc_file = self.get_from_narc("a/0/0/3", i)
                self.otpp_patch_array(narc_file, loaded_file)
            for i in [16, 62, 154, 321]:
                loaded_file = pkgutil.get_data(__name__, f"files/a125/{i:03d}")
                narc_file = self.get_from_narc("a/1/2/5", i)
                self.otpp_patch_array(narc_file, loaded_file)

            if not self.get_option("extra_cut_trees", False):
                loaded_file = pkgutil.get_data(__name__, f"files/a125/155")
                narc_file = self.get_from_narc("a/1/2/5", 155)
                self.otpp_patch_array(narc_file, loaded_file)

            if self.get_option("extra_cut_trees", False):
                loaded_file = pkgutil.get_data(__name__, f"files/a125/extra_cut_trees/155_cut_trees")
                narc_file = self.get_from_narc("a/1/2/5", 155)
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
            for i in [324, 348, 353]:
                loaded_file = pkgutil.get_data(__name__, f"files/a125/add_rock_smash/{i:03d}")
                narc_file = self.get_from_narc("a/1/2/5", i)
                self.otpp_patch_array(narc_file, loaded_file)
            if not self.get_option("move_strength_boulders", False):
                loaded_file = pkgutil.get_data(__name__, f"files/a125/370_rock")
                narc_file = self.get_from_narc("a/1/2/5", 370)
                self.otpp_patch_array(narc_file, loaded_file)
            if self.get_option("add_rock_smash_musharna", False):
                loaded_file = pkgutil.get_data(__name__, f"files/a125/add_rock_smash/153")
                narc_file = self.get_from_narc("a/1/2/5", 153)
                self.otpp_patch_array(narc_file, loaded_file)

        if self.get_option("extra_cut_trees", False) and self.get_option("extra_cut_trees_kyurem", False):
            loaded_file = pkgutil.get_data(__name__, f"files/a125/extra_cut_trees/232")
            narc_file = self.get_from_narc("a/1/2/5", 232)
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

        if self.get_option("move_strength_boulders", False):
            for i in [152, 208]:
                loaded_file = pkgutil.get_data(__name__, f"files/a125/move_strength_boulders/{i:03d}")
                narc_file = self.get_from_narc("a/1/2/5", i)
                self.otpp_patch_array(narc_file, loaded_file)
            if self.get_option("move_strength_boulders_vi_road", False):
                loaded_file = pkgutil.get_data(__name__, f"files/a125/move_strength_boulders/224")
                narc_file = self.get_from_narc("a/1/2/5", 224)
                self.otpp_patch_array(narc_file, loaded_file)
            if not self.get_option("add_rock_smash", False):
                loaded_file = pkgutil.get_data(__name__, f"files/a125/370_boulder")
                narc_file = self.get_from_narc("a/1/2/5", 370)
                self.otpp_patch_array(narc_file, loaded_file)
 
        if self.get_option("add_rock_smash", False) and self.get_option("move_strength_boulders", False):
            loaded_file = pkgutil.get_data(__name__, f"files/a125/370_rock_boulder")
            narc_file = self.get_from_narc("a/1/2/5", 370)
            self.otpp_patch_array(narc_file, loaded_file)

        if self.get_option("add_pass", False):
            for i in [107, 255]:
                loaded_file = pkgutil.get_data(__name__, f"files/a125/add_pass/{i:03d}")
                narc_file = self.get_from_narc("a/1/2/5", i)
                self.otpp_patch_array(narc_file, loaded_file)
            for i in [188, 190, 191, 193]:
                loaded_file = pkgutil.get_data(__name__, f"files/a008/add_pass/{i:03d}")
                narc_file = self.get_from_narc("a/0/0/8", i)
                self.otpp_patch_array(narc_file, loaded_file)

        # Dark Areas NARC Hex Edit
        dark_areas_narc = self.get_from_narc("a/1/4/9", 0)
        dark_areas_narc.clear()
        dark_areas_list = self.slot_data.get("dark_areas", ())

        dark_areas_narc += (7).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Striaton Gym" in dark_areas_list else b'\0\0'

        dark_areas_narc += (18).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Nacrene Gym" in dark_areas_list else b'\0\0'

        dark_areas_narc += (29).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Castelia Gym" in dark_areas_list else b'\0\0'

        dark_areas_narc += (63).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Nimbasa Gym" in dark_areas_list else b'\0\0'

        dark_areas_narc += (97).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Driftveil Gym" in dark_areas_list else b'\0\0'

        dark_areas_narc += (108).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Mistralton Gym" in dark_areas_list else b'\0\0'

        dark_areas_narc += (114).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Icirrus Gym" in dark_areas_list else b'\0\0'

        dark_areas_narc += (121).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Opelucid Gym" in dark_areas_list else b'\0\0'

        dark_areas_narc += (153).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Dreamyard Basement" in dark_areas_list else b'\0\0'

        dark_areas_narc += (324).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Wellspring Cave 1F" in dark_areas_list else b'\0\0'

        dark_areas_narc += (325).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Wellspring Cave B1F" in dark_areas_list else b'\0\0'

        dark_areas_narc += (155).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Pinwheel Forest Inside" in dark_areas_list else b'\0\0'

        for i in [160, 161, 162, 163, 164, 190]:
            dark_areas_narc += i.to_bytes(2, "little")
            dark_areas_narc += b'\1\0' if "Relic Castle Pre-Sand Room" in dark_areas_list else b'\0\0'

        for i in range(166, 189):
            dark_areas_narc += i.to_bytes(2, "little")
            dark_areas_narc += b'\1\0' if "Relic Castle Post-Sand Room" in dark_areas_list else b'\0\0'

        for i in [192, 193]:
            dark_areas_narc += i.to_bytes(2, "little")
            dark_areas_narc += b'\1\0' if "Cold Storage" in dark_areas_list else b'\0\0'

        for i in [333, 334]:
            dark_areas_narc += i.to_bytes(2, "little")
            dark_areas_narc += b'\1\0' if "Mistralton Cave" in dark_areas_list else b'\0\0'

        dark_areas_narc += (335).to_bytes(2, "little")
        dark_areas_narc += b'\1\0' if "Guidance Chamber" in dark_areas_list else b'\0\0'

        for i in range(195, 197):
            dark_areas_narc += i.to_bytes(2, "little")
            dark_areas_narc += b'\1\0' if "Chargestone Cave" in dark_areas_list else b'\0\0'

        for i in range(339, 341):
            dark_areas_narc += i.to_bytes(2, "little")
            dark_areas_narc += b'\1\0' if "Celestial Tower" in dark_areas_list else b'\0\0'

        for i in range(200, 203):
            dark_areas_narc += i.to_bytes(2, "little")
            dark_areas_narc += b'\1\0' if "Twist Mountain" in dark_areas_list else b'\0\0'

        for i in range(207, 212):
            dark_areas_narc += i.to_bytes(2, "little")
            dark_areas_narc += b'\1\0' if "Dragonspiral Tower" in dark_areas_list else b'\0\0'

        for i in range(352, 354):
            dark_areas_narc += i.to_bytes(2, "little")
            dark_areas_narc += b'\1\0' if "Challengers Cave" in dark_areas_list else b'\0\0'

        for i in range(215, 229):
            dark_areas_narc += i.to_bytes(2, "little")
            dark_areas_narc += b'\1\0' if "Victory Road" in dark_areas_list else b'\0\0'

        for i in [231, 234]:
            dark_areas_narc += i.to_bytes(2, "little")
            dark_areas_narc += b'\1\0' if "Giant Chasm" in dark_areas_list else b'\0\0'

        for i in range(245, 248):
            dark_areas_narc += i.to_bytes(2, "little")
            dark_areas_narc += b'\1\0' if "Abyssal Ruins" in dark_areas_list else b'\0\0'


    def generate_early(self):
        if DEV: return

        # Get full and player-provided lists
        # `support_weighting=False` is very important if you want to add a list option
        all_dark_areas = [
            "Striaton Gym",
            "Nacrene Gym",
            "Castelia Gym",
            "Nimbasa Gym",
            "Driftveil Gym",
            "Mistralton Gym",
            "Icirrus Gym",
            "Opelucid Gym",
            "Dreamyard Basement",
            "Wellspring Cave 1F",
            "Wellspring Cave B1F",
            "Pinwheel Forest Inside",
            "Relic Castle Pre-Sand Room",
            "Relic Castle Post-Sand Room",
            "Cold Storage",
            "Mistralton Cave",
            "Guidance Chamber",
            "Chargestone Cave",
            "Celestial Tower",
            "Twist Mountain",
            "Dragonspiral Tower",
            "Challengers Cave",
            "Victory Road",
            "Giant Chasm",
            "Abyssal Ruins"
        ]
        dark_areas_list: list[str] = self.get_option("dark_areas", [], typ=list, support_weighting=False).copy()
        
        # Process _Random and _All
        if "_All" in dark_areas_list:
            dark_areas_list = all_dark_areas
        elif "_Random" in dark_areas_list:
            for area in all_dark_areas:
                if area not in dark_areas_list and self.random.random() < 0.5:
                    dark_areas_list.append(area)

        # Add to world and slot data
        self.world.dark_areas = dark_areas_list
        self.world.extended_slot_data()["dark_areas"] = dark_areas_list

    @classmethod
    def stage_init(cls):
        from worlds.pokemon_bw.data.locations.rules import can_use_surf, can_use_waterfall, can_use_dive, can_use_cut, can_use_strength, can_use_flash, can_encounter_swords_of_justice

        def cut_with_trio_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
            return old_rule(state, world) and (state.has("Trio Badge", world.player) or not world.hm_with_badges)
        cls.modify_rule(can_use_cut, cut_with_trio_badge)

        def surf_with_quake_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
            return old_rule(state, world) and (state.has("Quake Badge", world.player) or not world.hm_with_badges)
        cls.modify_rule(can_use_surf, surf_with_quake_badge)

        def strength_with_bolt_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
            return old_rule(state, world) and (state.has("Bolt Badge", world.player) or not world.hm_with_badges)
        cls.modify_rule(can_use_strength, strength_with_bolt_badge)

        def waterfall_with_freeze_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
            return old_rule(state, world) and (state.has("Freeze Badge", world.player) or not world.hm_with_badges)
        cls.modify_rule(can_use_waterfall, waterfall_with_freeze_badge)

        def dive_with_legend_badge(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
            return old_rule(state, world) and (state.has("Legend Badge", world.player) or not world.hm_with_badges)
        cls.modify_rule(can_use_dive, dive_with_legend_badge)

        def swords_of_justice_with_dark_areas(old_rule: "ExtendedRule", state: CollectionState, world: "PokemonBWWorld") -> bool:
            return old_rule(state, world) and ((can_use_flash(state, world) and "Guidance Chamber" in world.dark_areas) or not "Guidance Chamber" in world.dark_areas)
        cls.modify_rule(can_encounter_swords_of_justice, swords_of_justice_with_dark_areas)


    # This is called after generating all regions, regions connections, locations, and events
    def create_regions(self, catchable_species_data: dict[str, "SpeciesData"]):
        from worlds.pokemon_bw.data.pokemon.movesets import table as moveset_table
        from worlds.pokemon_bw.data.locations.rules import (can_use_cut, can_use_surf, can_use_dive, can_use_strength, can_use_surf_or_strength,
                                                            dark_cave, challengers_cave)
        if DEV: return

        self.world.hm_with_badges = self.get_option("hm_with_badges", False)

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
        self.world.regions["Dreamyard South"].connect(
            self.world.regions["Dreamyard Basement"],
            "Dreamyard South to Dreamyard Basement",
            lambda state: True
        )
        self.world.regions["Dreamyard Basement"].connect(
            self.world.regions["Dreamyard Entrance"],
            "Dreamyard Basement to Dreamyard Entrance",
            lambda state: state.has("Basement Key", self.world.player)
        )


        if self.get_option("extra_cut_trees", False):

            self.world.get_entrance("Pinwheel Forest east").access_rule = lambda state: (
                state.can_reach_region("Nimbasa City", self.world.player)
                and state.has("Loot Sack", self.world.player)
                and state.can_reach_region("Nacrene City", self.world.player)
                )

            if not "Pinwheel Forest Inside" in self.world.dark_areas:
                self.world.regions["Pinwheel Forest Outside"].connect(
                    self.world.regions["Skyarrow Bridge"],
                    "Pinwheel Forest to Skyarrow Bridge with Cut",
                    lambda state: can_use_cut(state, self.world) and state.has("Dragon Skull", self.world.player)
                )
                self.world.regions["Skyarrow Bridge"].connect(
                    self.world.regions["Pinwheel Forest Outside"],
                    "Skyarrow Bridge to Pinwheel Forest with Cut",
                    lambda state: state.has("Dragon Skull", self.world.player) and can_use_cut(state, self.world)
                )
                self.world.get_entrance("Skyarrow Bridge to Pinwheel Forest West").access_rule = lambda state: (
                    state.has("Dragon Skull", self.world.player) and state.has("Loot Sack", self.world.player)
                    and (
                        can_use_cut(state, self.world) or
                        state.can_reach_region("Nacrene City", self.world.player)
                    )
                )
                self.world.get_entrance("Pinwheel Forest West to Pinwheel Forest Outside").access_rule = lambda state: True

            if "Pinwheel Forest Inside" in self.world.dark_areas:
                self.world.regions["Pinwheel Forest Outside"].connect(
                    self.world.regions["Skyarrow Bridge"],
                    "Pinwheel Forest to Skyarrow Bridge with Cut",
                    lambda state: can_use_cut(state, self.world) and state.has("Dragon Skull", self.world.player) and dark_cave(state, self.world)
                )
                self.world.regions["Skyarrow Bridge"].connect(
                    self.world.regions["Pinwheel Forest Outside"],
                    "Skyarrow Bridge to Pinwheel Forest with Cut",
                    lambda state: state.has("Dragon Skull", self.world.player) and can_use_cut(state, self.world) and dark_cave(state, self.world)
                )
                self.world.get_entrance("Skyarrow Bridge to Pinwheel Forest West").access_rule = lambda state: (
                    state.has("Dragon Skull", self.world.player) and state.has("Loot Sack", self.world.player) and dark_cave(state, self.world)
                    and (
                        can_use_cut(state, self.world) or
                        state.can_reach_region("Nacrene City", self.world.player)
                    )
                )
                self.world.get_entrance("Pinwheel Forest West to Pinwheel Forest Outside").access_rule = lambda state: dark_cave(state, self.world)

            if self.get_option("extra_cut_trees_kyurem", False):
                self.world.get_entrance("Giant Chasm crater north east cave entrance").access_rule = lambda state: can_use_cut(state, self.world)


        if self.get_option("move_strength_boulders", False):
            self.world.get_entrance("Route 13 north east").access_rule = lambda state: can_use_surf_or_strength(state, self.world)

            self.world.regions["Dreamyard Entrance"].connect(
                self.world.regions["Dreamyard South"],
                "Dreamyard Entrance to Dreamyard South",
                lambda state: can_use_strength(state, self.world)
            )
            if not "Icirrus Gym" and not "Dragonspiral Tower" in self.world.dark_areas:
                self.world.get_location("Dragonspiral Tower - 2F north east item").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Dragonspiral Tower - 2F item on pillar").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Dragonspiral Tower - 3F item").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Dragonspiral Tower - 4F item").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Dragonspiral Tower - 5F item #1").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Dragonspiral Tower - 5F item #2").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Dragonspiral Tower - 5F item #3").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Dragonspiral Tower - 6F item").access_rule = lambda state: can_use_strength(state, self.world)

            if "Icirrus Gym" or "Dragonspiral Tower" in self.world.dark_areas:
                self.world.get_location("Dragonspiral Tower - 2F north east item").access_rule = lambda state: can_use_strength(state, self.world) and dark_cave(state, self.world)
                self.world.get_location("Dragonspiral Tower - 2F item on pillar").access_rule = lambda state: can_use_strength(state, self.world) and dark_cave(state, self.world)
                self.world.get_location("Dragonspiral Tower - 3F item").access_rule = lambda state: can_use_strength(state, self.world) and dark_cave(state, self.world)
                self.world.get_location("Dragonspiral Tower - 4F item").access_rule = lambda state: can_use_strength(state, self.world) and dark_cave(state, self.world)
                self.world.get_location("Dragonspiral Tower - 5F item #1").access_rule = lambda state: can_use_strength(state, self.world) and dark_cave(state, self.world)
                self.world.get_location("Dragonspiral Tower - 5F item #2").access_rule = lambda state: can_use_strength(state, self.world) and dark_cave(state, self.world)
                self.world.get_location("Dragonspiral Tower - 5F item #3").access_rule = lambda state: can_use_strength(state, self.world) and dark_cave(state, self.world)
                self.world.get_location("Dragonspiral Tower - 6F item").access_rule = lambda state: can_use_strength(state, self.world) and dark_cave(state, self.world)

            if self.get_option("move_strength_boulders_vi_road", False):
                self.world.get_entrance("Victory Road north").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Victory Road Outside - Item #2").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Victory Road Outside - Item #3").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Victory Road Outside - Item #4").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Victory Road Outside - Item #6").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Victory Road 3F - Western cavern item").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Victory Road 4F - Western cavern item").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Victory Road 1F - Western cavern hidden item #1").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Victory Road 1F - Western cavern hidden item #2").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Victory Road 4F - Western cavern hidden item").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Victory Road 4F - Eastern cavern hidden item #1").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_location("Victory Road 4F - Eastern cavern hidden item #2").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_entrance("Victory Road (5F Cave) - Grass").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_entrance("Victory Road (5F Cave) - Rustling Grass").access_rule = lambda state: can_use_strength(state, self.world) and state.has("Trio Badge", self.world.player)
                self.world.get_entrance("Victory Road (6F Cave) - Grass").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_entrance("Victory Road (6F Cave) - Rustling Grass").access_rule = lambda state: can_use_strength(state, self.world) and state.has("Trio Badge", self.world.player)
                self.world.get_entrance("Victory Road (4F Right Cave) - Grass").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_entrance("Victory Road (4F Right Cave) - Rustling Grass").access_rule = lambda state: can_use_strength(state, self.world) and state.has("Trio Badge", self.world.player)
                self.world.get_entrance("Victory Road (7F Cave) - Grass").access_rule = lambda state: can_use_strength(state, self.world)
                self.world.get_entrance("Victory Road (7F Cave) - Rustling Grass").access_rule = lambda state: can_use_strength(state, self.world) and state.has("Trio Badge", self.world.player)

        if self.get_option("add_rock_smash", False):
            self.world.rock_smash_species = set(name for name, data in moveset_table.items() if "TM94" in data.tm_hm_moves)
            def can_use_rock_smash(state: CollectionState, world: "PokemonBWWorld") -> bool:
                return (state.has("TM94 Rock Smash", world.player)
                        and state.has_any(world.rock_smash_species, world.player)
                        and (state.has("Basic Badge", world.player) or not world.hm_with_badges))

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

            self.new_event(
                "Rock Smash Static Wellspring Cave", "Dwebble", "Wellspring Cave Entrance",
                extended_rule=can_use_rock_smash
            )
            self.new_event(
                "Rock Smash Static Challenger's Cave", "Dwebble", "Challenger's Cave",
                collection_rule=lambda state: can_use_rock_smash(state, self.world)
            )
            self.new_event(
                "Rock Smash Static Route 13", "Dwebble", "Route 13",
                extended_rule=can_use_rock_smash
            )

            self.world.get_location("Wellspring Cave - 1F hidden item #1").access_rule = lambda state: can_use_rock_smash(state, self.world)
            self.world.get_location("Wellspring Cave - 1F north east item").access_rule = lambda state: can_use_rock_smash(state, self.world)
            self.world.get_location("Challenger's Cave - B1F south item").access_rule = lambda state: can_use_rock_smash(state, self.world)

            self.world.get_entrance("Route 13 south gate").access_rule = lambda state: can_use_rock_smash(state, self.world)
            self.world.get_entrance("Undella Town north gate").access_rule = lambda state: can_use_rock_smash(state, self.world)

            if self.get_option("add_rock_smash_musharna", False):
                self.world.get_location("Dreamyard Static Encounter").access_rule = lambda state: can_use_rock_smash(state, self.world)
                self.world.get_location("Dreamyard Basement - North west item").access_rule = lambda state: can_use_rock_smash(state, self.world)
                self.world.get_entrance("Dreamyard (Basement) - Dark Grass").access_rule = lambda state: can_use_rock_smash(state, self.world)

                self.new_event(
                    "Rock Smash Static Dreamyard Basement", "Dwebble", "Dreamyard Basement",
                    extended_rule=can_use_rock_smash
                )

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

        if self.get_option("add_pass", False):
            self.world.regions["Mistralton City"].connect(
                self.world.regions["Village Bridge"],
                "Mistralton City to Village Bridge with Pass",
                lambda state: state.has("Maglev Pass", self.world.player)
            )
            self.world.regions["Village Bridge"].connect(
                self.world.regions["Mistralton City"],
                "Village Bridge to Mistralton City with Pass",
                lambda state: state.has("Maglev Pass", self.world.player)
            )

        # Dark Areas Logic
        if "Striaton Gym" in self.world.dark_areas:
            self.world.get_location("Striaton Gym - Gym guide item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Striaton Gym - Badge reward").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Striaton Gym - TM reward").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Striaton City - TM from Fennel").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Striaton City - Item from Amanita").access_rule = lambda state: dark_cave(state, self.world)

        if "Nacrene Gym" in self.world.dark_areas:
            self.world.get_location("Nacrene Gym - Gym guide item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Nacrene Gym - Badge reward").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Nacrene Gym - TM reward").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Nacrene City - Item from Bianca").access_rule = lambda state: dark_cave(state, self.world)

        if "Castelia Gym" in self.world.dark_areas:
            self.world.get_location("Castelia Gym - Gym guide item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Castelia Gym - Badge reward").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Castelia Gym - TM reward").access_rule = lambda state: dark_cave(state, self.world)

        if "Nimbasa Gym" in self.world.dark_areas:
            self.world.get_location("Nimbasa Gym - Gym guide item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Nimbasa Gym - Badge reward").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Nimbasa Gym - TM reward").access_rule = lambda state: dark_cave(state, self.world)

        if "Driftveil Gym" or "Cold Storage" in self.world.dark_areas:
            self.world.get_location("Driftveil Gym - Badge reward").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Driftveil City - TM from Bianca").access_rule = lambda state: dark_cave(state, self.world)

        if "Mistralton Gym" or "Celestial Tower" in self.world.dark_areas:
            self.world.get_location("Mistralton Gym - Gym guide item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Mistralton Gym - Badge reward").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Mistralton Gym - TM reward").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Mistralton City - Appearing item at south end of runway").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Twist Mountain - TM from Alder").access_rule = lambda state: dark_cave(state, self.world)

        if "Icirrus Gym" in self.world.dark_areas:
            self.world.get_location("Icirrus Gym - Gym guide item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Icirrus Gym - Badge reward").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Icirrus Gym - TM reward").access_rule = lambda state: dark_cave(state, self.world)

        if "Opelucid Gym" in self.world.dark_areas:
            self.world.get_location("Opelucid Gym - Gym guide item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Opelucid Gym - Badge reward").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Opelucid Gym - TM reward").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Opelucid City - Item from Professor Juniper").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Route 10 - Item from Bianka #1").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Route 10 - Item from Bianka #2").access_rule = lambda state: dark_cave(state, self.world)

        if "Dreamyard Basement" in self.world.dark_areas:
            self.world.get_entrance("Dreamyard South to Dreamyard Basement").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_entrance("Dreamyard Basement to Dreamyard Entrance").access_rule = lambda state: dark_cave(state, self.world) and state.has("Basement Key", self.world.player)
            self.world.get_entrance("Dreamyard traffic cone").access_rule = lambda state: dark_cave(state, self.world) and state.has("Basement Key", self.world.player)
            self.world.get_entrance("Dreamyard basement south").access_rule = lambda state: dark_cave(state, self.world)

        if "Wellspring Cave 1F" in self.world.dark_areas:
            self.world.get_entrance("Route 3 north west").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_entrance("Wellspring Cave Exit to Route 3").access_rule = lambda state: dark_cave(state, self.world)

        if not "Wellspring Cave 2F" in self.world.dark_areas:
            self.world.get_entrance("Wellspring Cave Stairs").access_rule = lambda state: True

        if "Pinwheel Forest Inside" in self.world.dark_areas and not self.get_option("extra_cut_trees", False):
            self.world.get_entrance("Enter Pinwheel Forest").access_rule = lambda state: dark_cave(state, self.world) and state.has("Loot Sack", self.world.player)
            self.world.get_entrance("Pinwheel Forest north").access_rule = lambda state: dark_cave(state, self.world) and state.has("Dragon Skull", self.world.player)
            self.world.get_entrance("Skyarrow Bridge to Pinwheel Forest West").access_rule = lambda state: dark_cave(state, self.world) and state.has("Dragon Skull", self.world.player)
            self.world.get_entrance("Pinwheel Forest West to Pinwheel Forest Outside").access_rule = lambda state: dark_cave(state, self.world) and state.has("Loot Sack", self.world.player)

        if "Relic Castle Pre-Sand Room" in self.world.dark_areas:
            self.world.get_entrance("Desert Resort tower").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_entrance("Desert Resort stairs").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_entrance("Relic Castle B2F castleside").access_rule = lambda state: dark_cave(state, self.world)

        if "Relic Castle Post-Sand Room" in self.world.dark_areas:
            self.world.get_entrance("Relic Castle B5F castleside").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_entrance("Relic Castle basement top left").access_rule = lambda state: dark_cave(state, self.world)

        if "Cold Storage" in self.world.dark_areas:
            self.world.get_location("Cold Storage Building - Item near entrance, up the stairs").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Cold Storage Building - Item on first ice field").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Cold Storage Building - South east item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Cold Storage Building - North east item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Cold Storage Building - Item in container").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Cold Storage - TM from sage Zinzolin").access_rule = lambda state: dark_cave(state, self.world)

        if not "Mistralton Cave" in self.world.dark_areas:
            self.world.get_entrance("Route 6 north east cave entrance").access_rule = lambda state: can_use_surf(state, self.world)

        if "Guidance Chamber" in self.world.dark_areas:
            self.world.get_location("Mistralton Cave - 3F north east hidden item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Mistralton Cave - 3F north west hidden item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Mistralton Cave - 3F south west item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Mistralton Cave - 3F north east item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Mistralton Cave - 3F north west item").access_rule = lambda state: dark_cave(state, self.world)

        if "Chargestone Cave" in self.world.dark_areas:
            self.world.get_entrance("Mistralton City cave entrance").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_entrance("Chargestone Cave north exit").access_rule = lambda state: dark_cave(state, self.world)

        if "Celestial Tower" in self.world.dark_areas:
            self.world.get_entrance("Route 7 tower").access_rule = lambda state: dark_cave(state, self.world)

        if "Twist Mountain" in self.world.dark_areas:
            self.world.get_entrance("Twist Mountain east exit").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_entrance("Icirrus City cave entrance").access_rule = lambda state: dark_cave(state, self.world)

        if ("Dragonspiral Tower" in self.world.dark_areas or "Icirrus Gym" in self.world.dark_areas) and not self.get_option("move_strength_boulders", False):
            self.world.get_location("Dragonspiral Tower - 2F north east item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Dragonspiral Tower - 2F item on pillar").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Dragonspiral Tower - 3F item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Dragonspiral Tower - 4F item").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Dragonspiral Tower - 5F item #1").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Dragonspiral Tower - 5F item #2").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Dragonspiral Tower - 5F item #3").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_location("Dragonspiral Tower - 6F item").access_rule = lambda state: dark_cave(state, self.world)

        if "Dragonspiral Tower" in self.world.dark_areas or "Icirrus Gym" in self.world.dark_areas:
            self.world.get_entrance("Dragonspiral Tower (1F) - Grass").access_rule = lambda state: dark_cave(state, self.world)
            self.world.get_entrance("Dragonspiral Tower (2F) - Grass").access_rule = lambda state: dark_cave(state, self.world)

        if not "Challengers Cave" in self.world.dark_areas:
            self.world.get_entrance("Route 9 cave entrance").access_rule = lambda state: state.has("Red Chain", self.world.player)
            self.world.get_entrance("Challenger's Cave Exit to Route 9").access_rule = lambda state: dark_cave(state, self.world)

        if self.get_option("add_rock_smash", False) and not "Challengers Cave" in self.world.dark_areas and not "Wellspring Cave 1F" in self.world.dark_areas:
            self.world.get_entrance("Wellspring Cave to Challenger's Cave Warp").access_rule = lambda state: can_use_rock_smash(state, self.world)
            self.world.get_entrance("Challenger's Cave to Wellspring Cave Warp").access_rule = lambda state: can_use_rock_smash(state, self.world)

        if "Victory Road" in self.world.dark_areas:
            self.world.get_entrance("Legend Badge gate").access_rule = lambda state: state.has("Legend Badge", self.world.player) and dark_cave(state, self.world)

        if "Giant Chasm" in self.world.dark_areas:
            self.world.get_entrance("Giant Chasm outer cave entrance").access_rule = lambda state: dark_cave(state, self.world)

        if "Abyssal Ruins" in self.world.dark_areas:
            self.world.get_entrance("Undella Bay dive spots").access_rule = lambda state: can_use_dive(state, self.world) and dark_cave(state, self.world)


    # This is called after generating the item pool of a world, but before placing all locked items (e.g. gym badges in gym rewards)
    def create_items_main_only(self, item_pool: list["PokemonBWItem"]):
        if DEV: return

        if self.get_option("add_rock_smash", False):
            for item in item_pool:
                if item.name == "TM94 Rock Smash":
                    item.classification = ItemClassification.progression

        # Add S.S. Ticket
        if self.get_option("add_ss_ticket", False):
            item_pool.append(self.new_item("S.S. Ticket", ItemClassification.progression))
        
        # Add Pass
        if self.get_option("add_pass", False):
            item_pool.append(self.new_item("Maglev Pass", ItemClassification.progression))

# Just run this python script and it will pack this plugin into an apworld file for you.
# Note that any file or folder that contains "_temp" in its name will be ignored and the archipelago.json that's
# bundled will be overwritten.
if __name__ == '__main__':
    from data.build import build

    build(Plugin.name, Plugin.version, Plugin.author)
