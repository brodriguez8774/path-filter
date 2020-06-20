"""
Filter creation for hand-held items.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import value_dict


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class WeaponParser():

    def __init__(self, filter_file, parse_num, weapon_types, defense_types):
        self.filter_file = filter_file
        self.weapon_types = weapon_types
        self.defense_types = defense_types
        self.parse_num = parse_num
        self.parse_subnum = 0

        logger.info('weapon_types: {0}'.format(self.weapon_types))
        logger.info('defense_types: {0}'.format(self.defense_types))

        # Handle for all present weapon types. Note that parse order is order that values show up in filter.
        if 'Wands' in self.weapon_types:
            self.parse_wands()

        if 'Shields' in self.weapon_types:
            self.parse_shields()

    def parse_item(self, item):
        # logger.info(item)
        self.filter_file.write('\n\n')
        self.filter_file.write('# === Item: {0} === #\n'.format(item['Name']))

        self.parse_item_rare(item)
        self.parse_item_rgb(item)
        self.parse_item_max_slot(item)
        self.parse_item_uncommon(item)
        self.parse_item_base(item)

    def parse_item_rare(self, item):
        self.filter_file.write('# Rare Type.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType {0}\n'.format(item['Name']))
        if not item['MaxLevel']:    # Only filter on ItemLevel if item is not a max-level drop.
            self.filter_file.write('    ItemLevel <= {0}\n'.format(item['DropLevel'] + 10))
        self.filter_file.write('    Rarity = Rare\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(value_dict['weapon']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(value_dict['rare']))
        self.filter_file.write('    SetFontSize {0}\n'.format(value_dict['default_font_size']))
        self.filter_file.write('\n')

    def parse_item_rgb(self, item):
        self.filter_file.write('# Linked RGB Type.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType {0}\n'.format(item['Name']))
        if not item['MaxLevel']:    # Only filter on ItemLevel if item is not a max-level drop.
            self.filter_file.write('    ItemLevel <= {0}\n'.format(item['DropLevel'] + 10))
        self.filter_file.write('    SocketGroup "RGB"\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(value_dict['weapon']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(value_dict['normal']))
        self.filter_file.write('    SetFontSize {0}\n'.format(value_dict['default_font_size']))
        self.filter_file.write('\n')

    def parse_item_max_slot(self, item):
        item_level = item['DropLevel']

        if item_level <= 25:
            # Filter for socket-max items. Somewhat rare early game.
            self.filter_file.write('# Max Slot Type.\n')
            self.filter_file.write('Show\n')

            # Limitations to filter on.
            self.filter_file.write('    BaseType {0}\n'.format(item['Name']))
            if not item['MaxLevel']:    # Only filter on ItemLevel if item is not a max-level drop.
                self.filter_file.write('    ItemLevel <= {0}\n'.format(item['DropLevel'] + 10))

            # Values to set if filter match is found.
            self.filter_file.write('    SetBackgroundColor {0}\n'.format(value_dict['weapon']))
            self.filter_file.write('    SetBorderColor {0}\n'.format(value_dict['normal']))
            self.filter_file.write('    SetFontSize {0}\n'.format(value_dict['default_font_size']))
            self.filter_file.write('\n')

    def parse_item_uncommon(self, item):
        self.filter_file.write('# Uncommon Type.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType {0}\n'.format(item['Name']))
        if not item['MaxLevel']:    # Only filter on ItemLevel if item is not a max-level drop.
            self.filter_file.write('    ItemLevel <= {0}\n'.format(item['DropLevel'] + 10))
        self.filter_file.write('    Rarity = Magic\n')

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(value_dict['weapon']))
        self.filter_file.write('    SetBorderColor {0}\n'.format(value_dict['magic']))
        self.filter_file.write('    SetFontSize {0}\n'.format(value_dict['default_font_size']))
        self.filter_file.write('\n')

    def parse_item_base(self, item):
        self.filter_file.write('# Base Type.\n')
        self.filter_file.write('Show\n')

        # Limitations to filter on.
        self.filter_file.write('    BaseType {0}\n'.format(item['Name']))
        if not item['MaxLevel']:    # Only filter on ItemLevel if item is not a max-level drop.
            self.filter_file.write('    ItemLevel <= {0}\n'.format(item['DropLevel'] + 10))

        # Values to set if filter match is found.
        self.filter_file.write('    SetBackgroundColor {0}\n'.format(value_dict['weapon']))
        self.filter_file.write('    SetFontSize {0}\n'.format(value_dict['default_font_size']))
        self.filter_file.write('\n')

    def parse_wands(self):
        logger.info('Parsing wands.')
        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------ #\n')
        self.filter_file.write('# --- [{0}.{1}] - Wands --- #\n'.format(self.parse_num, self.parse_subnum))
        self.filter_file.write('# ------------------------ #\n')
        self.filter_file.write('\n')

        # Parse wands.
        with open('resources/data/hand/wands.json', 'r') as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item)

    def parse_shields(self):
        logger.info('Parsing Shields.')
        self.parse_subnum += 1
        subsubnum = 0

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# -------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Shields --- #\n'.format(self.parse_num, self.parse_subnum))
        self.filter_file.write('# -------------------------- #\n')
        self.filter_file.write('\n')

        if 'A' in self.defense_types:
            # Parse Armor shields.
            subsubnum += 1

            self.filter_file.write('\n')
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - A Shields --- #\n'.format(self.parse_num, self.parse_subnum, subsubnum))
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('\n')

            with open('resources/data/hand/shields/A.json', 'r') as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item)

        if 'A/Ev' in self.defense_types:
            # Parse Armor/Evasion shields.
            subsubnum += 1

            self.filter_file.write('\n')
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - A/Ev Shields --- #\n'.format(self.parse_num, self.parse_subnum, subsubnum))
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('\n')

            with open('resources/data/hand/shields/A_Ev.json', 'r') as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item)

        if 'Ev' in self.defense_types:
            # Parse Evasion shields.
            subsubnum += 1

            self.filter_file.write('\n')
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - Ev Shields --- #\n'.format(self.parse_num, self.parse_subnum, subsubnum))
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('\n')

            with open('resources/data/hand/shields/Ev.json', 'r') as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item)

        if 'Ev/En' in self.defense_types:
            # Parse Evasion/Energy Shield shields.
            subsubnum += 1

            self.filter_file.write('\n')
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - Ev/En Shields --- #\n'.format(self.parse_num, self.parse_subnum, subsubnum))
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('\n')

            with open('resources/data/hand/shields/Ev_En.json', 'r') as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item)

        if 'En' in self.defense_types:
            # Parse Energy Shield shields.
            subsubnum += 1

            self.filter_file.write('\n')
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - En Shields --- #\n'.format(self.parse_num, self.parse_subnum, subsubnum))
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('\n')

            with open('resources/data/hand/shields/En.json', 'r') as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item)

        if 'A/En' in self.defense_types:
            # Parse Armor/Energy Shield shields.
            subsubnum += 1

            self.filter_file.write('\n')
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - A/En Shields --- #\n'.format(self.parse_num, self.parse_subnum, subsubnum))
            self.filter_file.write('# ---------------------------- #\n')
            self.filter_file.write('\n')

            with open('resources/data/hand/shields/En_A.json','r') as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item)
