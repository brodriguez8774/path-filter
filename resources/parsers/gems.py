"""
Filter creation for gems.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict, filter_dict


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class GemParser():
    """
    Filtering for all gem drops.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ==================== #\n')
        self.filter_file.write('# === [{0}] - Gems === #\n'.format(self.parse_num))
        self.filter_file.write('# ==================== #\n')
        self.filter_file.write('\n')

        self.rare_gems()
        self.high_quality_gems()
        self.vaal_gems()

    def rare_gems(self):
        """
        Handling for rare gems that cannot be purchased.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Rare Gems --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Gem"\n')
        self.filter_file.write('    BaseType "Empower" "Enhance" "Enlighten" "Portal"\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['unique']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['important_font_size']))
        self.filter_file.write('    MinimapIcon 0 {0} {1}\n'.format(
            display_dict['minimap_icon_special'],
            display_dict['minimap_color_special'],
        ))
        self.filter_file.write('    PlayEffect {0}'.format(display_dict['minimap_color_special']))
        self.filter_file.write('\n')

    def high_quality_gems(self):
        """
        Handling for high quality gems.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------------------ #\n')
        self.filter_file.write('# --- [{0}.{1}] - High Quality Gems --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ------------------------------------ #\n')
        self.filter_file.write('\n')

        # High quality between 15 and 20%.
        self.filter_file.write('# High quality gems [15 - 20]%.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Gem"\n')
        self.filter_file.write('    Quality >= 15\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['normal']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['important_font_size']))
        self.filter_file.write('\n')

        # High quality between 10 and 15%.
        self.filter_file.write('# High quality gems [10 - 15]%.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Gem"\n')
        self.filter_file.write('    Quality >= 10\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['normal']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['uncommon_font_size']))
        self.filter_file.write('\n')

        # High quality between 5 and 10%.
        self.filter_file.write('# High quality gems [5 - 10]%.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Gem"\n')
        self.filter_file.write('    Quality >= 5\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['normal']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['default_font_size']))
        self.filter_file.write('\n')

    def vaal_gems(self):
        """
        Handling for vaal gems.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Vaal Gems --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Gem"\n')
        self.filter_file.write('    BaseType "Vaal"\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(display_dict['normal']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['default_font_size']))
        self.filter_file.write('    MinimapIcon 0 {0} {1}\n'.format(
            display_dict['minimap_icon_special'],
            display_dict['minimap_color_special'],
        ))
        self.filter_file.write('    PlayEffect {0}'.format(display_dict['minimap_color_special']))
        self.filter_file.write('\n')
