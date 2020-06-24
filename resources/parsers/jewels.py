"""
Filter creation for jewels.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict, filter_dict


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class JewelParser():
    """
    Filtering for all jewel drops.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ====================== #\n')
        self.filter_file.write('# === [{0}] - Jewels === #\n'.format(self.parse_num))
        self.filter_file.write('# ====================== #\n')
        self.filter_file.write('\n')

        self.parse_standard()
        self.parse_abyss()
        self.parse_cluster()

    def parse_standard(self):
        """"""
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Standard Jewels --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('# Standard Jewels.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType "Cobalt Jewel" "Crimson Jewel" "Viridian Jewel"\n')

        # Values to set if filter match is found.
        self.filter_file.write('    BorderColor {0}\n'.format(display_dict['normal']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['rare_font_size']))
        self.filter_file.write('    PlayAlertSound 4 175\n')
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_color_special'],
            display_dict['minimap_icon_jewel']
        ))
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_special']))
        self.filter_file.write('\n')

    def parse_abyss(self):
        """"""
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Abyss Jewels --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ------------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('# Abyss Jewels.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Abyss Jewel"\n')

        # Values to set if filter match is found.
        self.filter_file.write('    BorderColor {0}\n'.format(display_dict['league_border']))
        self.filter_file.write('    SetTextColor {0}\n'.format(display_dict['league_text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['rare_font_size']))
        self.filter_file.write('    PlayAlertSound 4 175\n')
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_color_special'],
            display_dict['minimap_icon_jewel']
        ))
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_special']))
        self.filter_file.write('\n')

    def parse_cluster(self):
        """"""
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# --------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Cluster Jewels --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# --------------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('# Cluster Jewels.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType "Cluster Jewel"\n')

        # Values to set if filter match is found.
        self.filter_file.write('    BorderColor {0}\n'.format(display_dict['league_border']))
        self.filter_file.write('    SetTextColor {0}\n'.format(display_dict['league_text']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['rare_font_size']))
        self.filter_file.write('    PlayAlertSound 4 175\n')
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_color_special'],
            display_dict['minimap_icon_jewel']
        ))
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_special']))
        self.filter_file.write('\n')
