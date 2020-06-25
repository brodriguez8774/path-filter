"""
Python code to automatically generate a loot filter file for Path of Exile.
"""

# System Imports.
import argparse, os

# User Imports.
from resources import logging as init_logging
from resources.parsers.accessories import AccessoryParser
from resources.parsers.currency import CurrencyParser, PreEquipment_CurrencyParser, PostEquipment_CurrencyParser
from resources.parsers.defense import DefenseParser
from resources.parsers.flasks import FlaskParser
from resources.parsers.gems import GemParser
from resources.parsers.jewels import JewelParser
from resources.parsers.maps import MapParser
from resources.parsers.other import FinalParser, NotableGearParser, UniqueParser
from resources.parsers.table_of_contents import TableOfContentsGenerator
from resources.parsers.weapons import WeaponParser
from resources.data.value_dictionary import filter_dict


# Initialize Logger.
logger = init_logging.get_logger(__name__)


defense_choices = ['A', 'Ev', 'En', 'A/Ev', 'Ev/En', 'A/En']
weapon_choices = ['Bows', 'Quivers', 'Wands', 'Shields']


def run_filter_generation():
    """
    Start of program.
    """
    # Define argument parsing.
    parser = define_argparse_args()

    # Attempt to parse passed args.
    args = parser.parse_args()

    # Read in all arg values from user.
    debug = get_debug(args)
    file_name = get_file_name(args)
    defenses = get_defenses(args)
    weapons = get_weapons(args)
    shield_types = get_shield_types(args)
    base_drop_level = get_base_drop_level(args)
    level_rarity_modifier = get_level_rarity_modifier(args)
    hybrid_flask_bool = get_hybrid_flask_bool(args)

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
    logger.info('        Uncommon: +{0}'.format(base_drop_level + level_rarity_modifier))
    logger.info('        Rare:     +{0}'.format(base_drop_level + (level_rarity_modifier * 2)))
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
        filter_file.write('\n\n')
        filter_file.write('# Generated with:\n')
        filter_file.write('#     Weapons: {0}\n'.format(weapons))
        if 'Shields' in weapons:
            filter_file.write('#     Shields: {0}\n'.format(shield_types))
        filter_file.write('#     Defense: {0}\n'.format(defenses))
        filter_file.write('\n\n')

        # Generate Table of Contents.
        parse_num += 1
        TableOfContentsGenerator(filter_file, weapons, defenses, shield_types, hybrid_flask_bool, debug=debug)

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
        AccessoryParser(filter_file, parse_num, defenses, debug=debug)

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
        '--debug',
        action='store_true',
        help='Runs program in debug mode. '
             'Defaults to false.',
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


if __name__ == '__main__':
    logger.info('Starting program.')
    logger.info('')

    run_filter_generation()

    logger.info('')
    logger.info('Terminating program.')
