"""
Filter creation for maps.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict, filter_dict


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class MapParser():
    """
    Filtering for all map drops.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ==================== #\n')
        self.filter_file.write('# === [{0}] - Maps === #\n'.format(self.parse_num))
        self.filter_file.write('# ==================== #\n')
        self.filter_file.write('\n')

        self.generate_map_filter()

    def generate_map_filter(self):
        """
        Generates filtering for all map types.
        """
        # High quality maps.
        self.filter_file.write('# High Quality Maps.\n')
        self.filter_file.write('Show\n')
        self.filter_file.write('    Class "Map"\n')
        self.filter_file.write('    Quality >= 10\n')
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['rare_font_size']))
        self.filter_file.write('    PlayAlertSound 16 100\n')
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_icon_maps'],
            display_dict['minimap_color_maps']),
        )
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_maps']))
        self.filter_file.write('\n')

        # High tier maps.
        self.filter_file.write('# High Tier Maps.\n')
        self.filter_file.write('Show\n')
        self.filter_file.write('    Class "Map"\n')
        self.filter_file.write('    MapTier >= 11\n')
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['rare_font_size']))
        self.filter_file.write('    PlayAlertSound 16 100\n')
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_icon_maps'],
            display_dict['minimap_color_maps']),
        )
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_maps']))
        self.filter_file.write('\n')

        # Medium tier maps.
        self.filter_file.write('# Medium Tier Maps.\n')
        self.filter_file.write('Show\n')
        self.filter_file.write('    Class "Map"\n')
        self.filter_file.write('    MapTier >= 6\n')
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['uncommon_font_size']))
        self.filter_file.write('    PlayAlertSound 16 75\n')
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_icon_maps'],
            display_dict['minimap_color_maps']),
        )
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_maps']))
        self.filter_file.write('\n')

        # Low tier maps.
        self.filter_file.write('# Low Tier Maps.\n')
        self.filter_file.write('Show\n')
        self.filter_file.write('    Class "Map" "Map Fragments" "Misc Map Items"\n')
        self.filter_file.write('    SetFontSize {0}\n'.format(display_dict['default_font_size']))
        self.filter_file.write('    PlayAlertSound 16 50\n')
        self.filter_file.write('    MinimapIcon 2 {0} {1}\n'.format(
            display_dict['minimap_icon_maps'],
            display_dict['minimap_color_maps']),
        )
        self.filter_file.write('    PlayEffect {0}\n'.format(display_dict['minimap_color_maps']))
        self.filter_file.write('\n')



