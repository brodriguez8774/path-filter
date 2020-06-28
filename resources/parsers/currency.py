"""
Filter creation for currency and currency-recipe items.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict, filter_dict


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class CurrencyParser():
    """
    Filtering for all currency item drops.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ======================== #\n')
        self.filter_file.write('# === [{0}] - Currency === #\n'.format(self.parse_num))
        self.filter_file.write('# ======================== #\n')
        self.filter_file.write('\n')

        self.general_currency()
        self.league_specific()
        self.labyrinth_items()
        self.currency_catchall()

    def general_currency(self):
        """
        Handling for general currency items.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ----------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - General Currency --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ----------------------------------- #\n')
        self.filter_file.write('\n')

        # Mirror of Kalandra.
        self.create_general_rule(
            'Mirror of Kalandra',
            '"Mirror of Kalandra"',
            background_color=display_dict['unique_background'],
            border_color=None,
            text_color=display_dict['unique_text_color'],
            font_size=display_dict['unique_font_size'],
            sound='ShMirror 300',
            minimap='0 {0} {1}'.format(display_dict['minimap_color_unique'], display_dict['minimap_icon_currency']),
            playeffect=display_dict['minimap_color_unique']
        )

        # Exalted Orb.
        self.create_general_rule(
            'Exalted Orb',
            '"Exalted Orb"',
            background_color=None,
            border_color=None,
            text_color=display_dict['currency_text'],
            font_size=display_dict['rare_font_size'],
            sound='ShExalted 300',
            minimap='0 {0} {1}'.format(display_dict['minimap_color_currency'], display_dict['minimap_icon_currency']),
            playeffect=display_dict['minimap_color_currency'],
        )

        # Divine Orb.
        self.create_general_rule(
            'Divine Orb',
            '"Divine Orb"',
            background_color=None,
            border_color=None,
            text_color=display_dict['currency_text'],
            font_size=display_dict['rare_font_size'],
            sound='ShDivine 300',
            minimap='0 {0} {1}'.format(display_dict['minimap_color_currency'], display_dict['minimap_icon_currency']),
            playeffect=display_dict['minimap_color_currency'],
        )

        # Regal Orb.
        self.create_general_rule(
            'Regal Orb',
            '"Regal Orb"',
            background_color=None,
            border_color=None,
            text_color=display_dict['currency_text'],
            font_size=display_dict['rare_font_size'],
            sound='ShRegal 175',
            minimap='0 {0} {1}'.format(display_dict['minimap_color_currency'], display_dict['minimap_icon_currency']),
            playeffect=display_dict['minimap_color_currency'],
        )

        # Blessed Orb.
        self.create_general_rule(
            'Blessed Orb',
            '"Blessed Orb"',
            background_color=None,
            border_color=None,
            text_color=display_dict['currency_text'],
            font_size=display_dict['uncommon_font_size'],
            sound='ShBlessed 175',
            minimap='0 {0} {1}'.format(display_dict['minimap_color_currency'], display_dict['minimap_icon_currency']),
            playeffect=display_dict['minimap_color_currency'],
        )

        # Vaal Orb.
        self.create_general_rule(
            'Vaal Orb',
            '"Vaal Orb"',
            background_color=None,
            border_color=None,
            text_color=display_dict['currency_text'],
            font_size=display_dict['uncommon_font_size'],
            sound='ShVaal 175',
            minimap='1 {0} {1}'.format(display_dict['minimap_color_currency'], display_dict['minimap_icon_currency']),
            playeffect=display_dict['minimap_color_currency'],
        )

        # Chaos Orb.
        self.create_general_rule(
            'Chaos Orb',
            '"Chaos Orb"',
            background_color=None,
            border_color=None,
            text_color=display_dict['currency_text'],
            font_size=display_dict['uncommon_font_size'],
            sound='ShChaos 175',
            minimap='1 {0} {1}'.format(display_dict['minimap_color_currency'], display_dict['minimap_icon_currency']),
            playeffect=display_dict['minimap_color_currency'],
        )

        # Orb of Fusing.
        self.create_general_rule(
            'Orb of Fusing',
            '"Orb of Fusing"',
            background_color=None,
            border_color=None,
            text_color=display_dict['currency_text'],
            font_size=display_dict['default_font_size'],
            sound='ShFusing 175',
            minimap='2 {0} {1}'.format(display_dict['minimap_color_currency'], display_dict['minimap_icon_currency']),
            playeffect=display_dict['minimap_color_currency'],
        )

        # Orb of Alchemy.
        self.create_general_rule(
            'Orb of Alchemy',
            '"Orb of Alchemy"',
            background_color=None,
            border_color=None,
            text_color=display_dict['currency_text'],
            font_size=display_dict['default_font_size'],
            sound='ShAlchemy 175',
            minimap='2 {0} {1}'.format(display_dict['minimap_color_currency'], display_dict['minimap_icon_currency']),
            playeffect=display_dict['minimap_color_currency'],
        )

        # Divination Cards.
        self.create_general_rule(
            'Divination Cards',
            '"Card" "Stacked Deck"',
            background_color=None,
            border_color=None,
            text_color=display_dict['currency_text'],
            font_size=display_dict['default_font_size'],
            sound='9 175',
            minimap=None,
            playeffect=None,
        )

        # Misc important currency.
        self.create_general_rule(
            'Misc important currency',
            '"Gemcutter\'s Prism" "Cartographer\'s Chisel" "Silver Coin" "Orb of Scouring"  "Orb of Regret" "Stone of Passage" "Eternal Orb" "Master Cartographer\'s Seal" "Albino Rhoa Feather"',
            background_color=None,
            border_color=None,
            text_color=display_dict['currency_text'],
            font_size=display_dict['default_font_size'],
            sound='4 175',
            minimap='0 {0} {1}'.format(display_dict['minimap_color_currency'], display_dict['minimap_icon_currency']),
            playeffect=display_dict['minimap_color_currency'],
        )

        # Low level important currency.
        self.create_general_rule(
            'Low level important currency',
            '"Orb of Alteration" "Chromatic Orb" "Jeweller\'s Orb" "Armourer\'s Scrap" "Blacksmith\'s Whetstone" "Glassblower\'s Bauble" "Orb of Chance"',
            background_color=None,
            border_color=None,
            text_color=display_dict['currency_text'],
            font_size=display_dict['default_font_size'],
            sound=None,
            minimap='0 {0} {1}'.format(display_dict['minimap_color_currency'], display_dict['minimap_icon_currency']),
        )

    def create_general_rule(self, description_text, base_text, background_color=None, border_color=None,
                            text_color=None, font_size=None, sound=None, minimap=None, playeffect=None):
        """"""
        self.filter_file.write('# {0}.\n'.format(description_text))
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType {0}\n'.format(base_text))

        # Values to set if filter match is found.
        if background_color is not None:
            self.filter_file.write('    SetBackgroundColor {0}\n'.format(background_color))
        if border_color is not None:
            self.filter_file.write('    SetBorderColor {0}\n'.format(border_color))
        if text_color is not None:
            self.filter_file.write('    SetTextColor {0}\n'.format(text_color))
        if font_size is not None:
            self.filter_file.write('    SetFontSize {0}\n'.format(font_size))
        if sound is not None:
            self.filter_file.write('    PlayAlertSound {0}\n'.format(sound))
        if minimap is not None:
            self.filter_file.write('    MinimapIcon {0}\n'.format(minimap))
        if playeffect is not None:
            self.filter_file.write('    PlayEffect {0}\n'.format(playeffect))
        self.filter_file.write('\n')

    def league_specific(self):
        """
        Handling for league-specific items.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - League Currency --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('\n')

        self.create_league_rule('Harvest Classes', class_text='"Harvest Seed"')
        self.create_league_rule(
            'Harvest Bases',
            base_text='"Dedication to the Goddess" "Facetor\'s Lens" "Gift to the Goddess" "Infused Engineer\'s Orb"'
        )
        self.create_league_rule('Delerium Bases', base_text='"Delirium Orb" "Simulacrum Splinter" "Simulacrum"')
        self.create_league_rule(
            'Metamorph',
            base_text='"Abrasive Catalyst" "Fertile Catalyst" "Imbued Catalyst" "Intrinsic Catalyst" "Prismatic '
            'Catalyst" "Tempering Catalyst" "Turbulent Catalyst"'
        )
        self.create_league_rule(
            'Blight',
            base_text='"Amber Oil" "Azure Oil" "Black Oil" "Clear Oil" "Crimson Oil" "Golden Oil" "Opalescent Oil" '
            '"Sepia Oil" "Silver Oil" "Teal Oil" "Verdant Oil" "Violet Oil"'
        )
        self.create_league_rule('Legion Classes', class_text='"Incubator"')
        self.create_league_rule(
            'Legion Bases',
            base_text='"Timeless Eternal Empire Splinter" "Timeless Karui Splinter" "Timeless Maraketh Splinter" '
            '"Timeless Templar Splinter" "Timeless Vaal Splinter"'
        )
        self.create_league_rule('Delve', class_text='"Delve Socketable Currency"')
        self.create_league_rule('Incursion Classes', class_text='"Incursion Item"')
        self.create_league_rule(
            'Incursion Bases',
            base_text='"Vial of Dominance" "Vial of Summoning" "Vial of Awakening" "Vial of the Ritual" "Vial of'
            ' Fate" "Vial of Consequence" "Vial of Transcendence" "Vial of the Ghost" "Vial of Sacrifice"'
        )
        self.create_league_rule('Harbringer', class_text='"Piece"')
        self.create_league_rule(
            'Breach',
            base_text='"Blessing of Xoph" "Blessing of Tul" "Blessing of Esh" "Blessing of Uul-Netol" "Blessing of '
            'Chayula" "Splinter of Xoph" "Splinter of Tul" "Splinter of Esh" "Splinter of Uul-Netol" "Splinter of '
            'Chayula"'
        )
        self.create_league_rule('Prophecy', base_text='"Silver Coin"')
        self.create_league_rule('Essence', base_text='"Essence of"')
        self.create_league_rule('Perandus', base_text='"Perandus Coin"')

    def create_league_rule(self, description_text, *args, class_text=None, base_text=None, **kwargs):
        """
        Define filter for league item(s).
        :param description_text: Descriptive comment text for league.
        :param item_type: BaseType or Class.
        :param type_text: Text for league item.
        """
        if class_text is None and base_text is None:
            raise ValueError('Either class_text or base_text required for league currency.')

        self.filter_file.write('# {0}.\n'.format(description_text))
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        if class_text is not None:
            self.filter_file.write('    Class {0}\n'.format(class_text))
        if base_text is not None:
            self.filter_file.write('    BaseType {0}\n'.format(base_text))

        # Values to set if filter match is found.
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['league_border']))
        self.filter_file.write('    SetTextColor {0}\n'.format(display_dict['league_text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['rare_font_size']))
        self.filter_file.write('    PlayAlertSound 4 175\n')
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_color_special'],
            display_dict['minimap_icon_special']
        ))
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_special']))
        self.filter_file.write('\n')

    def labyrinth_items(self):
        """
        Handling for labyrinth-specific items.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Labyrinth Items --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Labyrinth" "Labyrinth Item" "Labyrinth Trinket" "Key" "Offering to the Goddess" "Divine Vessel"\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['uncommon_font_size']))
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_color_currency'],
            display_dict['minimap_icon_special'],
        ))
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_currency']))
        self.filter_file.write('\n')

    def currency_catchall(self):
        """
        Catch-all for general currency.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Currency Catch-All --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ------------------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Currency" "Stackable Currency" "Quest" "Quest Items" "Leaguestone"\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['default_font_size']))
        self.filter_file.write('\n')


class PreEquipment_CurrencyParser():
    """
    Filtering for all equipment/weapon drops that should unconditionally show as currency.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ============================================== #\n')
        self.filter_file.write('# === [{0}] - Pre-Equipment Currency Recipes === #\n'.format(self.parse_num))
        self.filter_file.write('# ============================================== #\n')
        self.filter_file.write('\n')


class PostEquipment_CurrencyParser():
    """
    Filtering for all equipment/weapons drops that should only show if other filters do not match.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# =============================================== #\n')
        self.filter_file.write('# === [{0}] - Post-Equipment Currency Recipes === #\n'.format(self.parse_num))
        self.filter_file.write('# =============================================== #\n')
        self.filter_file.write('\n')

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

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Quality Currencies --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ------------------------------------- #\n')
        self.filter_file.write('# Involves selling any single item of full 20% quality.\n')
        self.filter_file.write('# Alternatively, sell any combination of items (of the same quality type) that sum up to 40% quality.\n')
        self.filter_file.write('\n')

        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Quality = 20\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['normal']))
        self.filter_file.write('    SetTextColor {0} 0\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')

    def parse_chromatic(self):
        """
        Chromatic orb recipe.
        Involves item of 3 or more linked slots, with at least one red, green, and blue slot.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ----------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - RGB Linked --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ----------------------------- #\n')
        self.filter_file.write('# Involves item of 3 or more linked slots, with at least one red, green, and blue slot.\n')
        self.filter_file.write('\n')

        self.parse_high_level_chromatic()
        self.parse_low_level_chromatic()

    def parse_high_level_chromatic(self):
        """
        Displaying of rgb recipe at higher levels.
        """
        # 2 x 2 space item.
        self.filter_file.write('# Linked RGB - High Level 2x2.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    ItemLevel >= 50\n')
        self.filter_file.write('    SocketGroup "RGB"\n')
        self.filter_file.write('    Height 2\n')
        self.filter_file.write('    Width 2\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['normal']))
        self.filter_file.write('    SetTextColor {0} 0\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')

        # 3 x 1 space item.
        self.filter_file.write('# Linked RGB - High Level 3x1.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    ItemLevel >= 50\n')
        self.filter_file.write('    SocketGroup "RGB"\n')
        self.filter_file.write('    Height 3\n')
        self.filter_file.write('    Width 1\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['normal']))
        self.filter_file.write('    SetTextColor {0} 0\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')

    def parse_low_level_chromatic(self):
        """
        Displaying of rgb recipe at lower levels.
        """
        # Loop through all defense types.
        def_types = ['A', 'A/Ev', 'Ev', 'Ev/En', 'En', 'En/A']
        for def_type in def_types:
            def_file = def_type.replace('/', '_')

            # Loop through all defense slots.
            def_slots = ['helmets', 'chests', 'gloves', 'boots']

            for def_slot in def_slots:
                slot_list = []
                with open('resources/data/equipment/{0}/{1}.json'.format(def_file, def_slot), 'r') as json_file:
                    # Create boot section header.

                    # Loop through all items in json.
                    json_data = json.load(json_file)
                    for item in json_data:
                        # Parse item.
                        slot_list.append(item['Name'])

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
        item_set_string = None
        for item in item_set:
            if item_set_string is None:
                item_set_string = '"{0}"'.format(item)
            else:
                item_set_string += ' "{0}"'.format(item)

        self.filter_file.write('# Linked RGB - Low Level, {0} {1}.\n'.format(def_type, def_slot.title()))
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType {0}\n'.format(item_set_string))
        self.filter_file.write('    ItemLevel < 50\n')
        self.filter_file.write('    SocketGroup "RGB"\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict[def_type]))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['normal']))
        self.filter_file.write('    SetTextColor {0} 0\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')

    def parse_regal(self):
        """
        Regal Orb recipe.
        Involves getting a rare item for each slot, all item level 75 or above.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Regal Orb --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('# Involves getting a rare item for each slot, with all items level 75 or above.\n')
        self.filter_file.write('\n')

        # Weapon Slots.
        self.filter_file.write('# Prioritize Small Weapons.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    ItemLevel >= 75\n')
        self.filter_file.write('    Rarity = Rare\n')
        self.filter_file.write('    Height = 3\n')
        self.filter_file.write('    Width = 1\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['rare']))
        self.filter_file.write('    SetTextColor {0} 0\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')

        # Gear Slots.
        self.filter_file.write('# Gear Slots.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Helmets" "Body Armours" "Gloves" "Boots" "Ring" "Belt" "Amulet"\n')
        self.filter_file.write('    ItemLevel >= 75\n')
        self.filter_file.write('    Rarity = Rare\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['rare']))
        self.filter_file.write('    SetTextColor {0} 0\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')

    def parse_chaos(self):
        """
        Chaos Orb recipe.
        Involves getting a rare item for each slot, all item level 60 to 74 or above.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Chaos Orb --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('# Involves getting a rare item for each slot, with all items level 60 to 74.\n')
        self.filter_file.write('\n')

        # Weapon slots.
        self.filter_file.write('# Prioritize Small Weapons.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    ItemLevel >= 65\n')
        self.filter_file.write('    Rarity = Rare\n')
        self.filter_file.write('    Height = 3\n')
        self.filter_file.write('    Width = 1\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['rare']))
        self.filter_file.write('    SetTextColor {0} 0\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')

        # Gear slots.
        self.filter_file.write('# Gear Slots.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Helmets" "Body Armours" "Gloves" "Boots" "Ring" "Belt" "Amulet"\n')
        self.filter_file.write('    ItemLevel >= 65\n')
        self.filter_file.write('    Rarity = Rare\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['rare']))
        self.filter_file.write('    SetTextColor {0} 0\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')

    def parse_low_level(self):
        """
        General items that can be good to pick up early game, just to sell.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Low Level Currency --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ------------------------------------- #\n')
        self.filter_file.write('# General items that can be good to sell early game.\n')
        self.filter_file.write('\n')

        # Orb of Alchemy, 2x2.
        self.filter_file.write('# Chance at Orb of Alchemy - 2x2 or smaller.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    ItemLevel <= 40\n')
        self.filter_file.write('    Rarity = Rare\n')
        self.filter_file.write('    Width <= 2\n')
        self.filter_file.write('    Height <= 2\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['rare']))
        self.filter_file.write('    SetTextColor {0} 0\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')

        # Orb of Alchemy, 3x1.
        self.filter_file.write('# Chance at Orb of Alchemy - 3x1 or smaller.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    ItemLevel <= 40\n')
        self.filter_file.write('    Rarity = Rare\n')
        self.filter_file.write('    Width <= 3\n')
        self.filter_file.write('    Height <= 1\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['rare']))
        self.filter_file.write('    SetTextColor {0} 0\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')

        # Orb of Transmutation, 2x2.
        self.filter_file.write('# Chance at Orb of Transmutation - 2x2 or smaller.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    ItemLevel <= 20\n')
        self.filter_file.write('    Rarity = Magic\n')
        self.filter_file.write('    Width <= 2\n')
        self.filter_file.write('    Height <= 2\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['magic']))
        self.filter_file.write('    SetTextColor {0} 0\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')

        # Orb of Transmutation, 3x1.
        self.filter_file.write('# Chance at Orb of Transmutation - 3x1 or smaller.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    ItemLevel <= 20\n')
        self.filter_file.write('    Rarity = Magic\n')
        self.filter_file.write('    Width <= 3\n')
        self.filter_file.write('    Height <= 1\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['magic']))
        self.filter_file.write('    SetTextColor {0} 0\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')
