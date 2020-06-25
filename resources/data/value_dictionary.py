"""
Dictionary of general values used repeatedly in program.
"""


# Dictionary for filter value variables.
filter_dict = {
# Leveling attributes.
    'base_drop_level': 10,     # By default, show items that are within 10 levels of the initial drop level.
    'level_rarity_modifier': 5,    # By default, show uncommon by +5 levels above and rare by +10 levels above.
}


# Dictionary for display value variables.
display_dict = {
    # "Standard" in game colors.
    'normal': '200 200 200',
    'magic': '136 136 255',
    'rare': '255 255 199',
    'unique': '175 96 37',
    'text': '127 127 127',

    # Custom armor-class colors.
    'A': '48 3 3',
    'A/Ev': '73 73 4',
    'Ev': '3 48 26',
    'Ev/En': '3 33 48',
    'En': '10 3 48',
    'En/A': '48 3 48',

    # Custom other colors.
    'unique_background': '66 30 30',
    'unique_text_color': '175 96 37',
    'standard_background': '25 25 25',
    'weapon': '75 75 75',
    'currency_text': '218 190 147',
    'normal_important_text': '255 255 255',
    'uncommon_important_text': '136 136 255',
    'rare_important_text': '255 255 119',
    'league_border': '128 0 128',
    'league_text': '184 0 184',

    # Font values.
    'unique_font_size': 50,
    'important_font_size': 40,
    'rare_font_size': 32,
    'uncommon_font_size': 25,
    'default_font_size': 20,
    'min_font_size': 18,

    # Minimap icon values.
    'minimap_icon_currency': 'Circle',          # General currency.
    'minimap_icon_maps': 'Square',              # Map items.
    'minimap_icon_slots': 'Pentagon',           # 5 or 6 slot items.
    'minimap_icon_special': 'Triangle',         # League drops and other rare/special things.
    'minimap_icon_unique': 'UpsideDownHouse',   # Unique items.
    'minimap_icon_flasks': 'Raindrop',          # Flask items.
    'minimap_icon_jewel': 'Hexagon',            # Jewel items.
    'minimap_icon_influenced': 'Diamond',       # Influenced items.

    # Minimap color values.
    'minimap_color_currency': 'White',          # General currency.
    'minimap_color_maps': 'White',              # Map items.
    'minimap_color_notable': 'Yellow',            # Notable Gear Drops.
    'minimap_color_special': 'Purple',          # League currency and other rare things.
    'minimap_color_unique': 'Orange',           # Unique items.
    'minimap_color_flasks': 'Blue',             # Flask items.
}
