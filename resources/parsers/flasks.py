"""
Filter creation for flasks.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict
from resources.parsers.templates import FilterTemplates


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
        self.template = FilterTemplates(filter_file, debug=debug)
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
        self.show_tinctures()

    def parse_flask(self, flask):
        """
        Handles filter rule definition of flasks.
        :param flask: Flask to create rules for.
        """
        if flask['Class'] in ['Life', 'Mana']:
            drop_level = flask['DropLevel'] + 6
        elif flask['Class'] == 'Hybrid':
            drop_level = flask['DropLevel'] + 10
        else:
            drop_level = 70

        # Separate handling for quicksilver flasks.
        if flask['Name'] == 'Quicksilver Flask':
            self.template.common_item(
                description='Low level Quicksilver Flasks',
                base_text=flask['Name'],
                item_level='<= 59',
                font_size=display_dict['rare_font_size'],
                minimap_size=0,
                minimap_color=display_dict['minimap_color_flasks'],
                minimap_shape=display_dict['minimap_icon_flasks'],
                playeffect=display_dict['minimap_color_flasks'],
            )
            self.template.common_item(
                description='High level Quicksilver Flasks',
                base_text=flask['Name'],
                font_size=display_dict['uncommon_font_size'],
                minimap_size=2,
                minimap_color=display_dict['minimap_color_flasks'],
                minimap_shape=display_dict['minimap_icon_flasks'],
                playeffect=display_dict['minimap_color_flasks'],
            )
        else:
            # All other flasks.
            self.template.common_item(
                base_text=flask['Name'],
                item_level='<= {0}'.format(drop_level),
                minimap_size=2,
                minimap_color=display_dict['minimap_color_flasks'],
                minimap_shape=display_dict['minimap_icon_flasks'],
                playeffect=display_dict['minimap_color_flasks'],
            )

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
        self.template.notable_item(
            description='High quality gems [15 - 20]%',
            class_text=['Life Flasks', 'Mana Flasks', 'Hybrid Flasks', 'Utility Flasks', 'Critical Utility Flasks'],
            quality='>= 15',
            font_size=display_dict['rare_font_size'],
            minimap_size=1,
            minimap_color=display_dict['minimap_color_flasks'],
            minimap_shape=display_dict['minimap_icon_flasks'],
            playeffect=display_dict['minimap_color_flasks'],
        )

        # High quality between 10 and 15%.
        self.template.notable_item(
            description='High quality gems [10 - 15]%',
            class_text=['Life Flasks', 'Mana Flasks', 'Hybrid Flasks', 'Utility Flasks', 'Critical Utility Flasks'],
            quality='>= 10',
            font_size=display_dict['uncommon_font_size'],
            minimap_size=1,
            minimap_color=display_dict['minimap_color_flasks'],
            minimap_shape=display_dict['minimap_icon_flasks'],
            playeffect=display_dict['minimap_color_flasks'],
        )

        # High quality between 5 and 10%.
        self.template.notable_item(
            description='High quality gems [10 - 15]%',
            class_text=['Life Flasks', 'Mana Flasks', 'Hybrid Flasks', 'Utility Flasks', 'Critical Utility Flasks'],
            quality='>= 10',
            font_size=display_dict['default_font_size'],
            minimap_size=1,
            minimap_color=display_dict['minimap_color_flasks'],
            minimap_shape=display_dict['minimap_icon_flasks'],
            playeffect=display_dict['minimap_color_flasks'],
        )

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

    def show_tinctures(self):
        """
        Handling for tinctures.
        """

        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Tinctures --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('\n')

        self.template.common_item(
            base_text="Tincture",
            minimap_size=2,
            minimap_color=display_dict['minimap_color_flasks'],
            minimap_shape=display_dict['minimap_icon_flasks'],
            playeffect=display_dict['minimap_color_flasks'],
        )
