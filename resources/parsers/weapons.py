"""
Filter creation for hand-held items.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict, filter_dict
from resources.parsers.templates import FilterTemplates


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class WeaponParser():
    def __init__(self, filter_file, parse_num, weapon_types, shield_types, base_drop_level, level_rarity_modifier, debug=False):
        # Set class vars.
        self.filter_file = filter_file
        self.weapon_types = weapon_types
        self.shield_types = shield_types
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
        self.debug = debug

        # Update dict values.
        filter_dict['base_drop_level'] = base_drop_level
        filter_dict['level_rarity_modifier'] = level_rarity_modifier

        if self.debug:
            logger.info('weapon_types: {0}'.format(self.weapon_types))
            logger.info('defense_types: {0}'.format(self.shield_types))

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ======================= #\n')
        self.filter_file.write('# === [{0}] - Weapons === #\n'.format(self.parse_num))
        self.filter_file.write('# ======================= #\n')
        self.filter_file.write('\n')

        # Handle for all present weapon types. Note that parse order is order that values show up in filter.
        if 'Bows' in self.weapon_types:
            self.parse_bows()

        if 'Quivers' in self.weapon_types:
            self.parse_quivers()

        if 'Wands' in self.weapon_types:
            self.parse_wands()

        if 'Shields' in self.weapon_types:
            self.parse_shields()

    def parse_item(self, item):
        """
        Parses an individual item.
        :param item: The item to parse.
        """
        # logger.info(item)
        self.filter_file.write('\n\n')
        self.filter_file.write('# === Item: {0} === #\n'.format(item['Name']))

        self.parse_item_rare(item)

        # Exclude for weapons that don't have slots.
        if item['Class'] != 'Quiver':
            self.parse_item_max_slot(item)
            self.parse_item_rgb(item)

        self.parse_item_uncommon(item)
        self.parse_item_base(item)

    def parse_item_rare(self, item):
        """
        Handles filtering for rare version of item.
        :param item: The item to parse.
        """
        drop_level = filter_dict['base_drop_level'] + (filter_dict['level_rarity_modifier'] * 2)

        self.template.rare_item(
            base_text=item['Name'],
            background_color=display_dict['dark_grey_background'],
            item_level='<= {0}'.format(item['DropLevel'] + drop_level),
        )

    def parse_item_max_slot(self, item):
        """
        Handles filtering for max slot version of item.
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
                background_color=display_dict['dark_grey_background'],
                border_color=display_dict['normal'],
                font_size=display_dict['uncommon_font_size'],
            )

        elif item_level <= 35:
            # Filter for 4-socket max items early on.
            self.template.common_item(
                description='Max Slot Type',
                base_text=item['Name'],
                item_level='<= {0}'.format(item_level + drop_level),
                linked_sockets='3',
                background_color=display_dict['dark_grey_background'],
                border_color=display_dict['normal'],
                font_size=display_dict['uncommon_font_size'],
            )
            self.filter_file.write('# Max Slot Type.\n')
            self.filter_file.write('Show\n')

    def parse_item_rgb(self, item):
        """
        Handles filtering for linked RGB version of item.
        :param item: The item to parse.
        """
        drop_level = filter_dict['base_drop_level']

        self.template.common_item(
            description='Linked RGB Type',
            base_text=item['Name'],
            item_level='<= {0}'.format(item['DropLevel'] + drop_level),
            socket_group='"RGB"',
            background_color=display_dict['dark_grey_background'],
            border_color=display_dict['normal'],
            font_size=display_dict['uncommon_font_size'],
        )

    def parse_item_uncommon(self, item):
        """
        Handles filtering for uncommon/magic version of item.
        :param item: The item to parse.
        """
        drop_level = filter_dict['base_drop_level'] + filter_dict['level_rarity_modifier']

        self.template.uncommon_item(
            base_text=item['Name'],
            background_color=display_dict['dark_grey_background'],
            item_level='<= {0}'.format(item['DropLevel'] + drop_level),
        )

    def parse_item_base(self, item):
        """
        Handles filtering for standard version of item.
        :param item: The item to parse.
        """
        drop_level = filter_dict['base_drop_level']

        self.template.common_item(
            base_text=item['Name'],
            background_color=display_dict['dark_grey_background'],
            item_level='<= {0}'.format(item['DropLevel'] + drop_level),
        )

    def parse_bows(self):
        """
        Parses all "Bow" type weapons.
        """
        if self.debug:
            logger.info('Parsing bows.')

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ----------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Bows --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ----------------------- #\n')
        self.filter_file.write('\n')

        # Parse wands.
        with open('resources/data/hand/bows.json', 'r') as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item)

    def parse_quivers(self):
        """
        Parses all "Quiver" type weapons.
        """
        if self.debug:
            logger.info('Parsing quivers.')

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# -------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Quivers --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# -------------------------- #\n')
        self.filter_file.write('\n')

        # Parse wands.
        with open('resources/data/hand/quivers.json', 'r') as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item)

    def parse_wands(self):
        """
        Parses all "Wand" type weapons.
        """
        if self.debug:
            logger.info('Parsing wands.')

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------ #\n')
        self.filter_file.write('# --- [{0}.{1}] - Wands --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
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
        """
        Parses all "Shield" type items, based on selected defenses.
        """
        if self.debug:
            logger.info('Parsing Shields.')

        self.parse_subnum += 1
        subsubnum = 0

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# -------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Shields --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# -------------------------- #\n')
        self.filter_file.write('\n')

        if 'A' in self.shield_types:
            # Parse Armor shields.
            subsubnum += 1

            self.filter_file.write('\n')
            self.filter_file.write('# ------------------------------ #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - A Shields --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2), subsubnum))
            self.filter_file.write('# ------------------------------ #\n')
            self.filter_file.write('\n')

            with open('resources/data/hand/shields/A.json', 'r') as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item)

        if 'A/Ev' in self.shield_types:
            # Parse Armor/Evasion shields.
            subsubnum += 1

            self.filter_file.write('\n')
            self.filter_file.write('# --------------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - A/Ev Shields --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2), subsubnum))
            self.filter_file.write('# --------------------------------- #\n')
            self.filter_file.write('\n')

            with open('resources/data/hand/shields/A_Ev.json', 'r') as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item)

        if 'Ev' in self.shield_types:
            # Parse Evasion shields.
            subsubnum += 1

            self.filter_file.write('\n')
            self.filter_file.write('# ------------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - Ev Shields --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2), subsubnum))
            self.filter_file.write('# ------------------------------- #\n')
            self.filter_file.write('\n')

            with open('resources/data/hand/shields/Ev.json', 'r') as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item)

        if 'Ev/En' in self.shield_types:
            # Parse Evasion/Energy Shield shields.
            subsubnum += 1

            self.filter_file.write('\n')
            self.filter_file.write('# ---------------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - Ev/En Shields --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2), subsubnum))
            self.filter_file.write('# ---------------------------------- #\n')
            self.filter_file.write('\n')

            with open('resources/data/hand/shields/Ev_En.json', 'r') as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item)

        if 'En' in self.shield_types:
            # Parse Energy Shield shields.
            subsubnum += 1

            self.filter_file.write('\n')
            self.filter_file.write('# ------------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - En Shields --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2), subsubnum))
            self.filter_file.write('# ------------------------------- #\n')
            self.filter_file.write('\n')

            with open('resources/data/hand/shields/En.json', 'r') as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item)

        if 'A/En' in self.shield_types:
            # Parse Armor/Energy Shield shields.
            subsubnum += 1

            self.filter_file.write('\n')
            self.filter_file.write('# --------------------------------- #\n')
            self.filter_file.write('# --- [{0}.{1}.{2}] - A/En Shields --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2), subsubnum))
            self.filter_file.write('# --------------------------------- #\n')
            self.filter_file.write('\n')

            with open('resources/data/hand/shields/En_A.json','r') as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item)
