"""
Filter creation for equipment (worn items).
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict, filter_dict
from resources.parsers.templates import FilterTemplates


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class DefenseParser:

    def __init__(self, filter_file, parse_num, defense_types, base_drop_level, level_rarity_modifier, debug=False):
        # Set class vars.
        self.filter_file = filter_file
        self.defense_types = defense_types
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
        self.debug = debug

        # Update dict values.
        filter_dict['base_drop_level'] = base_drop_level
        filter_dict['level_rarity_modifier'] = level_rarity_modifier

        if self.debug:
            logger.info('defense_types: {0}'.format(self.defense_types))

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ====================== #\n')
        self.filter_file.write('# === [{0}] - Armors === #\n'.format(self.parse_num))
        self.filter_file.write('# ====================== #\n')
        self.filter_file.write('\n')

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
        if def_type == 'A':
            padding_count = 0
        elif def_type in ['Ev', 'En']:
            padding_count = 1
        elif def_type in ['A/Ev', 'En/A']:
            padding_count = 3
        else:
            padding_count = 4

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# --------------------{0} #\n'.format('-' * padding_count))
        self.filter_file.write('# --- [{0}.{1}] - {2} --- #\n'.format(self.parse_num, subnum, def_type))
        self.filter_file.write('# --------------------{0} #\n'.format('-' * padding_count))
        self.filter_file.write('\n')

        # Parse helmets.
        with open('resources/data/equipment/{0}/helmets.json'.format(def_file), 'r') as json_file:
            # Create helmet section header.
            self.filter_file.write('\n')
            self.filter_file.write('# -------------------------------{0} #\n'.format('-' * padding_count))
            self.filter_file.write(
                '# --- [{0}.{1}.{2}] - {3} Helmets --- #\n'.format(self.parse_num, subnum, '01', def_type)
            )
            self.filter_file.write('# -------------------------------{0} #\n'.format('-' * padding_count))
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
            self.filter_file.write('# ------------------------------{0} #\n'.format('-' * padding_count))
            self.filter_file.write(
                '# --- [{0}.{1}.{2}] - {3} Chests --- #\n'.format(self.parse_num, subnum, '02', def_type)
            )
            self.filter_file.write('# ------------------------------{0} #\n'.format('-' * padding_count))
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
            self.filter_file.write('# ------------------------------{0} #\n'.format('-' * padding_count))
            self.filter_file.write(
                '# --- [{0}.{1}.{2}] - {3} Gloves --- #\n'.format(self.parse_num, subnum, '03', def_type)
            )
            self.filter_file.write('# ------------------------------{0} #\n'.format('-' * padding_count))
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
            self.filter_file.write('# -----------------------------{0} #\n'.format('-' * padding_count))
            self.filter_file.write(
                '# --- [{0}.{1}.{2}] - {3} Boots --- #\n'.format(self.parse_num, subnum, '04', def_type)
            )
            self.filter_file.write('# -----------------------------{0} #\n'.format('-' * padding_count))
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
        self.parse_item_max_slot(def_type, item)
        self.parse_item_rgb(def_type, item)
        self.parse_item_uncommon(def_type, item)
        self.parse_item_base(def_type, item)

    def parse_item_rare(self, def_type, item):
        """
        Handles filtering for rare version of item.
        :param def_type: Defense type of the item.
        :param item: The item to parse.
        """
        drop_level = filter_dict['base_drop_level'] + (filter_dict['level_rarity_modifier'] * 2)

        if item['MaxLevel'] is True:
            self.template.rare_item(
                base_text=item['Name'],
                background_color=display_dict[def_type],
            )
        else:
            self.template.rare_item(
                base_text=item['Name'],
                item_level='<= {0}'.format(item['DropLevel'] + drop_level),
                background_color=display_dict[def_type],
            )

    def parse_item_max_slot(self, def_type, item):
        """
        Handles filtering for max slot version of item.
        :param def_type: Defense type of the item.
        :param item: The item to parse.
        """
        drop_level = filter_dict['base_drop_level'] + (filter_dict['level_rarity_modifier'] * 2)
        item_level = item['DropLevel']

        if item_level <= 25:
            # Filter for 3-socket max items early on.
            self.template.common_item(
                description='Max Slot Type',
                base_text=item['Name'],
                item_level='<= {0}'.format(item_level + drop_level),
                linked_sockets='3',
                background_color=display_dict[def_type],
                border_color=display_dict['normal'],
                font_size=display_dict['uncommon_font_size'],
            )

        elif item_level <= 35:
            # Filter for 4-socket max items early on.
            self.template.common_item(
                description='Max Slot Type',
                base_text=item['Name'],
                item_level='<= {0}'.format(item_level + drop_level),
                linked_sockets='4',
                background_color=display_dict[def_type],
                border_color=display_dict['normal'],
                font_size=display_dict['uncommon_font_size'],
            )

    def parse_item_rgb(self, def_type, item):
        """
        Handles filtering for linked RGB version of item.
        :param def_type: Defense type of the item.
        :param item: The item to parse.
        """
        drop_level = filter_dict['base_drop_level']

        if item['MaxLevel'] is True:
            self.template.common_item(
                description='Linked RGB Type',
                base_text=item['Name'],
                socket_group='"RGB"',
                background_color=display_dict[def_type],
                border_color=display_dict['normal'],
                font_size=display_dict['uncommon_font_size'],
            )
        else:
            self.template.common_item(
                description='Linked RGB Type',
                base_text=item['Name'],
                item_level='<= {0}'.format(item['DropLevel'] + drop_level),
                socket_group='"RGB"',
                background_color=display_dict[def_type],
                border_color=display_dict['normal'],
                font_size=display_dict['uncommon_font_size'],
            )

    def parse_item_uncommon(self, def_type, item):
        """
        Handles filtering for uncommon/magic version of item.
        :param def_type: Defense type of the item.
        :param item: The item to parse.
        """
        drop_level = filter_dict['base_drop_level'] + filter_dict['level_rarity_modifier']

        if item['MaxLevel'] is True:
            self.template.uncommon_item(
                base_text=item['Name'],
                background_color=display_dict[def_type],
            )
        else:
            self.template.uncommon_item(
                base_text=item['Name'],
                item_level='<= {0}'.format(item['DropLevel'] + drop_level),
                background_color=display_dict[def_type],
            )

    def parse_item_base(self, def_type, item):
        """
        Handles filtering for standard version of item.
        :param def_type: Defense type of the item.
        :param item: The item to parse.
        """
        drop_level = filter_dict['base_drop_level']

        if item['MaxLevel'] is True:
            self.template.common_item(
                base_text=item['Name'],
                background_color=display_dict[def_type],
            )
        else:
            self.template.common_item(
                base_text=item['Name'],
                item_level='<= {0}'.format(item['DropLevel'] + drop_level),
                background_color=display_dict[def_type],
            )

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
