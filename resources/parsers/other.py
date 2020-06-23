"""
Filter creation for all other items.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict, filter_dict


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class UniqueParser():
    """
    Filtering for all uniques.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(2)
        self.parse_subnum = 0
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# =========================== #\n')
        self.filter_file.write('# === [{0}] - Unique Items === #\n'.format(self.parse_num))
        self.filter_file.write('# =========================== #\n')
        self.filter_file.write('\n')

        # Unique Items.
        self.parse_subnum += 1
        self.parse_uniques()

    def parse_uniques(self):
        """
        Filter parsing for unique items.
        """
        parse_subnum = str(self.parse_subnum).zfill(2)

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


class NotableGearParser():
    """
    Filtering for all extra-notable equipment drops that should show unconditionally.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(2)
        self.parse_subnum = 0
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ============================ #\n')
        self.filter_file.write('# === [{0}] - Notable Gear  === #\n'.format(self.parse_num))
        self.filter_file.write('# ============================ #\n')
        self.filter_file.write('\n')

        # 5 or 6 slot items.
        self.parse_subnum += 1
        self.parse_high_slot()

    def parse_high_slot(self):
        """
        Filter parsing for items with 5 or 6 slots.
        """
        parse_subnum = str(self.parse_subnum).zfill(2)

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# --------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - High Slot Items --- #\n'.format(self.parse_num, parse_subnum))
        self.filter_file.write('# --------------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('\n')
        self.filter_file.write('# -------------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}.01] - 6-Link Slot Items --- #\n'.format(self.parse_num, parse_subnum))
        self.filter_file.write('# -------------------------------------- #\n')
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
        self.filter_file.write('# -------------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}.02] - 5-Link Slot Items --- #\n'.format(self.parse_num, parse_subnum))
        self.filter_file.write('# -------------------------------------- #\n')
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
