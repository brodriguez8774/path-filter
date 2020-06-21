"""
Filter creation for equipment (worn items).
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import value_dict


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class DefenseParser():

    def __init__(self, filter_file, parse_num, defense_types, debug=False):
        self.filter_file = filter_file
        self.defense_types = defense_types
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.debug = debug

        if self.debug:
            logger.info('defense_types: {0}'.format(self.defense_types))

        # Handle for all present weapon types. Note that parse order is order that values show up in filter.
        if 'A' in self.defense_types:
            self.parse_subnum += 1
            self.parse_a()

        if 'A/Ev' in self.defense_types:
            self.parse_subnum += 1
            self.parse_a_ev()

        if 'Ev' in self.defense_types:
            self.parse_subnum += 1
            self.parse_ev()

        if 'Ev/En' in self.defense_types:
            self.parse_subnum += 1
            self.parse_ev_en()

        if 'En' in self.defense_types:
            self.parse_subnum += 1
            self.parse_en()

        if 'A/En' in self.defense_types:
            self.parse_subnum += 1
            self.parse_en_a()

    def parse_section(self, def_type, subnum):
        """
        Parses a full armor type section.
        :param def_type: The armor type to parse.
        :param subnum: Counter of "armor type sections" parsed so far.
        """
        def_file = def_type.replace('/', '_')

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - {2} --- #\n'.format(self.parse_num, subnum, def_type))
        self.filter_file.write('# ---------------------- #\n')
        self.filter_file.write('\n')

        # Parse helmets.
        with open('resources/data/equipment/{0}/helmets.json'.format(def_file), 'r') as json_file:
            # Create helmet section header.
            self.filter_file.write('\n')
            self.filter_file.write('# ----------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - {3} Helmets --- #\n'.format(self.parse_num, subnum, '01', def_type))
            self.filter_file.write('# ----------------------------- #\n')
            self.filter_file.write('\n')

            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(def_type, item)

        # Parse chests.
        with open('resources/data/equipment/{0}/chests.json'.format(def_file), 'r') as json_file:
            # Create chest section header.
            self.filter_file.write('\n')
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - {3} Chests --- #\n'.format(self.parse_num, subnum, '02', def_type))
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('\n')

            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(def_type, item)

        # Parse gloves.
        with open('resources/data/equipment/{0}/gloves.json'.format(def_file), 'r') as json_file:
            # Create glove section header.
            self.filter_file.write('\n')
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - {3} Gloves --- #\n'.format(self.parse_num, subnum, '03', def_type))
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('\n')

            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(def_type, item)

        # Parse boots.
        with open('resources/data/equipment/{0}/boots.json'.format(def_file), 'r') as json_file:
            # Create boot section header.
            self.filter_file.write('\n')
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - {3} Boots --- #\n'.format(self.parse_num, subnum, '04', def_type))
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('\n')

            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(def_type, item)

    def parse_item(self, def_type, item):
        """
        Parses an individual item.
        :param def_type: Defense type of the item.
        :param item: The item to parse.
        """
        # logger.info(item)
        self.filter_file.write('\n\n')
        self.filter_file.write('# === Item: {0} === #\n'.format(item['Name']))

        self.parse_item_rare(def_type, item)
        self.parse_item_rgb(def_type, item)
        self.parse_item_max_slot(def_type, item)
        self.parse_item_uncommon(def_type, item)
        self.parse_item_base(def_type, item)

    def parse_item_rare(self, def_type, item):
        """
        Handles filtering for rare version of item.
        :param def_type: Defense type of the item.
        :param item: The item to parse.
        """
        self.filter_file.write('# Rare Type.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType {0}\n'.format(item['Name']))
        if not item['MaxLevel']:    # Only filter on ItemLevel if item is not a max-level drop.
            self.filter_file.write('    ItemLevel <= {0}\n'.format(item['DropLevel'] + 10))
        self.filter_file.write('    Rarity = Rare\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(value_dict[def_type]))
        self.filter_file.write('    SetBorderColor {0}\n'.format(value_dict['rare']))
        self.filter_file.write('    SetFontSize {0}\n'.format(value_dict['default_font_size']))
        self.filter_file.write('\n')

    def parse_item_rgb(self, def_type, item):
        """
        Handles filtering for linked RGB version of item.
        :param def_type: Defense type of the item.
        :param item: The item to parse.
        """
        self.filter_file.write('# Linked RGB Type.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType {0}\n'.format(item['Name']))
        if not item['MaxLevel']:    # Only filter on ItemLevel if item is not a max-level drop.
            self.filter_file.write('    ItemLevel <= {0}\n'.format(item['DropLevel'] + 10))
        self.filter_file.write('    SocketGroup "RGB"\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(value_dict[def_type]))
        self.filter_file.write('    SetBorderColor {0}\n'.format(value_dict['normal']))
        self.filter_file.write('    SetFontSize {0}\n'.format(value_dict['default_font_size']))
        self.filter_file.write('\n')

    def parse_item_max_slot(self, def_type, item):
        """
        Handles filtering for max slot version of item.
        :param def_type: Defense type of the item.
        :param item: The item to parse.
        """
        item_level = item['DropLevel']

        if item_level <= 25:
            # Filter for 3-socket max items.
            self.filter_file.write('# Max Slot Type.\n')
            self.filter_file.write('Show\n')

            # Limitations to filter on.
            self.filter_file.write('    BaseType {0}\n'.format(item['Name']))
            self.filter_file.write('    ItemLevel <= {0}\n'.format(item['DropLevel']))
            self.filter_file.write('    LinkedSockets >= 3\n')

            # Values to set if filter match is found.
            self.filter_file.write('    SetBackgroundColor {0}\n'.format(value_dict[def_type]))
            self.filter_file.write('    SetBorderColor {0}\n'.format(value_dict['normal']))
            self.filter_file.write('    SetFontSize {0}\n'.format(value_dict['default_font_size']))
            self.filter_file.write('\n')

        elif item_level <= 35:
            # Filter for 4-socket max items.
            self.filter_file.write('# Max Slot Type.\n')
            self.filter_file.write('Show\n')

            # Limitations to filter on.
            self.filter_file.write('    BaseType {0}\n'.format(item['Name']))
            self.filter_file.write('    ItemLevel <= {0}\n'.format(item['DropLevel']))
            self.filter_file.write('    LinkedSockets >= 4\n')

            # Values to set if filter match is found.
            self.filter_file.write('    SetBackgroundColor {0}\n'.format(value_dict[def_type]))
            self.filter_file.write('    SetFontSize {0}\n'.format(value_dict['default_font_size']))
            self.filter_file.write('\n')

    def parse_item_uncommon(self, def_type, item):
        """
        Handles filtering for uncommon/magic version of item.
        :param def_type: Defense type of the item.
        :param item: The item to parse.
        """
        self.filter_file.write('# Uncommon Type.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType {0}\n'.format(item['Name']))
        if not item['MaxLevel']:    # Only filter on ItemLevel if item is not a max-level drop.
            self.filter_file.write('    ItemLevel <= {0}\n'.format(item['DropLevel'] + 10))
        self.filter_file.write('    Rarity = Magic\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(value_dict[def_type]))
        self.filter_file.write('    SetBorderColor {0}\n'.format(value_dict['magic']))
        self.filter_file.write('    SetFontSize {0}\n'.format(value_dict['default_font_size']))
        self.filter_file.write('\n')

    def parse_item_base(self, def_type, item):
        """
        Handles filtering for standard version of item.
        :param def_type: Defense type of the item.
        :param item: The item to parse.
        """
        self.filter_file.write('# Base Type.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType {0}\n'.format(item['Name']))
        if not item['MaxLevel']:    # Only filter on ItemLevel if item is not a max-level drop.
            self.filter_file.write('    ItemLevel <= {0}\n'.format(item['DropLevel'] + 10))

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(value_dict[def_type]))
        self.filter_file.write('    SetFontSize {0}\n'.format(value_dict['default_font_size']))
        self.filter_file.write('\n')

    def parse_a(self):
        """
        Parses all "Armor" type defense equipment.
        """
        if self.debug:
            logger.info('Parsing Armor defenses.')

        parse_subnum = str(self.parse_subnum).zfill(2)
        self.parse_section('A', parse_subnum)

    def parse_a_ev(self):
        """
        Parses all "Armor/Evasion" type defense equipment.
        """
        if self.debug:
            logger.info('Parsing Armor/Evasion defenses.')

        parse_subnum = str(self.parse_subnum).zfill(2)
        self.parse_section('A/Ev', parse_subnum)

    def parse_ev(self):
        """
        Parses all "Evasion" type defense equipment.
        """
        if self.debug:
            logger.info('Parsing Evasion defenses.')

        parse_subnum = str(self.parse_subnum).zfill(2)
        self.parse_section('Ev', parse_subnum)

    def parse_ev_en(self):
        """
        Parses all "Evasion/Energy Shield" type defense equipment.
        """
        if self.debug:
            logger.info('Parsing Evasion/Energy Shield defenses.')

        parse_subnum = str(self.parse_subnum).zfill(2)
        self.parse_section('Ev/En', parse_subnum)

    def parse_en(self):
        """
        Parses all "Energy Shield" type defense equipment.
        """
        if self.debug:
            logger.info('Parsing Energy Shield defenses.')

        parse_subnum = str(self.parse_subnum).zfill(2)
        self.parse_section('En', parse_subnum)

    def parse_en_a(self):
        """
        Parses all "Armor/Energy Shield" type defense equipment.
        """
        if self.debug:
            logger.info('Parsing Armor/Energy Shield defenses.')

        parse_subnum = str(self.parse_subnum).zfill(2)
        self.parse_section('En/A', parse_subnum)
