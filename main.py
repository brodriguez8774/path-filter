"""
Python code to automatically generate a loot filter file for Path of Exile.
"""

# System Imports.
import argparse

# User Imports.
from resources import logging as init_logging


# Initialize Logger.
logger = init_logging.get_logger(__name__)




if __name__ == '__main__':
    logger.info('Starting program.')
    logger.info('')

    # Define argument parsing.
    parser = argparse.ArgumentParser(description='Generates a loot filter file for path of exile.')
    parser.add_argument(
        '-d', '--defense',
        nargs='+',
        choices=['A', 'Ev', 'En', 'A/Ev', 'Ev/En', 'A/En'],
        help='Use to define desired armor types to show. Default shows all types.'
    )
    parser.add_argument(
        '-w', '--weapons',
        nargs='+',
        choices=['Wands', 'Shields'],
        help='Use to define desired weapon types to show. Default shows all types.'
    )

    # Attempt to parse passed args.
    args = parser.parse_args()

    # Display args.
    logger.info('Parsed args:')
    logger.info('{0}'.format(args))
    logger.info('{0}'.format(args.defense))
    logger.info('{0}'.format(args.weapons))

    logger.info('')
    logger.info('Terminating program.')
