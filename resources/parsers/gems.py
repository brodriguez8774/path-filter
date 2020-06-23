"""
Filter creation for gems.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict, filter_dict


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class GemParser():
    """
    Filtering for all gem drops.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ==================== #\n')
        self.filter_file.write('# === [{0}] - Gems === #\n'.format(self.parse_num))
        self.filter_file.write('# ==================== #\n')
        self.filter_file.write('\n')
