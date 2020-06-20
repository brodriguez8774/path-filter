"""
Filter creation for accessories.
"""

# System Imports.

# User Imports.
from resources import logging as init_logging


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class AccessoryParser():

    def __init__(self, filter_file, parse_num, accessory_types):
        self.filter_file = filter_file
        self.parse_num = parse_num
        self.accessory_types = accessory_types
