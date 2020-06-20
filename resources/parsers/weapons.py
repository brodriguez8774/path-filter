"""
Filter creation for hand-held items.
"""

# System Imports.

# User Imports.
from resources import logging as init_logging


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class WeaponParser():

    def __init__(self, filter_file, parse_num, weapon_types, defense_types):
        self.filter_file = filter_file
        self.pars_num = parse_num
        self.weapon_types = weapon_types
        self.defense_types = defense_types

        logger.info('weapon_types: {0}'.format(self.weapon_types))
        logger.info('defense_types: {0}'.format(self.defense_types))

        # Handle for all present weapon types. Note that parse order is order that values show up in filter.
        if 'Wands' in self.weapon_types:
            self.parse_wands()

        if 'Shields' in self.weapon_types:
            self.parse_shields()

    def parse_wands(self):
        logger.info('Parsing wands.')

    def parse_shields(self):
        logger.info('Parsing Shields.')
