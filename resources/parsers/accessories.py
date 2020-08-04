"""
Filter creation for accessories.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import filter_dict
from resources.parsers.templates import FilterTemplates


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class AccessoryParser():

    def __init__(self, filter_file, parse_num, hidden_amulets, hidden_belts, hidden_rings, base_drop_level,
                 level_rarity_modifier, debug=False):
        self.filter_file = filter_file
        self.hidden_amulets = hidden_amulets
        self.hidden_belts = hidden_belts
        self.hidden_rings = hidden_rings
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
        self.debug = debug

        # Update dict values.
        filter_dict['base_drop_level'] = base_drop_level
        filter_dict['level_rarity_modifier'] = level_rarity_modifier

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# =========================== #\n')
        self.filter_file.write('# === [{0}] - Accessories === #\n'.format(self.parse_num))
        self.filter_file.write('# =========================== #\n')
        self.filter_file.write('\n')

        self.parse_amulets()
        self.parse_belts()
        self.parse_rings()

    def handle_accessory(self, item, exception_list):
        """
        Creates filtering for passed accessory.
        :param item: Accessory item to determine filtering on.
        :param exception_list: List of exceptions. If item is set to hide but in this list, then show for first levels.
        """
        item_type = item['Class']

        if item_type == 'Amulet':
            hidden_list = self.hidden_amulets
        elif item_type == 'Belt':
            hidden_list = self.hidden_belts
        else:
            hidden_list = self.hidden_rings

        # Determine level drop modifiers.
        rare_drop_modifier = filter_dict['base_drop_level'] + (filter_dict['level_rarity_modifier'] * 2)
        magic_drop_modifier = filter_dict['base_drop_level'] + filter_dict['level_rarity_modifier']
        normal_drop_modifier = filter_dict['base_drop_level']

        self.filter_file.write('\n\n# === {0}: {1} === #\n'.format(item_type, item['Name']))

        if item['Name'] not in hidden_list:
            # Display accessory normally.

            if self.debug:
                logger.info('Not hidden: {0}'.format(item['Name']))

            self.template.rare_item(base_text=item['Name'])
            self.template.uncommon_item(base_text=item['Name'])
            self.template.common_item(base_text=item['Name'])

        else:
            # Accessory set to always hide.
            # For some select accessories, we make an exception and show it for the first levels.

            if self.debug:
                logger.info('Hidden: {0}'.format(item['Name']))

            if item['Name'] in exception_list:
                # Exception. Show for first levels, as determined by base_drop_level and rarity_level_modifier.
                self.template.rare_item(
                    base_text=item['Name'],
                    item_level='<= {0}'.format(item['DropLevel'] + rare_drop_modifier),
                )
                self.template.uncommon_item(
                    base_text=item['Name'],
                    item_level='<= {0}'.format(item['DropLevel'] + magic_drop_modifier),
                )
                self.template.common_item(
                    base_text=item['Name'],
                    item_level='<= {0}'.format(item['DropLevel'] + normal_drop_modifier),
                )

            else:
                # Hide all other accessories.
                self.template.hidden_item(base_text=item['Name'])

    def parse_amulets(self):
        """
        Handle parsing for amulet items.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# -------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Amulets --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# -------------------------- #\n')
        self.filter_file.write('\n')

        if self.debug:
            logger.info('')
            logger.info('Handling amulets.')

        with open('resources/data/accessories/amulets.json', 'r') as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                self.handle_accessory(item, ['Coral Amulet', 'Paua Amulet'])

    def parse_belts(self):
        """
        Handle parsing for belt items.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------ #\n')
        self.filter_file.write('# --- [{0}.{1}] - Belts --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ------------------------ #\n')
        self.filter_file.write('\n')

        if self.debug:
            logger.info('')
            logger.info('Handling belts.')

        with open('resources/data/accessories/belts.json', 'r') as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                self.handle_accessory(item, ['Chain Belt', 'Rustic Sash', 'Leather Belt'])

    def parse_rings(self):
        """
        Handle parsing for ring items.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------ #\n')
        self.filter_file.write('# --- [{0}.{1}] - Rings --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ------------------------ #\n')
        self.filter_file.write('\n')

        if self.debug:
            logger.info('')
            logger.info('Handling rings.')

        with open('resources/data/accessories/rings.json', 'r') as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                self.handle_accessory(
                    item,
                    ['Coral Ring', 'Sapphire Ring', 'Topaz Ring', 'Ruby Ring', 'Two-Stone Ring']
                )
