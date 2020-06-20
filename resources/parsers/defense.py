"""
Filter creation for equipment (worn items).
"""

# System Imports.

# User Imports.
from resources import logging as init_logging


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class DefenseParser():

    def __init__(self, filter_file, defense_types):
        self.filter_file = filter_file
        self.defense_types = defense_types

        logger.info('defense_types: {0}'.format(self.defense_types))

        # Handle for all present weapon types. Note that parse order is order that values show up in filter.
        if 'A' in self.defense_types:
            self.parse_a()

        if 'A/Ev' in self.defense_types:
            self.parse_a_ev()

        if 'Ev' in self.defense_types:
            self.parse_ev()

        if 'Ev/En' in self.defense_types:
            self.parse_ev_en()

        if 'En' in self.defense_types:
            self.parse_en()

        if 'A/En' in self.defense_types:
            self.parse_en_a()

    def parse_a(self):
        logger.info('Parsing Armor defenses.')

    def parse_a_ev(self):
        logger.info('Parsing Armor/Evasion defenses.')

    def parse_ev(self):
        logger.info('Parsing Evasion defenses.')

    def parse_ev_en(self):
        logger.info('Parsing Evasion/Energy Shield defenses.')

    def parse_en(self):
        logger.info('Parsing Energy Shield defenses.')

    def parse_en_a(self):
        logger.info('Parsing Armor/Energy Shield defenses.')
