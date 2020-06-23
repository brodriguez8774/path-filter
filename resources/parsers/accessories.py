"""
Filter creation for accessories.
"""

# System Imports.

# User Imports.
from resources import logging as init_logging


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class AccessoryParser():

    def __init__(self, filter_file, parse_num, accessory_types, debug=False):
        self.filter_file = filter_file
        self.accessory_types = accessory_types
        self.parse_num = str(parse_num).zfill(2)

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ========================== #\n')
        self.filter_file.write('# === [{0}] - Accessories === #\n'.format(self.parse_num))
        self.filter_file.write('# ========================== #\n')
        self.filter_file.write('\n')
