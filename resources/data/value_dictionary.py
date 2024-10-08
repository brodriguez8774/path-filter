"""
Dictionary of general values used repeatedly in program.
"""

# Dictionary for filter value variables.
filter_dict = {
    # Leveling attributes.
    "base_drop_level": 15,  # By default, show items that are within 10 levels of the initial drop level.
    "level_rarity_modifier": 5,  # By default, show uncommon by +5 levels above and rare by +10 levels above.
}


# Dictionary for display value variables.
display_dict = {
    # "Standard" in game colors.
    "normal": "200 200 200",
    "uncommon": "136 136 255",
    "rare": "255 255 199",
    "unique": "175 96 37",
    "text": "127 127 127",
    "quest": "74 230 58",
    # Custom armor-class colors.
    "A": "92 10 10",  # 5c0a0a
    "A/Ev": "92 78 10",  # 5c4e0a
    "Ev": "10 92 28",  # 0a5c1c
    "Ev/En": "10 81 92",  # 0a515c
    "En": "22 10 92",  # 160a5c
    "En/A": "48 3 48",  # 5c0a5c
    # Custom other colors.
    "standard_background": "25 25 25",
    "dark_grey_background": "75 75 75",
    "unique_background": "66 30 30",
    "normal_border": "140 140 140",
    "notable_border": "220 220 220",
    "rare_currency_border": "255 215 0",
    "currency_orb_border": "0 0 0",
    "league_border": "128 0 128",
    "card_border": "14 186 255",
    "normal_text": "140 140 140",
    "notable_text": "200 200 200",
    "uncommon_text": "136 136 255",
    "rare_text": "255 255 119",
    "unique_text": "175 96 37",
    "currency_text": "255 215 0",
    "league_text": "184 0 184",
    "card_text": "14 186 255",
    # Font values.
    "unique_font_size": 50,
    "important_font_size": 40,
    "rare_font_size": 32,
    "uncommon_font_size": 25,
    "default_font_size": 20,
    "min_font_size": 18,
    # Minimap icon values.
    "minimap_icon_currency": "Circle",  # General currency.
    "minimap_icon_maps": "Square",  # Map items.
    "minimap_icon_slots": "Pentagon",  # 5 or 6 slot items.
    "minimap_icon_special": "Triangle",  # League drops and other rare/special things.
    "minimap_icon_unique": "UpsideDownHouse",  # Unique items.
    "minimap_icon_flasks": "Raindrop",  # Flask items.
    "minimap_icon_jewel": "Hexagon",  # Jewel items.
    "minimap_icon_influenced": "Diamond",  # Influenced items.
    # Minimap color values.
    "minimap_color_currency": "White",  # General currency.
    "minimap_color_maps": "White",  # Map items.
    "minimap_color_notable": "Yellow",  # Notable Gear Drops.
    "minimap_color_special": "Purple",  # League currency and other rare things.
    "minimap_color_unique": "Orange",  # Unique items.
    "minimap_color_flasks": "Blue",  # Flask items.
}
