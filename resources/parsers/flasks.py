"""
Filter creation for flasks.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict, filter_dict


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class FlaskParser():
    """
    Filtering for all flask drops.
    """
    def __init__(self, filter_file, parse_num, show_hybrid_flasks, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.hybrid_flasks = show_hybrid_flasks
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ====================== #\n')
        self.filter_file.write('# === [{0}] - Flasks === #\n'.format(self.parse_num))
        self.filter_file.write('# ====================== #\n')
        self.filter_file.write('\n')

        self.show_high_quality_flasks()
        self.show_life_flasks()
        self.show_mana_flasks()
        if self.hybrid_flasks:
            self.show_hybrid_flasks()
        self.show_utility_flasks()

    def parse_flask(self, flask):
        """
        Handles filter rule definition of flasks.
        :param flask: Flask to create rules for.
        """
        if flask['Class'] in ['Life', 'Mana']:
            drop_level = flask['DropLevel'] + 6
        elif flask['Class'] == 'Hybrid':
            drop_level = flask['DropLevel'] + 10
        elif flask['Name'] == 'Quicksilver Flask':
            drop_level = 100
        else:
            drop_level = 70

        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType "{0}"\n'.format(flask['Name']))
        self.filter_file.write('    ItemLevel <= {0}\n'.format(drop_level))

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['default_font_size']))
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_icon_flasks'],
            display_dict['minimap_color_flasks'],
        ))
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_flasks']))
        self.filter_file.write('\n')

    def show_high_quality_flasks(self):
        """
        Handling for high quality flasks.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# -------------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - High Quality Flasks --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# -------------------------------------- #\n')
        self.filter_file.write('\n')

        # High quality between 15 and 20%.
        self.filter_file.write('# High quality flasks [15 - 20]%.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Life Flasks" "Mana Flasks" "Hybrid Flasks" "Utility Flasks" "Critical Utility Flasks"\n')
        self.filter_file.write('    Quality >= 15\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['important_font_size']))
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_icon_flasks'],
            display_dict['minimap_color_flasks'],
        ))
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_flasks']))
        self.filter_file.write('\n')

        # High quality between 10 and 15%.
        self.filter_file.write('# High quality flasks [10 - 15]%.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Life Flasks" "Mana Flasks" "Hybrid Flasks" "Utility Flasks" "Critical Utility Flasks"\n')
        self.filter_file.write('    Quality >= 10\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['uncommon_font_size']))
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_icon_flasks'],
            display_dict['minimap_color_flasks'],
        ))
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_flasks']))
        self.filter_file.write('\n')

        # High quality between 5 and 10%.
        self.filter_file.write('# High quality flasks [5 - 10]%.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    Class "Life Flasks" "Mana Flasks" "Hybrid Flasks" "Utility Flasks" "Critical Utility Flasks"\n')
        self.filter_file.write('    Quality >= 5\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(display_dict['standard_background']))
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['default_font_size']))
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_icon_flasks'],
            display_dict['minimap_color_flasks'],
        ))
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_flasks']))
        self.filter_file.write('\n')

    def show_life_flasks(self):
        """
        Handling for life flasks.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------------ #\n')
        self.filter_file.write('# --- [{0}.{1}] - Life Flasks --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ------------------------------ #\n')
        self.filter_file.write('\n')

        with open('resources/data/flasks/life.json', 'r') as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for flask in json_data:
                # Parse item.
                self.parse_flask(flask)

    def show_mana_flasks(self):
        """
        Handling for mana flasks.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------------ #\n')
        self.filter_file.write('# --- [{0}.{1}] - Mana Flasks --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ------------------------------ #\n')
        self.filter_file.write('\n')

        with open('resources/data/flasks/mana.json', 'r') as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for flask in json_data:
                # Parse item.
                self.parse_flask(flask)

    def show_hybrid_flasks(self):
        """
        Handling for hybrid flasks.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# -------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Hybrid Flasks --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# -------------------------------- #\n')
        self.filter_file.write('\n')

        with open('resources/data/flasks/hybrid.json', 'r') as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for flask in json_data:
                # Parse item.
                self.parse_flask(flask)

    def show_utility_flasks(self):
        """
        Handling for utility flasks.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# --------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Utility Flasks --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# --------------------------------- #\n')
        self.filter_file.write('\n')

        with open('resources/data/flasks/utility.json', 'r') as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for flask in json_data:
                # Parse item.
                self.parse_flask(flask)
