"""
Filter creation for maps.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict
from resources.parsers.templates import FilterTemplates


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class MapParser():
    """
    Filtering for all map drops.
    """
    def __init__(self, filter_file, parse_num, debug=False):
        self.filter_file = filter_file
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
        self.debug = debug

        # Section Start.
        self.filter_file.write('\n')
        self.filter_file.write('# ==================== #\n')
        self.filter_file.write('# === [{0}] - Maps === #\n'.format(self.parse_num))
        self.filter_file.write('# ==================== #\n')
        self.filter_file.write('\n')

        self.generate_map_filter()

    def generate_map_filter(self):
        """
        Generates filtering for all map types.
        """
        # High quality maps.
        self.template.notable_item(
            description='High Quality Maps',
            class_text='Map',
            quality='>= 10',
            font_size=display_dict['rare_font_size'],
            minimap_size=1,
            minimap_color=display_dict['minimap_color_maps'],
            minimap_shape=display_dict['minimap_icon_maps'],
            sound='13 250',
            playeffect=display_dict['minimap_color_maps'],
        )

        # High tier maps.
        self.template.notable_item(
            description='High Tier Maps',
            class_text='Map',
            map_tier='>= 11',
            font_size=display_dict['rare_font_size'],
            minimap_size=0,
            minimap_color=display_dict['minimap_color_maps'],
            minimap_shape=display_dict['minimap_icon_maps'],
            sound='13 250',
            playeffect=display_dict['minimap_color_maps'],
        )

        # Medium tier maps.
        self.template.notable_item(
            description='Medium Tier Maps',
            class_text='Map',
            map_tier='>= 6',
            font_size=display_dict['uncommon_font_size'],
            minimap_size=1,
            minimap_color=display_dict['minimap_color_maps'],
            minimap_shape=display_dict['minimap_icon_maps'],
            sound='13 225',
            playeffect=display_dict['minimap_color_maps'],
        )

        # Low tier maps.
        self.template.notable_item(
            description='Low Tier Maps',
            class_text=['Map', 'Map Fragments', 'Misc Map Items'],
            font_size=display_dict['default_font_size'],
            minimap_size=1,
            minimap_color=display_dict['minimap_color_maps'],
            minimap_shape=display_dict['minimap_icon_maps'],
            sound='13 200',
            playeffect=display_dict['minimap_color_maps'],
        )

        # Misc map items.
        self.template.notable_item(
            description='Misc Map Item Classes',
            class_text=[
                "Vault Keys",
            ],
            font_size=display_dict['rare_font_size'],
        )
        self.template.notable_item(
            description='Misc Map Item Bases',
            base_text=[
                "Reliquary Key", "Chronicle of Atzoatl", "Inscribed Ultimatum", "Mirrored Tablet", "Primeval Remnant",
                "Primordial Remnant",
            ],
            font_size=display_dict['rare_font_size'],
        )

        # Map-like items.
        self.template.notable_item(
            description='Map-like Item Classes',
            class_text=[
                "Blueprints", "Contracts", "Memories", "Sanctum Research",
            ],
            font_size=display_dict['rare_font_size'],
        )
        self.template.notable_item(
            description='Map-like Item Bases',
            class_text=[
                "Expedition Logbook",
            ],
            font_size=display_dict['rare_font_size'],
        )
