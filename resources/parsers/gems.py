"""
Filter creation for gems.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict
from resources.parsers.templates import FilterTemplates


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class GemParser:
    """
    Filtering for all gem drops.
    """

    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
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
        self.filter_file.write(
            '# --- [{0}.{1}] - Rare Gems --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('\n')

        self.template.special_item(
            description='Rare gems',
            class_text='Gem',
            base_text=[
                'Empower',
                'Enhance',
                'Enlighten',
                'Portal',
            ],
            border_color=display_dict['unique'],
            minimap_size=0,
        )

    def high_quality_gems(self):
        """
        Handling for high quality gems.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------------------ #\n')
        self.filter_file.write(
            '# --- [{0}.{1}] - High Quality Gems --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write('# ------------------------------------ #\n')
        self.filter_file.write('\n')

        # High quality between 15 and 20%.
        self.template.rare_currency(
            description='High quality gems [15 - 20]%',
            class_text='Gem',
            quality='>= 15',
            font_size=display_dict['important_font_size'],
            minimap_size=2,
            sound='5 175',
        )

        # High quality between 10 and 15%.
        self.template.rare_currency(
            description='High quality gems [10 - 15]%',
            class_text='Gem',
            quality='>= 10',
            font_size=display_dict['rare_font_size'],
            minimap_size=2,
            sound='5 175',
        )

        # High quality between 5 and 10%.
        self.template.rare_currency(
            description='High quality gems [5 - 10]%',
            class_text='Gem',
            quality='>= 5',
            font_size=display_dict['uncommon_font_size'],
            minimap_size=2,
            sound='5 175',
        )

        # High quality under 5%
        self.template.rare_currency(
            description='High quality gems [1 - 4]%',
            class_text='Gem',
            quality='>= 1',
            font_size=display_dict['default_font_size'],
        )

    def vaal_gems(self):
        """
        Handling for vaal gems.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write(
            '# --- [{0}.{1}] - Vaal Gems --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write('# ---------------------------- #\n')
        self.filter_file.write('\n')

        self.template.notable_item(
            class_text='Gem',
            base_text='Vaal',
            font_size=display_dict['uncommon_font_size'],
        )
