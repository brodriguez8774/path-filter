"""
Python code to automatically generate a loot filter file for Path of Exile.
"""

# System Imports.
import argparse, json, os, sys

# User Imports.
from resources import logging as init_logging
from resources.parsers.accessories import AccessoryParser
from resources.parsers.currency import CurrencyParser, PreEquipment_CurrencyParser, PostEquipment_CurrencyParser
from resources.parsers.defense import DefenseParser
from resources.parsers.flasks import FlaskParser
from resources.parsers.gems import GemParser
from resources.parsers.jewels import JewelParser
from resources.parsers.maps import MapParser
from resources.parsers.other import FinalParser, NotableGearParser, QuestItemParser, UniqueParser
from resources.parsers.table_of_contents import TableOfContentsGenerator
from resources.parsers.weapons import WeaponParser
from resources.data.value_dictionary import filter_dict


# Initialize Logger.
logger = init_logging.get_logger(__name__)


defense_choices = ['A', 'Ev', 'En', 'A/Ev', 'Ev/En', 'A/En']
weapon_choices = ['Bows', 'Quivers', 'Sceptres', 'Wands', 'Shields']


def run_filter_generation():
    """
    Start of program.
    """
    # Define argument parsing.
    parser = define_argparse_args()

    # Attempt to parse passed args.
    args = parser.parse_args()

    # Determine if program should display help output or generate filter.
    amulet_help = get_amulet_help(args)
    belt_help = get_belt_help(args)
    ring_help = get_ring_help(args)

    if amulet_help or belt_help or ring_help:
        # At least one help arg passed. Display help and cancel filter generation.
        if amulet_help:
            display_amulet_help()

        if belt_help:
            display_belt_help()

        if ring_help:
            display_ring_help()

        logger.info('Cancelling filter generation.')
    else:
        # No help arg passed. Continue with actual filter generation.
        generate_filter(args)

def generate_filter(args ,test_mode=False):
    """
    Logic to actually generate filter file.
    :param args: Argparse args.
    :param test_mode: Debugging mode for testing specific sections of generation.
    """
    # Read in all arg values from user.
    debug = get_debug(args)
    file_name = get_file_name(args)
    defenses = get_defenses(args)
    weapons = get_weapons(args)
    shield_types = get_shield_types(args)
    base_drop_level = get_base_drop_level(args)
    level_rarity_modifier = get_level_rarity_modifier(args)
    hybrid_flask_bool = get_hybrid_flask_bool(args)
    hidden_amulets = get_hidden_amulets(args)
    hidden_belts = get_hidden_belts(args)
    hidden_rings = get_hidden_rings(args)

    # Display args.
    logger.info('')
    logger.info('Creating filter:')
    logger.info('    Filter Name: "{0}"'.format(file_name))
    logger.info('    Weapon Types: {0}'.format(weapons))
    if 'Shields' in weapons:
        logger.info('    Shield Types: {0}'.format(shield_types))
    logger.info('    Defense Types: {0}'.format(defenses))
    logger.info('')
    logger.info('    Drop Level Modifiers (from item base drop level):')
    logger.info('        Base:     +{0}'.format(base_drop_level))
    logger.info('        Magic:    +{0}'.format(base_drop_level + level_rarity_modifier))
    logger.info('        Rare:     +{0}'.format(base_drop_level + (level_rarity_modifier * 2)))
    logger.info('')
    if len(hidden_amulets) > 0 or len(hidden_belts) > 0 or len(hidden_rings) > 0:
        logger.info('    Note: For leveling purposes, some amulets/belts/rings will display')
        logger.info('          early on, even if set to ''"hidden".')
        if len(hidden_amulets) > 0:
            logger.info('    Hidden Amulets: {0}'.format(hidden_amulets))
        if len(hidden_belts) > 0:
            logger.info('    Hidden Belts: {0}'.format(hidden_belts))
        if len(hidden_rings) > 0:
            logger.info('    Hidden Rings: {0}'.format(hidden_rings))
        logger.info('')

    # Create generation folder, if not present.
    try:
        os.mkdir('./generated_filters')
    except FileExistsError:
        pass  # Folder already exists. This is fine.

    # Create filter.
    parse_num = 0
    with open('generated_filters/{0}'.format(file_name), "w") as filter_file:
        filter_file.write('\n')
        filter_file.write('# ======================= #\n')
        filter_file.write('# === POE Loot Filter === #\n')
        filter_file.write('# ======================= #\n')
        filter_file.write('#\n#\n')
        filter_file.write('# Generated with:\n')
        filter_file.write('#     Base Drop Level: {0}\n'.format(base_drop_level))
        filter_file.write('#     Level Rarity Modifier: {0}\n'.format(level_rarity_modifier))
        filter_file.write('#\n')
        filter_file.write('#     Weapons: {0}\n'.format(weapons))
        if 'Shields' in weapons:
            filter_file.write('#     Shields: {0}\n'.format(shield_types))
        filter_file.write('#     Defense: {0}\n'.format(defenses))
        filter_file.write('#     Hidden Amulets: {0}\n'.format(hidden_amulets))
        filter_file.write('#     Hidden Belts: {0}\n'.format(hidden_belts))
        filter_file.write('#     Hidden Rings: {0}\n'.format(hidden_rings))
        filter_file.write('#     Show Hybrid Flasks: {0}\n'.format(hybrid_flask_bool))
        filter_file.write('#\n')
        filter_file.write('# Original Command:\n')
        filter_file.write('#    python')
        orig_args = sys.argv
        for arg in orig_args:
            if 'main.py' in arg or arg[0] == '-':
                filter_file.write(' {0}'.format(arg))
            else:
                filter_file.write(' "{0}"'.format(arg))
        filter_file.write('\n#\n')

        filter_file.write('#\n#\n')

        if not test_mode:
            # Generate Table of Contents.
            parse_num += 1
            TableOfContentsGenerator(filter_file, weapons, defenses, shield_types, hybrid_flask_bool, debug=debug)

            # Generate Quest Item Filtering.
            parse_num += 1
            QuestItemParser(filter_file, parse_num, debug=debug)

            # Generate Unique Filtering.
            parse_num += 1
            UniqueParser(filter_file, parse_num, debug=debug)

            # Generate Currency Filtering.
            parse_num += 1
            CurrencyParser(filter_file, parse_num, debug=debug)

            # Generate Map Filtering.
            parse_num += 1
            MapParser(filter_file, parse_num, debug=debug)

            # Generate Gem Filtering.
            parse_num += 1
            GemParser(filter_file, parse_num, debug=debug)

            # Generate Jewel Filtering.
            parse_num += 1
            JewelParser(filter_file, parse_num, debug=debug)

            # Generate Flask Filtering.
            parse_num += 1
            FlaskParser(filter_file, parse_num, hybrid_flask_bool, debug=debug)

            # Generate Notable Gear Filtering.
            parse_num += 1
            NotableGearParser(filter_file, parse_num, debug=debug)

            # Generate Pre-Equipment Currency Filtering.
            parse_num += 1
            PreEquipment_CurrencyParser(filter_file, parse_num, debug=debug)

            # Generate Accessory Filtering.
            parse_num += 1
            AccessoryParser(
                filter_file,
                parse_num,
                hidden_amulets,
                hidden_belts,
                hidden_rings,
                base_drop_level,
                level_rarity_modifier,
                debug=debug,
            )

            # Generate Weapon Filtering.
            parse_num += 1
            WeaponParser(filter_file, parse_num, weapons, shield_types, base_drop_level, level_rarity_modifier, debug=debug)

            # Generate Defense Filtering.
            parse_num += 1
            DefenseParser(filter_file, parse_num, defenses, base_drop_level, level_rarity_modifier, debug=debug)

            # Generate Post-Equipment Currency Filtering.
            parse_num += 1
            PostEquipment_CurrencyParser(filter_file, parse_num, debug=debug)

            # Generate End-of-Filter filtering.
            parse_num += 1
            FinalParser(filter_file, parse_num, debug=debug)

        else:
            # Test mode. For debugging.

            # Hide all non-test items.
            FinalParser(filter_file, parse_num, debug=debug)

        logger.info('Created filter at "./generated_filters/{0}"'.format(file_name))


def define_argparse_args():
    """
    Defines and sets up argparse, to take in user-provided args.
    """
    parser = argparse.ArgumentParser(description='Generates a loot filter file for path of exile.')
    parser.add_argument(
        '-n', '--name',
        nargs='+',
        help='Name for loot filter. '
             'Defaults to "path.filter" if not specified.',
    )
    parser.add_argument(
        '-d', '--defense',
        nargs='+',
        choices=defense_choices,
        help='Use to define desired armor types to show. '
             'Default shows all types.',
    )
    parser.add_argument(
        '-w', '--weapons',
        nargs='+',
        choices=weapon_choices,
        help='Use to define desired weapon types to show. '
             'Default shows all types.',
    )
    parser.add_argument(
        '--shield_type',
        nargs='+',
        choices=defense_choices,
        help='Used to define desired shield types to show. '
             'Default shows all types.'
    )
    parser.add_argument(
        '--base_drop_level',
        nargs=1,
        type=int,
        help='Defines how many levels a weapon/armor item drop should display for, from when it starts spawning. '
             'Defaults to 10.'
    )
    parser.add_argument(
        '--level_rarity_modifier',
        nargs=1,
        type=int,
        help='Defines how many additional levels to display a weapon/armor item drop, based on rarity. '
             'Defaults to +5.'
    )
    parser.add_argument(
        '--show_hybrid_flasks',
        action='store_true',
        help='Determines if hybrid flasks should display or not. '
             'Defaults to false.'
    )
    parser.add_argument(
        '--hide_amulets',
        nargs='+',
        choices=get_amulet_list(),
        help='Hides all passed amulets from filtering. For list of amulets, use the "--amulet_help" arg.'
    )
    parser.add_argument(
        '--hide_belts',
        nargs='+',
        choices=get_belt_list(),
        help='Hides all passed belts from filtering. For list of belts, use the "--belt_help" arg.'
    )
    parser.add_argument(
        '--hide_rings',
        nargs='+',
        choices=get_ring_list(),
        help='Hides all passed rings from filtering. For list of rings, use the "--ring_help" arg.'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Runs program in debug mode. '
             'Defaults to false.',
    )
    parser.add_argument(
        '--amulet_help', '--amulets_help', '--help_amulets',
        action='store_true',
        help='Displays available amulets to hide with the "--hide_amulets" command. '
             'By default, all amulets display at all times.'
    )
    parser.add_argument(
        '--belt_help', '--belts_help', '--help_belts',
        action='store_true',
        help='Displays available belts to hide with the "--hide_belts" command. '
             'By default, all belts display at all times.'
    )
    parser.add_argument(
        '--ring_help', '--rings_help', '--help_rings',
        action='store_true',
        help='Displays available rings to hide with the "--hide_rings" command. '
             'By default, all rings display at all times.'
    )
    return parser


def get_debug(args):
    """
    Get program debug bool to determine if debug output is displayed for program.
    :param args: Argparse args.
    """
    if args.debug:
        return True
    else:
        return False


def get_file_name(args):
    """
    Get file name for generated loot filter.
    :param args: Argparse args.
    """
    if args.name is None:
        # Use default name.
        return 'path.filter'
    else:
        # Use user-provided name.
        file_name = ''
        for item in args.name:
            if file_name == '':
                file_name = item
            else:
                file_name += '_{0}'.format(item)

        # Ensure it ends with ".filter".
        if not file_name.endswith(".filter"):
            file_name += '.filter'

        return file_name


def get_defenses(args):
    """
    Get defense types to filter on.
    :param args: Argparse args.
    """
    if args.defense is None:
        # Default to showing all defense types.
        return defense_choices
    else:
        # Show user-specified defense types.
        return args.defense


def get_weapons(args):
    """
    Get weapon types to filter on.
    :param args: Argparse args.
    """
    if args.weapons is None:
        # Default to showing all weapon types.
        return weapon_choices
    else:
        # Show user-specified weapon types.
        return args.weapons


def get_shield_types(args):
    """
    Get shield types to filter on.
    :param args: Argparse args.
    """
    if args.shield_type is None:
        # Default to showing all shield types.
        return defense_choices
    else:
        # Show user-specified shield types.
        return args.shield_type


def get_base_drop_level(args):
    """
    Get base drop level value. For all weapon and armor types set to display, this (plus the original item drop level)
    determines how many levels the item will show for.
    :param args: Argparse args.
    """
    if args.base_drop_level is None:
        return filter_dict['base_drop_level']
    else:
        return args.base_drop_level[0]


def get_level_rarity_modifier(args):
    """
    Get level rarity modifier value. This is combined with the above "base drop level" to determine how many additional
    levels to show uncommon and rare items for. Uncommon items use this value directly, while rare multiply it by 2.
    :param args: Argparse args.
    """
    if args.level_rarity_modifier is None:
        return filter_dict['level_rarity_modifier']
    else:
        return args.level_rarity_modifier[0]


def get_hybrid_flask_bool(args):
    """
    Check for hybrid flasks display bool. Determines if hybrid flasks will display in filter or not.
    :param args: Argparse args.
    """
    if args.show_hybrid_flasks:
        return True
    else:
        return False


def get_amulet_help(args):
    """
    Checks for amulet help bool. If true, displays available belts to filter on for "--hide_amulets" arg and cancels
    filter creation.
    :param args: Argparse args.
    """
    if args.amulet_help:
        return True
    else:
        return False


def get_belt_help(args):
    """
    Checks for belt help bool. If true, displays available belts to filter on for "--hide_belts" arg and cancels
    filter creation.
    :param args: Argparse args.
    """
    if args.belt_help:
        return True
    else:
        return False


def get_ring_help(args):
    """
    Checks for ring help bool. If true, displays available belts to filter on for "--hide_rings" arg and cancels
    filter creation.
    :param args: Argparse args.
    """
    if args.ring_help:
        return True
    else:
        return False


def get_hidden_amulets(args):
    """
    Get hidden amulet list. Anything in this list will not show up in filtering.
    :param args: Argparse args.
    """
    if args.hide_amulets:
        return args.hide_amulets
    else:
        return []


def get_hidden_belts(args):
    """
    Get hidden belt list. Anything in this list will not show up in filtering.
    :param args: Argparse args.
    """
    if args.hide_belts:
        return args.hide_belts
    else:
        return []


def get_hidden_rings(args):
    """
    Get hidden ring list. Anything in this list will not show up in filtering.
    :param args: Argparse args.
    """
    if args.hide_rings:
        return args.hide_rings
    else:
        return []


def get_amulet_list():
    """
    Gets list of all amulets from json data.
    :return: List of all available amulets.
    """
    item_list = []
    with open('resources/data/accessories/amulets.json', 'r') as json_file:
        # Loop through all items in json.
        json_data = json.load(json_file)
        for item in json_data:
            item_list.append(item['Name'])

    return item_list


def get_belt_list():
    """
    Gets list of all belts from json data.
    :return: List of all available belts.
    """
    item_list = []
    with open('resources/data/accessories/belts.json', 'r') as json_file:
        # Loop through all items in json.
        json_data = json.load(json_file)
        for item in json_data:
            item_list.append(item['Name'])

    return item_list


def get_ring_list():
    """
    Gets list of all rings from json data.
    :return: List of all available rings.
    """
    item_list = []
    with open('resources/data/accessories/rings.json', 'r') as json_file:
        # Loop through all items in json.
        json_data = json.load(json_file)
        for item in json_data:
            item_list.append(item['Name'])

    return item_list


def display_amulet_help():
    """
    Displays helper list of all available amulets.
    """
    item_list = get_amulet_list()
    logger.info('Amulets:')
    for item in item_list:
        logger.info('    {0}'.format(item))
    logger.info('')


def display_belt_help():
    """
    Displays helper list of all available belts.
    """
    item_list = get_belt_list()
    logger.info('Belts:')
    for item in item_list:
        logger.info('    {0}'.format(item))
    logger.info('')


def display_ring_help():
    """
    Displays helper list of all available rings.
    """
    item_list = get_ring_list()
    logger.info('Rings:')
    for item in item_list:
        logger.info('    {0}'.format(item))
    logger.info('')


if __name__ == '__main__':
    logger.info('Starting program.')
    logger.info('')

    run_filter_generation()

    logger.info('')
    logger.info('Terminating program.')
