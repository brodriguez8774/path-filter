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
    'weapon': '75 75 75',

    # Font values.
    'unique_font_size': 50,
    'rare_font_size': 32,
    'uncommon_font_size': 25,
    'default_font_size': 20,
}
