"""
Filter creation for all other items.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict
from resources.parsers.templates import FilterTemplates


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class QuestItemParser():
    """
    Filtering for all quest items.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# =========================== #\n')
        self.filter_file.write('# === [{0}] - Quest Items === #\n'.format(self.parse_num))
        self.filter_file.write('# =========================== #\n')
        self.filter_file.write('\n')

        self.template.quest_item(
            description='General Quest Items',
            class_text=['Quest', 'Quest Items', 'Pantheon Soul'],
        )

        self.template.quest_item(
            description='Atlas Quest Items',
            base_text='Watchstone',
        )


class UniqueParser():
    """
    Filtering for all uniques.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ============================ #\n')
        self.filter_file.write('# === [{0}] - Unique Items === #\n'.format(self.parse_num))
        self.filter_file.write('# ============================ #\n')
        self.filter_file.write('\n')

        # Unique Items.
        self.parse_uniques()

    def parse_uniques(self):
        """
        Filter parsing for unique items.
        """
        self.parse_subnum += 1

        # Unique tier maps.
        self.template.unique_item(
            description='Unique Tier Maps',
            class_text='Map',
            minimap_shape=display_dict['minimap_icon_maps'],
            sound='13 200',
        )

        # General Unique Items.
        self.template.unique_item(
            description='General Unique Items',
        )


class NotableGearParser():
    """
    Filtering for all extra-notable equipment drops that should show unconditionally.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ============================= #\n')
        self.filter_file.write('# === [{0}] - Notable Gear  === #\n'.format(self.parse_num))
        self.filter_file.write('# ============================= #\n')
        self.filter_file.write('\n')

        # 5 or 6 slot items.
        self.parse_high_slot()
        self.parse_influence()
        self.parse_veiled_items()
        self.parse_fishing_rods()

    def parse_high_slot(self):
        """
        Filter parsing for items with 5 or 6 slots.
        """
        self.parse_subnum += 1
        parse_subnum = str(self.parse_subnum).zfill(2)

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - High Slot Items --- #\n'.format(self.parse_num, parse_subnum))
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('\n')

        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}.01] - 6-Link Items --- #\n'.format(self.parse_num, parse_subnum))
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('\n')

        self.template.rare_item(
            linked_sockets='6',
            font_size=display_dict['important_font_size'],
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_slots'],
            sound='6 300',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.uncommon_item(
            linked_sockets='6',
            font_size=display_dict['important_font_size'],
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_slots'],
            sound='6 300',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.common_item(
            linked_sockets='6',
            font_size=display_dict['important_font_size'],
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_slots'],
            sound='6 300',
            playeffect=display_dict['minimap_color_notable'],
        )

        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}.02] - 5-Link Items --- #\n'.format(self.parse_num, parse_subnum))
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('\n')

        self.template.rare_item(
            linked_sockets='5',
            font_size=display_dict['unique_font_size'],
            minimap_size=1,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_slots'],
            sound='6 225',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.uncommon_item(
            linked_sockets='5',
            font_size=display_dict['unique_font_size'],
            minimap_size=1,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_slots'],
            sound='6 225',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.common_item(
            linked_sockets='5',
            font_size=display_dict['unique_font_size'],
            minimap_size=1,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_slots'],
            sound='6 225',
            playeffect=display_dict['minimap_color_notable'],
        )

        self.filter_file.write('\n')
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}.03] - 6 Slot Items --- #\n'.format(self.parse_num, parse_subnum))
        self.filter_file.write('# ---------------------------------- #\n')
        self.filter_file.write('\n')

        self.template.rare_item(
            sockets='6',
            font_size=display_dict['unique_font_size'],
            minimap_size=2,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_slots'],
            playeffect=display_dict['minimap_color_notable'],
            sound='6 175',
        )
        self.template.uncommon_item(
            sockets='6',
            font_size=display_dict['unique_font_size'],
            minimap_size=2,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_slots'],
            playeffect=display_dict['minimap_color_notable'],
            sound='6 175',
        )
        self.template.common_item(
            sockets='6',
            font_size=display_dict['unique_font_size'],
            minimap_size=2,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_slots'],
            playeffect=display_dict['minimap_color_notable'],
            sound='6 175',
        )

    def parse_influence(self):
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ----------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Influenced Items --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ----------------------------------- #\n')
        self.filter_file.write('\n')

        # General map influence types.
        self.template.rare_item(
            description='Map-Influenced Types',
            has_influence=['Shaper', 'Elder', 'Crusader', 'Hunter', 'Redeemer', 'Warlord'],
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.uncommon_item(
            description='Map-Influenced Types',
            has_influence=['Shaper', 'Elder', 'Crusader', 'Hunter', 'Redeemer', 'Warlord'],
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.common_item(
            description='Map-Influenced Types',
            has_influence=['Shaper', 'Elder', 'Crusader', 'Hunter', 'Redeemer', 'Warlord'],
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )

        # Fractured types.
        self.template.rare_item(
            description='Fractured Influence Types',
            is_fractured=True,
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.uncommon_item(
            description='Fractured Influence Types',
            is_fractured=True,
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.common_item(
            description='Fractured Influence Types',
            is_fractured=True,
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )

        # Synthesized types.
        self.template.rare_item(
            description='Synthesis Influence Types',
            is_synthesized=True,
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.uncommon_item(
            description='Synthesis Influence Types',
            is_synthesized=True,
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.common_item(
            description='Synthesis Influence Types',
            is_synthesized=True,
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )

        # Mirrored types.
        self.template.rare_item(
            description='Mirror Types',
            is_mirrored=True,
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.uncommon_item(
            description='Mirror Types',
            is_mirrored=True,
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.common_item(
            description='Mirror Types',
            is_mirrored=True,
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )

        # Replica types.
        self.template.rare_item(
            description='Replica Types',
            is_replica=True,
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.uncommon_item(
            description='Replica Types',
            is_replica=True,
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )
        self.template.common_item(
            description='Replica Types',
            is_replica=True,
            minimap_size=0,
            minimap_color=display_dict['minimap_color_notable'],
            minimap_shape=display_dict['minimap_icon_influenced'],
            sound='5 300',
            playeffect=display_dict['minimap_color_notable'],
        )

    def parse_veiled_items(self):
        """
        Handling for betrayal league veiled items.
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Veiled Items --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ------------------------------- #\n')
        self.filter_file.write('\n')

        self.template.special_item(
            has_mod='Veil',
        )

    def parse_fishing_rods(self):
        """
        Handling for fishing rods???
        """
        self.parse_subnum += 1

        self.filter_file.write('\n')
        self.filter_file.write('# ------------------------------- #\n')
        self.filter_file.write('# --- [{0}.{1}] - Fishing Rods --- #\n'.format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write('# ------------------------------- #\n')
        self.filter_file.write('\n')

        self.template.special_item(
            class_text='Fishing Rods',
        )


class FinalParser():
    """
    End of filter parsing.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ======================================= #\n')
        self.filter_file.write('# === [{0}] - Final/Cleanup Filtering === #\n'.format(self.parse_num))
        self.filter_file.write('# ======================================= #\n')
        self.filter_file.write('\n')

        # Hide any gear that has not yet been parsed.
        self.template.hidden_item(
            description='Hide remaining gear that has not yet been parsed.',
            base_text=["Helmets", "Body Armours", "Gloves", "Boots", "Ring", "Belt", "Amulet"]
        )

        # Kalguur gold currency.
        # Set here so that it will not accidentally make gear with text "gold" special.
        self.template.special_item(
            base_text='Gold',
        )

        # Hide everything else that has not yet been parsed.
        self.template.hidden_item(description='Hide everything else of little to no value')
