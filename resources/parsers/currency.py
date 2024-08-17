"""
Filter creation for currency and currency-recipe items.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict
from resources.parsers.templates import FilterTemplates


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class CurrencyParser:
    """
    Filtering for all currency item drops.
    """

    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
        self.debug = debug

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# ======================== #\n")
        self.filter_file.write("# === [{0}] - Currency === #\n".format(self.parse_num))
        self.filter_file.write("# ======================== #\n")
        self.filter_file.write("\n")

        self.general_currency()
        self.league_specific()
        self.quest_like_items()
        self.currency_catchall()

    def general_currency(self):
        """
        Handling for general currency items.
        """
        self.parse_subnum += 1

        self.filter_file.write("\n")
        self.filter_file.write("# ----------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - General Currency --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ----------------------------------- #\n")
        self.filter_file.write("\n")

        # Mirror of Kalandra.
        self.template.rare_currency(
            description="Mirror of Kalandra",
            base_text="Mirror of Kalandra",
            background_color=display_dict["unique_background"],
            border_color=display_dict["unique"],
            text_color=display_dict["unique_text"],
            font_size=display_dict["unique_font_size"],
            minimap_size=0,
            minimap_color=display_dict["minimap_color_unique"],
            minimap_shape=display_dict["minimap_icon_currency"],
            sound="ShMirror 300",
            playeffect=display_dict["minimap_color_unique"],
        )

        # Exalted Orb.
        self.template.rare_currency(
            description="Exalted Orb",
            base_text="Exalted Orb",
            sound="ShExalted 300",
        )

        # Divine Orb.
        self.template.rare_currency(
            description="Divine Orb",
            base_text="Divine Orb",
            sound="ShDivine 300",
        )

        # Regal Orb.
        self.template.rare_currency(
            description="Regal Orb",
            base_text="Regal Orb",
            sound="ShRegal 300",
        )

        # Blessed Orb.
        self.template.rare_currency(
            description="Blessed Orb",
            base_text="Blessed Orb",
            sound="ShBlessed 300",
        )

        # Vaal Orb.
        self.template.rare_currency(
            description="Vaal Orb",
            base_text="Vaal Orb",
            sound="ShVaal 300",
        )

        # Chaos Orb.
        self.template.rare_currency(
            description="Chaos Orb",
            base_text="Chaos Orb",
            sound="ShChaos 300",
        )

        # Orb of Fusing.
        self.template.rare_currency(
            description="Orb of Fusing",
            base_text="Orb of Fusing",
            font_size=display_dict["rare_font_size"],
            minimap_size=1,
            sound="ShFusing 300",
        )

        # Orb of Alchemy.
        self.template.rare_currency(
            description="Orb of Alchemy",
            base_text="Orb of Alchemy",
            font_size=display_dict["rare_font_size"],
            minimap_size=1,
            sound="ShAlchemy 250",
        )

        # Divination Cards.
        self.template.card_item(
            description="Divination Cards",
            class_text="Currency",
            base_text=["Stacked Deck"],
        )
        self.template.card_item(
            class_text=["Divination Card"],
        )

        # Misc important currency.
        self.template.rare_currency(
            description="Misc Important Currency",
            base_text=[
                "Cartographer's Chisel",
                "Orb of Scouring",
                "Orb of Regret",
                "Silver Coin",
                "Gemcutter's Prism",
                "Eternal Orb",
                "Master Cartographer's Seal",
                "Albino Rhoa Feather",
                "Orb of Chance",
                "Sextant",
                "Awakener's Orb",
                "Bestiary Orb",
                "Orb of Annulment",
                "Ancient Orb",
                "Engineer's Orb",
                "Harbinger's Orb",
                "Orb of Binding",
                "Orb of Horizons",
                "Fracturing Shard",
                "Burial Medallion",
                "Grand Eldritch Ember",
                "Grand Eldritch Ichor",
                "Greater Eldritch Ichor",
                "Scrap Metal",
                "Stacked Deck",
                "Ancient Shard",
                "Astragali",
                "Enkindling Orb",
                "Exalted Shard",
                "Greater Eldritch Ember",
                "Lesser Eldritch Ember",
                "Lesser Eldritch Ichor",
                "Orb of Scouring",
                "Orb of Unmaking",
            ],
            font_size=display_dict["uncommon_font_size"],
            minimap_size=2,
            sound="5 175",
        )
        self.template.rare_currency(
            description="Misc Currency Shards",
            class_text="Currency",
            base_text="Shard",
            font_size=display_dict["uncommon_font_size"],
            minimap_size=2,
            sound="5 175",
        )

        # Misc low importance currency.
        self.template.rare_currency(
            description="Misc Low Importance Currency - Low Level",
            base_text=[
                "Orb of Alteration",
                "Orb of Augmentation",
                "Chromatic Orb",
                "Jeweller's Orb",
                "Armourer's Scrap",
                "Blacksmith's Whetstone",
                "Glassblower's Bauble",
            ],
            area_level="<= 49",
            font_size=display_dict["default_font_size"],
        )

        self.template.notable_item(
            description="Misc Low Importance Currency",
            base_text=[
                "Chromatic Orb",
                "Jeweller's Orb",
                "Armourer's Scrap",
                "Blacksmith's Whetstone",
                "Glassblower's Bauble",
            ],
            font_size=display_dict["default_font_size"],
        )

    def league_specific(self):
        """
        Handling for league-specific items.
        """
        self.parse_subnum += 1

        self.filter_file.write("\n")
        self.filter_file.write("# ---------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - League Currency --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ---------------------------------- #\n")
        self.filter_file.write("\n")

        # Settlers of Kalguur.
        self.template.special_item(
            description="Kalguur Runes",
            base_text=[
                "Power Rune",
                "Time Rune",
                "Bounty Rune",
                "Journey Rune",
                "Mountain Rune",
                "River Rune",
                "Bound Rune",
                "Life Rune",
                "Sun Rune",
                "War Rune",
                "Rune",
            ],
        )

        # Trial of the Ancestors.
        self.template.special_item(
            description="Trial of the Ancestors",
            base_text=[
                "Omen of",
                "Tattoo of ",
            ],
        )

        # Ritual.
        self.template.special_item(
            description="Ritual",
            class_text="Corpses",
        )

        # Heist.
        self.template.special_item(
            description="Heist Classes",
            class_text=[
                "Heist Cloaks",
                "Heist Brooches",
                "Heist Gear",
                "Heist Tools",
                "Heist Target",
            ],
        )
        self.template.special_item(
            description="Heist Bases",
            base_text=[
                "Whisper-woven Cloak",
                "Hooded Cloak",
                "Foliate Brooch",
                "Enamel Brooch",
                "Burst Band",
                "Obsidian Sharpening Stone",
                "Precise Arrowhead",
                "Grandmaster Keyring",
                "Master Lockpick",
                "Regicide Disguise Kit",
                "Silkweave Sole",
                "Steel Bracers",
                "Thaumaturgical Sensing Charm",
                "Thaumaturgical Ward",
                "Thaumetic Blowtorch",
                "Thaumetic Flashpowder",
                "Azurite Flashpowder",
                "Espionage Disguise Kit",
                "Fine Lockpick",
                "Polished Sensing Charm",
                "Runed Bracers",
                "Shining Ward",
                "Skeleton Keyring",
                "Sulphur Blowtorch",
                "Winged Sole",
                "Rogue's Marker",
                "Thief's Trinket",
            ],
        )

        # Harvest.
        # Seems to be discontinued.
        # self.template.special_item(
        #     description='Harvest Classes',
        #     class_text='Harvest Seed',
        # )
        # self.template.special_item(
        #     description='Harvest Bases',
        #     base_text=[
        #         'Dedication to the Goddess', 'Facetor\'s Lens', 'Gift to the Goddess', 'Infused Engineer\'s Orb',
        #     ],
        # )

        # Delirium.
        self.template.special_item(
            description="Delerium Bases",
            base_text=["Delirium Orb", "Simulacrum Splinter", "Simulacrum"],
        )

        # Metamorph.
        self.template.special_item(
            description="Metamorph",
            base_text=[
                "Abrasive Catalyst",
                "Fertile Catalyst",
                "Imbued Catalyst",
                "Intrinsic Catalyst",
                "Prismatic Catalyst",
                "Tempering Catalyst",
                "Turbulent Catalyst",
            ],
        )

        # Blight.
        self.template.special_item(
            description="Blight",
            base_text=[
                "Amber Oil",
                "Azure Oil",
                "Black Oil",
                "Clear Oil",
                "Crimson Oil",
                "Golden Oil",
                "Opalescent Oil",
                "Sepia Oil",
                "Silver Oil",
                "Teal Oil",
                "Verdant Oil",
                "Violet Oil",
            ],
        )

        # Legion.
        self.template.special_item(
            description="Legion Classes",
            class_text="Incubator",
        )
        self.template.special_item(
            description="Legion Bases",
            base_text=[
                "Timeless Eternal Empire Splinter",
                "Timeless Karui Splinter",
                "Timeless Maraketh Splinter",
                "Timeless Templar Splinter",
                "Timeless Vaal Splinter",
            ],
            font_size=display_dict["uncommon_font_size"],
            minimap_size=2,
        )

        # Scarab.
        self.template.special_item(
            description="Scarab Items",
            class_text="Map Fragments",
            base_text="Scarab",
        )

        # Delve.
        self.template.special_item(
            description="General Delve Currency",
            class_text=[
                "Delve Socketable Currency",
                "Delve Stackable Socketable Currency",
            ],
        )
        self.template.special_item(
            description="Delve Fossils",
            class_text="Currency",
            base_text="Fossil",
        )
        self.template.special_item(
            description="Delve Resonators",
            base_text="Resonator",
        )

        # Incursion.
        self.template.special_item(
            description="Incursion Classes",
            class_text="Incursion Item",
        )
        self.template.special_item(
            description="Incursion Bases",
            base_text=[
                "Vial of Dominance",
                "Vial of Summoning",
                "Vial of Awakening",
                "Vial of the Ritual",
                "Vial of Fate",
                "Vial of Consequence",
                "Vial of Transcendence",
                "Vial of the Ghost",
                "Vial of Sacrifice",
            ],
        )
        self.template.special_item(
            description="Incursion Stone of Passage",
            base_text="Stone of Passage",
            font_size=display_dict["unique_font_size"],
            minimap_size=0,
            sound="4 300",
        )

        # Harbringer.
        self.template.special_item(
            description="Harbringer",
            class_text="Piece",
        )
        self.template.special_item(
            description="Breach",
            base_text=[
                "Blessing of Xoph",
                "Blessing of Tul",
                "Blessing of Esh",
                "Blessing of Uul-Netol",
                "Blessing of Chayula",
                "Splinter of Xoph",
                "Splinter of Tul",
                "Splinter of Esh",
                "Splinter of Uul-Netol",
                "Splinter of Chayula",
            ],
            font_size=display_dict["uncommon_font_size"],
            minimap_size=2,
        )
        self.template.special_item(
            description="Essence",
            base_text="Essence of",
            font_size=display_dict["uncommon_font_size"],
            minimap_size=2,
        )
        self.template.special_item(
            description="Essence",
            base_text="Remnant of",
            font_size=display_dict["uncommon_font_size"],
            minimap_size=2,
        )

        # OG.
        self.template.special_item(
            description="Prophecies",
            base_text="Prophecy",
            class_text="Currency",
            font_size=display_dict["uncommon_font_size"],
        )
        self.template.special_item(
            description="Perandus",
            base_text="Perandus Coin",
            font_size=display_dict["uncommon_font_size"],
        )
        self.template.special_item(
            description="Talismans",
            class_text="Amulets",
            base_text="Talisman",
        )

        # Other.
        self.template.special_item(
            description="Other/Misc Special Currency",
            base_text=[
                "Deregulation Scroll",
                "Electroshock Scroll",
                "Fragmentation Scroll",
                "Haemocombustion Scroll",
                "Specularity Scroll",
                "Time-light Scroll",
                "Imprint",
                "Unshaping Orb",
            ],
        )

    def quest_like_items(self):
        """
        Handling for quest-like items.
        """
        self.parse_subnum += 1

        self.filter_file.write("\n")
        self.filter_file.write("# ---------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Quest-like Items --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ---------------------------------- #\n")
        self.filter_file.write("\n")

        # Labyrinth classes.
        self.template.special_item(
            description="Labyrinth Classes",
            class_text=[
                "Labyrinth",
                "Labyrinth Item",
                "Labyrinth Trinket",
            ],
        )

        # Labyrinth base types.
        self.template.special_item(
            description="Labyrinth Bases",
            base_text=[
                "Key",
                "Offering to the Goddess",
                "Divine Vessel",
            ],
        )

        # Labyrinth classes.
        self.template.special_item(
            description="Quest-like Classes",
            class_text=["Incursion Items"],
        )

        # Labyrinth base types.
        self.template.special_item(
            description="Quest-like Bases",
            base_text=["Maven's"],
        )

    def currency_catchall(self):
        """
        Catch-all for general currency.
        """
        self.parse_subnum += 1

        self.filter_file.write("\n")
        self.filter_file.write("# ------------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Currency Catch-All --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ------------------------------------- #\n")
        self.filter_file.write("\n")

        self.template.common_item(
            class_text=[
                "Currency",
                "Stackable Currency",
                "Leaguestone",
            ],
        )


class PreEquipment_CurrencyParser:
    """
    Filtering for all equipment/weapon drops that should unconditionally show as currency.
    """

    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
        self.debug = debug

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# ============================================== #\n")
        self.filter_file.write("# === [{0}] - Pre-Equipment Currency Recipes === #\n".format(self.parse_num))
        self.filter_file.write("# ============================================== #\n")
        self.filter_file.write("\n")

        self.filter_file.write("# None so far.")
        self.filter_file.write("\n")
        self.filter_file.write("\n")


class PostEquipment_CurrencyParser:
    """
    Filtering for all equipment/weapons drops that should only show if other filters do not match.
    """

    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
        self.debug = debug

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# =============================================== #\n")
        self.filter_file.write("# === [{0}] - Post-Equipment Currency Recipes === #\n".format(self.parse_num))
        self.filter_file.write("# =============================================== #\n")
        self.filter_file.write("\n")

        self.parse_quality()
        self.parse_chromatic()
        self.parse_regal()
        self.parse_chaos()
        self.parse_low_level()

    def parse_quality(self):
        """
        Various "Quality Improvement Currency" recipes.
        Involves selling any single item of full 20% quality.
        Alternatively, sell any combination of items (of the same quality type) that sum up to 40% quality.
        """
        self.parse_subnum += 1

        self.filter_file.write("\n")
        self.filter_file.write("# ------------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Quality Currencies --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ------------------------------------- #\n")
        self.filter_file.write("# Involves selling any single item of full 20% quality.\n")
        self.filter_file.write(
            "# Alternatively, sell any combination of items (of the same quality type) that sum up to 40% quality.\n"
        )
        self.filter_file.write("\n")

        self.template.notable_item(quality=20)

    def parse_chromatic(self):
        """
        Chromatic orb recipe.
        Involves item of 3 or more linked slots, with at least one red, green, and blue slot.
        """
        self.parse_subnum += 1

        self.filter_file.write("\n")
        self.filter_file.write("# ----------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - RGB Linked --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ----------------------------- #\n")
        self.filter_file.write(
            "# Involves item of 3 or more linked slots, with at least one red, green, and blue slot.\n"
        )
        self.filter_file.write("\n")

        self.parse_high_level_chromatic()
        self.parse_low_level_chromatic()

    def parse_high_level_chromatic(self):
        """
        Displaying of rgb recipe at higher levels.
        """
        # 2 x 2 space item.
        self.template.currency_recipe_high_level(
            description="Linked RGB - High Level 2x2",
            item_level=">= 50",
            height="<= 2",
            width="<= 2",
            border_color=display_dict["normal"],
        )

        # 3 x 1 space item.
        self.template.currency_recipe_high_level(
            description="Linked RGB - High Level 3x1",
            item_level=">= 50",
            height="<= 3",
            width="<= 1",
            border_color=display_dict["normal"],
        )

    def parse_low_level_chromatic(self):
        """
        Displaying of rgb recipe at lower levels.
        """
        # Loop through all defense types.
        def_types = [
            "A",
            "A/Ev",
            "Ev",
            "Ev/En",
            "En",
            "En/A",
        ]
        for def_type in def_types:
            def_file = def_type.replace("/", "_")

            # Loop through all defense slots.
            def_slots = [
                "helmets",
                "chests",
                "gloves",
                "boots",
            ]

            for def_slot in def_slots:
                slot_list = []
                with open("resources/data/equipment/{0}/{1}.json".format(def_file, def_slot), "r") as json_file:
                    # Create boot section header.

                    # Loop through all items in json.
                    json_data = json.load(json_file)
                    for item in json_data:
                        # Parse item.
                        slot_list.append(item["Name"])

                # Use list to parse item.
                self.parse_def_slot_chromatic(def_type, def_slot, slot_list)

    def parse_def_slot_chromatic(self, def_type, def_slot, item_set):
        """
        Handles filtering for linked RGB version of def type slot.
        :param def_type: Defense type of the item.
        :param def_slot: Slot for item.
        :param item: The def type set to parse.
        """
        # Create item string.
        item_set_list = []
        for item in item_set:
            item_set_list.append("{0}".format(item))

        self.template.currency_recipe_low_level(
            description="Linked RGB - Low Level, {0} {1}".format(def_type, def_slot.title()),
            base_text=item_set_list,
            item_level="< 50",
            socket_group='"RGB"',
        )

    def parse_regal(self):
        """
        Regal Orb recipe.
        Involves getting a rare item for each slot, all item level 75 or above.
        """
        self.parse_subnum += 1

        self.filter_file.write("\n")
        self.filter_file.write("# ---------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Regal Orb --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ---------------------------- #\n")
        self.filter_file.write("# Involves getting a rare item for each slot, with all items level 75 or above.\n")
        self.filter_file.write("\n")

        # Weapon Slots.
        self.template.currency_recipe_high_level(
            description="Prioritize Small Weapons",
            item_level=">= 75",
            rarity="Rare",
            height="<= 3",
            width="<= 1",
        )

        # Gear Slots.
        self.template.currency_recipe_high_level(
            description="Gear Slots",
            class_text=[
                "Helmets",
                "Body Armours",
                "Gloves",
                "Boots",
                "Ring",
                "Belt",
                "Amulet",
            ],
            item_level=">= 75",
            rarity="Rare",
        )

    def parse_chaos(self):
        """
        Chaos Orb recipe.
        Involves getting a rare item for each slot, all item level 60 to 74 or above.
        """
        self.parse_subnum += 1

        self.filter_file.write("\n")
        self.filter_file.write("# ---------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Chaos Orb --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ---------------------------- #\n")
        self.filter_file.write("# Involves getting a rare item for each slot, with all items level 60 to 74.\n")
        self.filter_file.write("\n")

        # Weapon slots.
        self.template.currency_recipe_high_level(
            description="Prioritize Small Weapons",
            item_level=">= 65",
            rarity="Rare",
            height="<= 3",
            width="<= 1",
        )

        # Gear Slots.
        self.template.currency_recipe_high_level(
            description="Gear Slots",
            class_text=[
                "Helmets",
                "Body Armours",
                "Gloves",
                "Boots",
                "Ring",
                "Belt",
                "Amulet",
            ],
            item_level=">= 65",
            rarity="Rare",
        )

    def parse_low_level(self):
        """
        General items that can be good to pick up early game, just to sell.
        """
        self.parse_subnum += 1

        self.filter_file.write("\n")
        self.filter_file.write("# ------------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Low Level Currency --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ------------------------------------- #\n")
        self.filter_file.write("# General items that can be good to sell early game.\n")
        self.filter_file.write("\n")

        # Orb of Alchemy, 2x2.
        self.template.currency_recipe_low_level(
            description="Chance at Orb of Alchemy - 2x2 or smaller",
            item_level="<= 55",
            rarity="Rare",
            width="<= 2",
            height="<= 2",
        )

        # Orb of Alchemy, 3x1.
        self.template.currency_recipe_low_level(
            description="Chance at Orb of Alchemy - 3x1 or smaller",
            item_level="<= 55",
            rarity="Rare",
            width="<= 3",
            height="<= 1",
        )

        # Orb of Transmutation, 2x2.
        self.template.currency_recipe_low_level(
            description="Chance at Orb of Transmutation - 2x2 or smaller",
            item_level="<= 44",
            rarity="Magic",
            width="<= 2",
            height="<= 2",
            border_color=display_dict["uncommon"],
        )

        # Orb of Transmutation, 3x1.
        self.template.currency_recipe_low_level(
            description="Chance at Orb of Transmutation - 3x1 or smaller",
            item_level="<= 44",
            rarity="Magic",
            width="<= 3",
            height="<= 1",
            border_color=display_dict["uncommon"],
        )
