"""
Filter creation for hand-held items.
"""

# System Imports.
import json

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict, filter_dict
from resources.parsers.templates import FilterTemplates


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class WeaponParser:
    def __init__(
        self, filter_file, parse_num, weapon_types, shield_types, base_drop_level, level_rarity_modifier, debug=False
    ):
        # Set class vars.
        self.filter_file = filter_file
        self.weapon_types = weapon_types
        self.shield_types = shield_types
        self.parse_num = str(parse_num).zfill(3)
        self.parse_subnum = 0
        self.template = FilterTemplates(filter_file, debug=debug)
        self.debug = debug

        # Update dict values.
        filter_dict["base_drop_level"] = base_drop_level
        filter_dict["level_rarity_modifier"] = level_rarity_modifier

        if self.debug:
            logger.info("weapon_types: {0}".format(self.weapon_types))
            logger.info("defense_types: {0}".format(self.shield_types))

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# ======================= #\n")
        self.filter_file.write("# === [{0}] - Weapons === #\n".format(self.parse_num))
        self.filter_file.write("# ======================= #\n")
        self.filter_file.write("\n")

        # Parse all weapon drops on selected weapons for low level socket connections.
        self.parse_low_level_sockets(weapon_types)

        # Handle for all present weapon types. Note that parse order is order that values show up in filter.
        if "OneHandMaces" in self.weapon_types:
            self.parse_one_hand_maces()

        if "TwoHandMaces" in self.weapon_types:
            self.parse_two_hand_maces()

        if "OneHandAxes" in self.weapon_types:
            self.parse_one_hand_axes()

        if "TwoHandAxes" in self.weapon_types:
            self.parse_two_hand_axes()

        if "Daggers" in self.weapon_types:
            self.parse_daggers()

        if "OneHandSwords" in self.weapon_types:
            self.parse_one_hand_swords()

        if "OneHandThrustingSwords" in self.weapon_types:
            self.parse_one_hand_thrusting_swords()

        if "TwoHandSwords" in self.weapon_types:
            self.parse_two_hand_swords()

        if "Claws" in self.weapon_types:
            self.parse_claws()

        if "Bows" in self.weapon_types:
            self.parse_bows()

        if "Quivers" in self.weapon_types:
            self.parse_quivers()

        if "Sceptres" in self.weapon_types:
            self.parse_sceptres()

        if "Wands" in self.weapon_types:
            self.parse_wands()

        if "Staves" in self.weapon_types:
            self.parse_staves()

        if "Shields" in self.weapon_types:
            self.parse_shields()

    def parse_low_level_sockets(self, weapon_types):
        """
        Parses low level armor for linked sockets.
        """
        if self.debug:
            logger.info("Parsing low level armor sockets.")

        self.parse_subnum += 1
        parse_subnum = str(self.parse_subnum).zfill(2)
        section_name = "Early Weapon Socket Links"
        padding_count = len(section_name) - 1

        for weapon in weapon_types:
            logger.info("WEAPON: {0}".format(weapon))

        three_link_weapon_slots = {}
        six_link_weapon_slots = {}
        selected_weapon_classes = []

        # Weapons tend to be directly tied to skills.
        # So only display linked weapons as indicated by the select type.
        if "OneHandMaces" in weapon_types:
            selected_weapon_classes.append("One Hand Maces")
            three_link_weapon_slots["One Hand Maces"] = "A"

        if "TwoHandMaces" in weapon_types:
            selected_weapon_classes.append("Two Hand Maces")
            three_link_weapon_slots["Two Hand Maces"] = "A"
            six_link_weapon_slots["Two Hand Maces"] = "A"

        if "OneHandAxes" in weapon_types:
            selected_weapon_classes.append("One Hand Axes")
            three_link_weapon_slots["One Hand Axes"] = "A/Ev"

        if "TwoHandAxes" in weapon_types:
            selected_weapon_classes.append("Two Hand Axes")
            three_link_weapon_slots["Two Hand Axes"] = "A/Ev"
            six_link_weapon_slots["Two Hand Axes"] = "A/Ev"

        if "Daggers" in weapon_types:
            selected_weapon_classes.append("Daggers")
            three_link_weapon_slots["Daggers"] = "Ev/En"

        if "OneHandSwords" in weapon_types:
            selected_weapon_classes.append("One Hand Swords")
            three_link_weapon_slots["One Hand Swords"] = "A/Ev"

        if "OneHandThrustingSwords" in weapon_types:
            selected_weapon_classes.append("Thrusting One Hand Swords")
            three_link_weapon_slots["Thrusting One Hand Swords"] = "Ev"

        if "TwoHandSwords" in weapon_types:
            selected_weapon_classes.append("Two Hand Swords")
            three_link_weapon_slots["Two Hand Swords"] = "A/Ev"
            six_link_weapon_slots["Two Hand Swords"] = "A/Ev"

        if "Claws" in weapon_types:
            selected_weapon_classes.append("Claws")
            three_link_weapon_slots["Claws"] = "Ev/En"

        if "Bows" in weapon_types:
            selected_weapon_classes.append("Bows")
            three_link_weapon_slots["Bows"] = "Ev"
            six_link_weapon_slots["Bows"] = "Ev"

        if "Sceptres" in weapon_types:
            selected_weapon_classes.append("Sceptres")
            three_link_weapon_slots["Sceptres"] = "En/A"

        if "Wands" in weapon_types:
            selected_weapon_classes.append("Wands")
            three_link_weapon_slots["Wands"] = "En"

        if "Staves" in weapon_types:
            selected_weapon_classes.append("Staves")
            three_link_weapon_slots["Staves"] = "En/A"
            six_link_weapon_slots["Staves"] = "En/A"

        if "Shields" in weapon_types:
            selected_weapon_classes.append("Shields")
            three_link_weapon_slots["Shields"] = None

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# --------------------{0} #\n".format("-" * padding_count))
        self.filter_file.write("# --- [{0}.{1}] - {2} --- #\n".format(self.parse_num, parse_subnum, section_name))
        self.filter_file.write("# --------------------{0} #\n".format("-" * padding_count))
        self.filter_file.write("\n")
        self.filter_file.write("# Displays more variety of low-level gear with good early socket connections.\n")
        self.filter_file.write("# To help builds out early game.\n")
        self.filter_file.write("\n")

        for weapon_class in selected_weapon_classes:
            weapon_class_attr = three_link_weapon_slots[weapon_class]

            # Filter for 3-socket max items early on.
            self.template.common_item(
                description="Early 3-Linked-Socket Linked RGB",
                class_text=weapon_class,
                item_level="<= 25",
                socket_group='"RGB"',
                background_color=display_dict[weapon_class_attr] if weapon_class_attr else None,
                border_color=display_dict["notable_border"],
                font_size=display_dict["rare_font_size"],
            )
            self.template.rare_item(
                description="Early 3-Linked-Socket Slot Rares",
                class_text=weapon_class,
                item_level="<= 25",
                linked_sockets="3",
                background_color=display_dict[weapon_class_attr] if weapon_class_attr else None,
                border_color=display_dict["notable_border"],
                font_size=display_dict["important_font_size"],
            )
            self.template.uncommon_item(
                description="Early 3-Linked-Socket Slot Uncommons",
                class_text=weapon_class,
                item_level="<= 25",
                linked_sockets="3",
                background_color=display_dict[weapon_class_attr] if weapon_class_attr else None,
                border_color=display_dict["notable_border"],
                font_size=display_dict["rare_font_size"],
            )
            self.template.common_item(
                description="Early 3-Linked-Socket Slot Normals",
                class_text=weapon_class,
                item_level="<= 25",
                linked_sockets="3",
                background_color=display_dict[weapon_class_attr] if weapon_class_attr else None,
                border_color=display_dict["notable_border"],
                font_size=display_dict["uncommon_font_size"],
            )

            # Weapons of 6 socket size.
            if len(six_link_weapon_slots) > 0:

                try:
                    weapon_class_attr = six_link_weapon_slots[weapon_class]

                    # Filter for 4-socket max items early on.
                    self.template.common_item(
                        description="Early 4-Linked-Socket Linked RGB",
                        class_text=weapon_class,
                        item_level="<= 40",
                        socket_group='"RGB"',
                        linked_sockets="4",
                        background_color=display_dict[weapon_class_attr],
                        border_color=display_dict["notable_border"],
                        font_size=display_dict["rare_font_size"],
                    )
                    self.template.rare_item(
                        description="Early 4-Linked-Socket Slot Rares",
                        class_text=weapon_class,
                        item_level="<= 40",
                        linked_sockets="4",
                        background_color=display_dict[weapon_class_attr],
                        border_color=display_dict["notable_border"],
                        font_size=display_dict["important_font_size"],
                    )
                    self.template.uncommon_item(
                        description="Early 4-Linked-Socket Slot Uncommons",
                        class_text=weapon_class,
                        item_level="<= 40",
                        linked_sockets="4",
                        background_color=display_dict[weapon_class_attr],
                        border_color=display_dict["notable_border"],
                        font_size=display_dict["rare_font_size"],
                    )
                    self.template.common_item(
                        description="Early 4-Linked-Socket Slot Normals",
                        class_text=weapon_class,
                        item_level="<= 40",
                        linked_sockets="4",
                        background_color=display_dict[weapon_class_attr],
                        border_color=display_dict["notable_border"],
                        font_size=display_dict["uncommon_font_size"],
                    )

                    # Filter for 5-socket max items early on.
                    self.template.common_item(
                        description="Early 5-Linked-Socket Linked RGB",
                        class_text=weapon_class,
                        item_level="<= 60",
                        socket_group='"RGB"',
                        linked_sockets="5",
                        background_color=display_dict[weapon_class_attr],
                        border_color=display_dict["notable_border"],
                        font_size=display_dict["important_font_size"],
                    )
                    self.template.rare_item(
                        description="Early 5-Linked-Socket Slot Rares",
                        class_text=weapon_class,
                        item_level="<= 60",
                        linked_sockets="5",
                        background_color=display_dict[weapon_class_attr],
                        border_color=display_dict["notable_border"],
                        font_size=display_dict["important_font_size"],
                    )
                    self.template.uncommon_item(
                        description="Early 5-Linked-Socket Slot Uncommons",
                        class_text=weapon_class,
                        item_level="<= 60",
                        linked_sockets="5",
                        background_color=display_dict[weapon_class_attr],
                        border_color=display_dict["notable_border"],
                        font_size=display_dict["rare_font_size"],
                    )
                    self.template.common_item(
                        description="Early 5-Linked-Socket Slot Normals",
                        class_text=weapon_class,
                        item_level="<= 60",
                        linked_sockets="5",
                        background_color=display_dict[weapon_class_attr],
                        border_color=display_dict["notable_border"],
                        font_size=display_dict["uncommon_font_size"],
                    )

                except KeyError:
                    # If we made it here, then weapon type only went up to 3 sockets max.
                    pass

    def parse_item(self, item, background_color):
        """
        Parses an individual item.
        :param item: The item to parse.
        :param background_color: Background color to give item.
        """
        # logger.info(item)
        self.filter_file.write("\n\n")
        self.filter_file.write("# === Item: {0} === #\n".format(item["Name"]))

        self.parse_item_rare(item, background_color)

        # Exclude for weapons that don't have slots.
        if item["Class"] != "Quiver":
            self.parse_item_max_slot(item, background_color)
            self.parse_item_rgb(item, background_color)

        self.parse_item_uncommon(item, background_color)
        self.parse_item_base(item, background_color)

    def parse_item_rare(self, item, background_color):
        """
        Handles filtering for rare version of item.
        :param item: The item to parse.
        :param background_color: Background color to give item.
        """
        drop_level = filter_dict["base_drop_level"] + (filter_dict["level_rarity_modifier"] * 2)

        if item["MaxLevel"] is True:
            self.template.rare_item(
                base_text=item["Name"],
                background_color=background_color,
            )
        else:
            self.template.rare_item(
                base_text=item["Name"],
                background_color=background_color,
                item_level="<= {0}".format(item["DropLevel"] + drop_level),
            )

    def parse_item_max_slot(self, item, background_color):
        """
        Handles filtering for max slot version of item.
        :param item: The item to parse.
        :param background_color: Background color to give item.
        """
        drop_level = filter_dict["base_drop_level"] + (filter_dict["level_rarity_modifier"] * 2)
        item_level = item["DropLevel"]

        if item_level <= 25:
            # Filter for 3-socket max items early on.
            self.template.common_item(
                description="Max Slot Type",
                base_text=item["Name"],
                item_level="<= {0}".format(item_level + drop_level),
                linked_sockets="3",
                background_color=background_color,
                border_color=display_dict["normal"],
                font_size=display_dict["uncommon_font_size"],
            )

        elif item_level <= 35:
            # Filter for 4-socket max items early on.
            self.template.common_item(
                description="Max Slot Type",
                base_text=item["Name"],
                item_level="<= {0}".format(item_level + drop_level),
                linked_sockets="3",
                background_color=background_color,
                border_color=display_dict["normal"],
                font_size=display_dict["uncommon_font_size"],
            )

    def parse_item_rgb(self, item, background_color):
        """
        Handles filtering for linked RGB version of item.
        :param item: The item to parse.
        :param background_color: Background color to give item.
        """
        drop_level = filter_dict["base_drop_level"]

        if item["MaxLevel"] is True:
            self.template.common_item(
                description="Linked RGB Type",
                base_text=item["Name"],
                socket_group='"RGB"',
                background_color=background_color,
                border_color=display_dict["normal"],
                font_size=display_dict["uncommon_font_size"],
            )
        else:
            self.template.common_item(
                description="Linked RGB Type",
                base_text=item["Name"],
                item_level="<= {0}".format(item["DropLevel"] + drop_level),
                socket_group='"RGB"',
                background_color=background_color,
                border_color=display_dict["normal"],
                font_size=display_dict["uncommon_font_size"],
            )

    def parse_item_uncommon(self, item, background_color):
        """
        Handles filtering for uncommon/magic version of item.
        :param item: The item to parse.
        :param background_color: Background color to give item.
        """
        drop_level = filter_dict["base_drop_level"] + filter_dict["level_rarity_modifier"]

        # Only explicitly show uncommons if low level.
        # Otherwise, they'll show up as currency drops if relevant.
        if item["DropLevel"] <= 25:
            if item["MaxLevel"] is True:
                self.template.uncommon_item(
                    base_text=item["Name"],
                    background_color=background_color,
                )
            else:
                self.template.uncommon_item(
                    base_text=item["Name"],
                    background_color=background_color,
                    item_level="<= {0}".format(item["DropLevel"] + drop_level),
                )

    def parse_item_base(self, item, background_color):
        """
        Handles filtering for standard version of item.
        :param item: The item to parse.
        :param background_color: Background color to give item.
        """
        drop_level = filter_dict["base_drop_level"]

        if item["MaxLevel"] is True:
            self.template.common_item(
                base_text=item["Name"],
                background_color=background_color,
            )
        else:
            self.template.common_item(
                base_text=item["Name"],
                background_color=background_color,
                item_level="<= {0}".format(item["DropLevel"] + drop_level),
            )

    def parse_one_hand_maces(self):
        """
        Parses all "One Hand Mace" type weapons.
        """
        if self.debug:
            logger.info("Parsing one handed maces.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# --------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - One Hand Maces --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# --------------------------------- #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/one_hand_maces.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["A"])

    def parse_two_hand_maces(self):
        """
        Parses all "Two Hand Mace" type weapons.
        """
        if self.debug:
            logger.info("Parsing two handed maces.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# --------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Two Hand Maces --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# --------------------------------- #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/two_hand_mace.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["A"])

    def parse_one_hand_axes(self):
        """
        Parses all "One Hand Axe" type weapons.
        """
        if self.debug:
            logger.info("Parsing one handed axes.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# -------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - One Hand Axes --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# -------------------------------- #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/one_hand_axes.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["A/Ev"])

    def parse_two_hand_axes(self):
        """
        Parses all "Two Hand Axe" type weapons.
        """
        if self.debug:
            logger.info("Parsing two handed axes.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# -------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Two Hand Axes --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# -------------------------------- #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/two_hand_axes.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["A/Ev"])

    def parse_daggers(self):
        """
        Parses all "Dagger" type weapons.
        """
        if self.debug:
            logger.info("Parsing daggers.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# -------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Daggers --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# -------------------------- #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/daggers.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["Ev/En"])

    def parse_one_hand_swords(self):
        """
        Parses all "OneHandSword" type weapons.
        """
        if self.debug:
            logger.info("Parsing one handed swords.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# ----------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - One Handed Swords --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ----------------------------------- #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/one_hand_swords.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["A/Ev"])

    def parse_one_hand_thrusting_swords(self):
        """
        Parses all "OneHandSword" type weapons.
        """
        if self.debug:
            logger.info("Parsing one handed thrusting swords.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# ----------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - One Handed Thrusting Swords --- #\n".format(
                self.parse_num, str(self.parse_subnum).zfill(2)
            )
        )
        self.filter_file.write("# ----------------------------------- #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/one_hand_thrusting_swords.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["Ev"])

    def parse_two_hand_swords(self):
        """
        Parses all "TwoHandSword" type weapons.
        """
        if self.debug:
            logger.info("Parsing two handed swords.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# ----------------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Two Handed Swords --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ----------------------------------- #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/two_hand_swords.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["A/Ev"])

    def parse_claws(self):
        """
        Parses all "Claw" type weapons.
        """
        if self.debug:
            logger.info("Parsing claws.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# ------------------------ #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Claws --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ------------------------ #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/claws.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["Ev/En"])

    def parse_bows(self):
        """
        Parses all "Bow" type weapons.
        """
        if self.debug:
            logger.info("Parsing bows.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# ----------------------- #\n")
        self.filter_file.write("# --- [{0}.{1}] - Bows --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2)))
        self.filter_file.write("# ----------------------- #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/bows.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["Ev"])

    def parse_quivers(self):
        """
        Parses all "Quiver" type weapons.
        """
        if self.debug:
            logger.info("Parsing quivers.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# -------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Quivers --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# -------------------------- #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/quivers.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["Ev"])

    def parse_sceptres(self):
        """
        Parses all "Sceptre" type weapons.
        """
        if self.debug:
            logger.info("Parsing sceptres.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# --------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Sceptres --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# --------------------------- #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/sceptres.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["En/A"])

    def parse_wands(self):
        """
        Parses all "Wand" type weapons.
        """
        if self.debug:
            logger.info("Parsing wands.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# ------------------------ #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Wands --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ------------------------ #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/wands.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["En"])

    def parse_staves(self):
        """
        Parses all "Staff" type weapons.
        """
        if self.debug:
            logger.info("Parsing staves.")

        self.parse_subnum += 1

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# ------------------------ #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Staves --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# ------------------------ #\n")
        self.filter_file.write("\n")

        # Parse wands.
        with open("resources/data/hand/staves.json", "r") as json_file:
            # Loop through all items in json.
            json_data = json.load(json_file)
            for item in json_data:
                # Parse item.
                self.parse_item(item, display_dict["En/A"])

    def parse_shields(self):
        """
        Parses all "Shield" type items, based on selected defenses.
        """
        if self.debug:
            logger.info("Parsing Shields.")

        self.parse_subnum += 1
        subsubnum = 0

        # Section Start.
        self.filter_file.write("\n")
        self.filter_file.write("# -------------------------- #\n")
        self.filter_file.write(
            "# --- [{0}.{1}] - Shields --- #\n".format(self.parse_num, str(self.parse_subnum).zfill(2))
        )
        self.filter_file.write("# -------------------------- #\n")
        self.filter_file.write("\n")

        if "A" in self.shield_types:
            # Parse Armor shields.
            subsubnum += 1

            self.filter_file.write("\n")
            self.filter_file.write("# ------------------------------ #\n")
            self.filter_file.write(
                "# --- [{0}.{1}.{2}] - A Shields --- #\n".format(
                    self.parse_num, str(self.parse_subnum).zfill(2), subsubnum
                )
            )
            self.filter_file.write("# ------------------------------ #\n")
            self.filter_file.write("\n")

            with open("resources/data/hand/shields/A.json", "r") as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item, display_dict["A"])

        if "A/Ev" in self.shield_types:
            # Parse Armor/Evasion shields.
            subsubnum += 1

            self.filter_file.write("\n")
            self.filter_file.write("# --------------------------------- #\n")
            self.filter_file.write(
                "# --- [{0}.{1}.{2}] - A/Ev Shields --- #\n".format(
                    self.parse_num, str(self.parse_subnum).zfill(2), subsubnum
                )
            )
            self.filter_file.write("# --------------------------------- #\n")
            self.filter_file.write("\n")

            with open("resources/data/hand/shields/A_Ev.json", "r") as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item, display_dict["A/Ev"])

        if "Ev" in self.shield_types:
            # Parse Evasion shields.
            subsubnum += 1

            self.filter_file.write("\n")
            self.filter_file.write("# ------------------------------- #\n")
            self.filter_file.write(
                "# --- [{0}.{1}.{2}] - Ev Shields --- #\n".format(
                    self.parse_num, str(self.parse_subnum).zfill(2), subsubnum
                )
            )
            self.filter_file.write("# ------------------------------- #\n")
            self.filter_file.write("\n")

            with open("resources/data/hand/shields/Ev.json", "r") as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item, display_dict["Ev"])

        if "Ev/En" in self.shield_types:
            # Parse Evasion/Energy Shield shields.
            subsubnum += 1

            self.filter_file.write("\n")
            self.filter_file.write("# ---------------------------------- #\n")
            self.filter_file.write(
                "# --- [{0}.{1}.{2}] - Ev/En Shields --- #\n".format(
                    self.parse_num, str(self.parse_subnum).zfill(2), subsubnum
                )
            )
            self.filter_file.write("# ---------------------------------- #\n")
            self.filter_file.write("\n")

            with open("resources/data/hand/shields/Ev_En.json", "r") as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item, display_dict["Ev/En"])

        if "En" in self.shield_types:
            # Parse Energy Shield shields.
            subsubnum += 1

            self.filter_file.write("\n")
            self.filter_file.write("# ------------------------------- #\n")
            self.filter_file.write(
                "# --- [{0}.{1}.{2}] - En Shields --- #\n".format(
                    self.parse_num, str(self.parse_subnum).zfill(2), subsubnum
                )
            )
            self.filter_file.write("# ------------------------------- #\n")
            self.filter_file.write("\n")

            with open("resources/data/hand/shields/En.json", "r") as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item, display_dict["En"])

        if "En/A" in self.shield_types:
            # Parse Armor/Energy Shield shields.
            subsubnum += 1

            self.filter_file.write("\n")
            self.filter_file.write("# --------------------------------- #\n")
            self.filter_file.write(
                "# --- [{0}.{1}.{2}] - En/A Shields --- #\n".format(
                    self.parse_num, str(self.parse_subnum).zfill(2), subsubnum
                )
            )
            self.filter_file.write("# --------------------------------- #\n")
            self.filter_file.write("\n")

            with open("resources/data/hand/shields/En_A.json", "r") as json_file:
                # Loop through all items in json.
                json_data = json.load(json_file)
                for item in json_data:
                    # Parse item.
                    self.parse_item(item, display_dict["En/A"])
