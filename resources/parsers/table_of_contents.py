"""
Filter creation for table of contents section.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class TableOfContentsGenerator():
    """
    Creates table of contents for filter file.
    """
    def __init__(self, filter_file, weapon_types, defense_types, shield_types, debug=False):
        # Set class vars.
        self.filter_file = filter_file
        self.weapon_types = weapon_types
        self.defense_types = defense_types
        self.shield_types = shield_types
        self.debug = debug

        self.generate_table_of_contents()

    def generate_table_of_contents(self):
        parse_num = 1

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ================================= #\n')
        self.filter_file.write('# === [{0}] - Table of Contents === #\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('# ================================= #\n')
        self.filter_file.write('\n')

        self.filter_file.write('# Use ctrl+f to jump to the indicated section.\n')
        self.filter_file.write('\n')

        self.filter_file.write('# [{0}] - Table of Contents\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('#\n')

        parse_num += 1
        self.filter_file.write('# [{0}] - Uniques\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('#\n')

        parse_num += 1
        self.filter_file.write('# [{0}] - Currency\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('#\n')

        parse_num += 1
        self.filter_file.write('# [{0}] - Maps\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('#\n')

        parse_num += 1
        self.filter_file.write('# [{0}] - Gems\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('#\n')

        parse_num += 1
        self.filter_file.write('# [{0}] - Flasks\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('#\n')

        parse_num += 1
        self.filter_file.write('# [{0}] - Notable Gear\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('# [{0}.01] - High Slot Items\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('# [{0}.01.01] - 6-Link Slot Items\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('# [{0}.01.02] - 5-Link Slot Items\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('#\n')

        parse_num += 1
        self.filter_file.write('# [{0}] - Pre-Equipment Currency Recipes\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('#\n')

        parse_num += 1
        self.filter_file.write('# [{0}] - Accessories\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('#\n')

        parse_num += 1
        self.filter_file.write('# [{0}] - Weapons\n'.format(str(parse_num).zfill(3)))

        parse_subnum = 0
        if 'Bows' in self.weapon_types:
            parse_subnum += 1
            self.filter_file.write('# [{0}.{1}] - Bows\n'.format(str(parse_num).zfill(3), str(parse_subnum).zfill(2)))

        if 'Quivers' in self.weapon_types:
            parse_subnum += 1
            self.filter_file.write('# [{0}.{1}] - Quivers\n'.format(
                str(parse_num).zfill(3),
                str(parse_subnum).zfill(2)),
            )

        if 'Wands' in self.weapon_types:
            parse_subnum += 1
            self.filter_file.write('# [{0}.{1}] - Wands\n'.format(str(parse_num).zfill(3), str(parse_subnum).zfill(2)))

        if 'Shields' in self.weapon_types:
            parse_subnum += 1
            self.filter_file.write('# [{0}.{1}] - Shields\n'.format(
                str(parse_num).zfill(3),
                str(parse_subnum).zfill(2)),
            )

            parse_subsubnum = 0
            if 'A' in self.shield_types:
                parse_subsubnum += 1
                self.filter_file.write('# [{0}.{1}.{2}] - A Shields\n'.format(
                    str(parse_num).zfill(3),
                    str(parse_subnum).zfill(2),
                    str(parse_subsubnum).zfill(2)),
                )

            if 'A/Ev' in self.shield_types:
                parse_subsubnum += 1
                self.filter_file.write('# [{0}.{1}.{2}] - A/Ev Shields\n'.format(
                    str(parse_num).zfill(3),
                    str(parse_subnum).zfill(2),
                    str(parse_subsubnum).zfill(2)),
                )

            if 'Ev' in self.shield_types:
                parse_subsubnum += 1
                self.filter_file.write('# [{0}.{1}.{2}] - Ev Shields\n'.format(
                    str(parse_num).zfill(3),
                    str(parse_subnum).zfill(2),
                    str(parse_subsubnum).zfill(2)),
                )

            if 'Ev/En' in self.shield_types:
                parse_subsubnum += 1
                self.filter_file.write('# [{0}.{1}.{2}] - Ev/En Shields\n'.format(
                    str(parse_num).zfill(3),
                    str(parse_subnum).zfill(2),
                    str(parse_subsubnum).zfill(2)),
                )

            if 'En' in self.shield_types:
                parse_subsubnum += 1
                self.filter_file.write('# [{0}.{1}.{2}] - En Shields\n'.format(
                    str(parse_num).zfill(3),
                    str(parse_subnum).zfill(2),
                    str(parse_subsubnum).zfill(2)),
                )

            if 'A/En' in self.shield_types:
                parse_subsubnum += 1
                self.filter_file.write('# [{0}.{1}.{2}] - A/En Shields\n'.format(
                    str(parse_num).zfill(3),
                    str(parse_subnum).zfill(2),
                    str(parse_subsubnum).zfill(2)),
                )

            self.filter_file.write('#\n')

        parse_num += 1
        self.filter_file.write('# [{0}] - Armors\n'.format(str(parse_num).zfill(3)))

        parse_subnum = 0
        if 'A' in self.defense_types:
            parse_subnum += 1
            self.filter_file.write('# [{0}.{1}] - A Armors\n'.format(
                str(parse_num).zfill(3),
                str(parse_subnum).zfill(2)),
            )

        if 'A/Ev' in self.defense_types:
            parse_subnum += 1
            self.filter_file.write('# [{0}.{1}] - A/Ev Armors\n'.format(
                str(parse_num).zfill(3),
                str(parse_subnum).zfill(2)),
            )

        if 'Ev' in self.defense_types:
            parse_subnum += 1
            self.filter_file.write('# [{0}.{1}] - Ev Armors\n'.format(
                str(parse_num).zfill(3),
                str(parse_subnum).zfill(2)),
            )

        if 'Ev/En' in self.defense_types:
            parse_subnum += 1
            self.filter_file.write('# [{0}.{1}] - Ev/En Armors\n'.format(
                str(parse_num).zfill(3),
                str(parse_subnum).zfill(2)),
            )

        if 'En' in self.defense_types:
            parse_subnum += 1
            self.filter_file.write('# [{0}.{1}] - En Armors\n'.format(
                str(parse_num).zfill(3),
                str(parse_subnum).zfill(2)),
            )

        if 'En/A' in self.defense_types:
            parse_subnum += 1
            self.filter_file.write('# [{0}.{1}] - En/A Armors\n'.format(
                str(parse_num).zfill(3),
                str(parse_subnum).zfill(2)),
            )

        self.filter_file.write('#\n')

        parse_num += 1
        self.filter_file.write('# [{0}] - Post-Equipment Currency Recipes\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('# [{0}.01] - RGB Linked (Chromatic Orb)\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('#\n')

        parse_num += 1
        self.filter_file.write('# [{0}] - Final/Cleanup Filtering\n'.format(str(parse_num).zfill(3)))
        self.filter_file.write('\n')
