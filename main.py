"""
Python code to automatically generate a loot filter file for Path of Exile.
"""

# System Imports.
import argparse, os

# User Imports.
from resources import logging as init_logging
from resources.parsers.accessories import AccessoryParser
from resources.parsers.defense import DefenseParser
from resources.parsers.weapons import WeaponParser


# Initialize Logger.
logger = init_logging.get_logger(__name__)


if __name__ == '__main__':
    logger.info('Starting program.')
    logger.info('')

    defense_choices = ['A', 'Ev', 'En', 'A/Ev', 'Ev/En', 'A/En']
    weapon_choices = ['Bows', 'Quivers', 'Wands', 'Shields']

    # Define argument parsing.
    parser = argparse.ArgumentParser(description='Generates a loot filter file for path of exile.')
    parser.add_argument(
        '-n', '--name',
        nargs='+',
        help='Name for loot filter. Defaults to "path.filter" if not specified.',
    )
    parser.add_argument(
        '-d', '--defense',
        nargs='+',
        choices=defense_choices,
        help='Use to define desired armor types to show. Default shows all types.',
    )
    parser.add_argument(
        '-w', '--weapons',
        nargs='+',
        choices=weapon_choices,
        help='Use to define desired weapon types to show. Default shows all types.',
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Runs program in debug mode.',
    )

    # Attempt to parse passed args.
    args = parser.parse_args()

    if args.debug:
        debug = True
    else:
        debug = False

    if args.name is None:
        # Use default name.
        file_name = 'path.filter'
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

    if args.defense is None:
        # Default to showing all defense types.
        defense = defense_choices
    else:
        # Show user-specified defense types.
        defense = args.defense

    if args.weapons is None:
        # Default to showing all weapon types.
        weapons = weapon_choices
    else:
        # Show user-specified weapon types.
        weapons = args.weapons

    # Display args.
    logger.info('')
    logger.info('Creating filter:')
    logger.info('    Filter Name: "{0}"'.format(file_name))
    logger.info('    Weapon Types: {0}'.format(weapons))
    logger.info('    Defense Types: {0}'.format(defense))
    logger.info('')

    # Create generation folder, if not present.
    try:
        os.mkdir('./generated_filters')
    except FileExistsError:
        pass    # Folder already exists. This is fine.

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
        filter_file.write('#     Defense: {0}\n'.format(defense))
        filter_file.write('\n\n')

        # Generate Weapon Filtering.
        parse_num += 1
        WeaponParser(filter_file, parse_num, weapons, defense, debug=debug)

        # Generate Defense Filtering.
        parse_num += 1
        DefenseParser(filter_file, parse_num, defense, debug=debug)

    logger.info('')
    logger.info('Created filter at "./generated_filters/{0}"'.format(file_name))
    logger.info('Terminating program.')
