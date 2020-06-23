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
    def __init__(self, filter_file, parse_num, defense_types, debug=False):
        self.filter_file = filter_file
        self.defense_types = defense_types
        self.parse_num = str(parse_num).zfill(2)
        self.parse_subnum = 0
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ======================= #\n')
        self.filter_file.write('# === [{0}] - Currency === #\n'.format(self.parse_num))
        self.filter_file.write('# ======================= #\n')
        self.filter_file.write('\n')


class PreEquipment_CurrencyParser():
    """
    Filtering for all equipment/weapon drops that should unconditionally show as currency.
    """
    def __init__(self, filter_file, parse_num, defense_types, debug=False):
        self.filter_file = filter_file
        self.defense_types = defense_types
        self.parse_num = str(parse_num).zfill(2)
        self.parse_subnum = 0
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ============================================= #\n')
        self.filter_file.write('# === [{0}] - Pre-Equipment Currency Recipes === #\n'.format(self.parse_num))
        self.filter_file.write('# ============================================= #\n')
        self.filter_file.write('\n')

        # Unique Items.
        self.parse_subnum += 1
        self.parse_uniques()

        # 5 or 6 slot items.
        self.parse_subnum += 1
        self.parse_high_slot()

    def parse_uniques(self):
        """
        Filter parsing for unique items.
        """
        parse_subnum = str(self.parse_subnum).zfill(2)

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Unique Items --- #\n'.format(self.parse_num, parse_subnum))
        self.filter_file.write('# ------------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('Show\n')
        self.filter_file.write('    Rarity = Unique\n')
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(display_dict['unique_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['unique']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['unique_text_color']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['unique_font_size']))
        self.filter_file.write('    PlayAlertSound 1 300\n')
        self.filter_file.write('    MinimapIcon 0 {0} {1}\n'.format(display_dict['minimap_icon_unique'], display_dict['minimap_color_unique']))
        self.filter_file.write('    PlayerEffect {0}\n'.format(display_dict['minimap_color_unique']))

        self.filter_file.write('\n')

    def parse_high_slot(self):
        """
        Filter parsing for items with 5 or 6 slots.
        """
        parse_subnum = str(self.parse_subnum).zfill(2)

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - High Slot Items --- #\n'.format(self.parse_num, parse_subnum))
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('\n')
        self.filter_file.write('# --------------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}.01] - 6-Link Slot Items --- #\n'.format(self.parse_num, parse_subnum))
        self.filter_file.write('# --------------------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('# Rare Type.\n')
        self.filter_file.write('Show\n')
        self.filter_file.write('    Rarity = Rare\n')
        self.filter_file.write('    LinkedSockets = 6\n')
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['rare']))
        self.parse_high_slot_filter()

        self.filter_file.write('# Uncommon Type.\n')
        self.filter_file.write('Show\n')
        self.filter_file.write('    Rarity = Magic\n')
        self.filter_file.write('    LinkedSockets = 6\n')
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['magic']))
        self.parse_high_slot_filter()

        self.filter_file.write('# Base Type.\n')
        self.filter_file.write('Show\n')
        self.filter_file.write('    Rarity = Normal\n')
        self.filter_file.write('    LinkedSockets = 6\n')
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['normal']))
        self.parse_high_slot_filter()

        self.filter_file.write('\n')
        self.filter_file.write('# --------------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}.02] - 5-Link Slot Items --- #\n'.format(self.parse_num, parse_subnum))
        self.filter_file.write('# --------------------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('# Rare Type.\n')
        self.filter_file.write('Show\n')
        self.filter_file.write('    Rarity = Rare\n')
        self.filter_file.write('    LinkedSockets = 5\n')
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['rare']))
        self.parse_high_slot_filter()

        self.filter_file.write('# Uncommon Type.\n')
        self.filter_file.write('Show\n')
        self.filter_file.write('    Rarity = Magic\n')
        self.filter_file.write('    LinkedSockets = 5\n')
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['magic']))
        self.parse_high_slot_filter()

        self.filter_file.write('# Base Type.\n')
        self.filter_file.write('Show\n')
        self.filter_file.write('    Rarity = Normal\n')
        self.filter_file.write('    LinkedSockets = 5\n')
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['normal']))
        self.parse_high_slot_filter()

    def parse_high_slot_filter(self):
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['important_font_size']))
        self.filter_file.write('    PlayAlertSound 1 100\n')
        self.filter_file.write('    MinimapIcon 1 {0} {1}\n'.format(display_dict['minimap_icon_slots'], display_dict['minimap_color_slots']))
        self.filter_file.write('    PlayerEffect {0}\n'.format(display_dict['minimap_color_slots']))
        self.filter_file.write('\n')


class PostEquipment_CurrencyParser():
    """
    Filtering for all equipment/weapons drops that should only show if other filters do not match.
    """
    def __init__(self, filter_file, parse_num, defense_types, debug=False):
        self.filter_file = filter_file
        self.defense_types = defense_types
        self.parse_num = str(parse_num).zfill(2)
        self.parse_subnum = 0
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ============================================== #\n')
        self.filter_file.write('# === [{0}] - Post-Equipment Currency Recipes === #\n'.format(self.parse_num))
        self.filter_file.write('# ============================================== #\n')
        self.filter_file.write('\n')

        self.parse_armor_rgb()

    def parse_armor_rgb(self):
        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - RGB Linked --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('\n')

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
                self.parse_def_slot_rgb(def_type, def_slot, slot_list)

    def parse_def_slot_rgb(self, def_type, def_slot, item_set):
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

        self.filter_file.write('# Linked RGB {0} {1}.\n'.format(def_type, def_slot.title()))
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType {0}\n'.format(item_set_string))
        self.filter_file.write('    SocketGroup "RGB"\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0} 100\n'.format(display_dict[def_type]))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['normal']))
        self.filter_file.write('    SetTextColor {0} 100\n'.format(display_dict['text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['min_font_size']))
        self.filter_file.write('\n')
