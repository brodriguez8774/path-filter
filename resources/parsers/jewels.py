"""
Filter creation for jewels.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict
from resources.parsers.templates import FilterTemplates


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class JewelParser:
    """
    Filtering for all jewel drops.
    """

    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
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
        self.filter_file.write(
            '# --- [{0}.{1}] - Standard Jewels --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('\n')

        self.template.special_item(
            base_text=['Cobalt Jewel', 'Crimson Jewel', 'Viridian Jewel'],
            minimap_size=2,
            minimap_shape=display_dict['minimap_icon_jewel'],
        )

    def parse_abyss(self):
        """"""
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------------- #\n')
        self.filter_file.write(
            '# --- [{0}.{1}] - Abyss Jewels --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write('# ------------------------------- #\n')
        self.filter_file.write('\n')

        self.template.special_item(
            class_text='Abyss Jewel',
            minimap_size=1,
            minimap_shape=display_dict['minimap_icon_jewel'],
        )

    def parse_cluster(self):
        """"""
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# --------------------------------- #\n')
        self.filter_file.write(
            '# --- [{0}.{1}] - Cluster Jewels --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write('# --------------------------------- #\n')
        self.filter_file.write('\n')

        self.template.special_item(
            base_text='Cluster Jewel',
            minimap_size=0,
            minimap_shape=display_dict['minimap_icon_jewel'],
            sound='4 300',
        )
