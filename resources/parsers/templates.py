"""
General filter templates to make filters more consistent.
"""

# System Imports.

# User Imports.
from resources import logging as init_logging
from resources.data.value_dictionary import display_dict


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class FilterTemplates():
    def __init__(self, filter_file, debug=False):
        self.filter_file = filter_file
        self.base = BaseTemplate(filter_file, debug)
        self.debug = debug

        if debug:
            logger.info('Initializing FilterTemplates class.')

    def unique_item(self, *args,
            description='Unique Type', class_text=None, base_text=None,
            quality=None,
            linked_sockets=None, socket_group=None, sockets=None,
            height=None, width=None,
            has_influence=None, map_tier=None,
            background_color=display_dict['unique_background'], border_color=display_dict['unique'],
            text_color=display_dict['unique_text'], font_size=display_dict['unique_font_size'],
            minimap_size=0, minimap_color=display_dict['minimap_color_unique'],
            minimap_shape=display_dict['minimap_icon_unique'],
            sound='1 300', playeffect=display_dict['minimap_color_unique']):
        """
        General filtering template for unique items.
        """
        self.base.write_rule(
            description=description, class_text=class_text, base_text=base_text,
            rarity='Unique', quality=quality,
            linked_sockets=linked_sockets, socket_group=socket_group, sockets=sockets,
            height=height, width=width,
            has_influence=has_influence, map_tier=map_tier,
            background_color=background_color, border_color=border_color,
            text_color=text_color, font_size=font_size,
            minimap_size=minimap_size, minimap_color=minimap_color, minimap_shape=minimap_shape,
            sound=sound, playeffect=playeffect,
        )

    def rare_item(self, *args,
            description='Rare Type', class_text=None, base_text=None,
            item_level=None, quality=None,
            linked_sockets=None, socket_group=None, sockets=None,
            height=None, width=None,
            has_influence=None, map_tier=None,
            background_color=display_dict['standard_background'], border_color=display_dict['rare'],
            text_color=display_dict['rare_text'], font_size=display_dict['rare_font_size'],
            minimap_size=None, minimap_color=None, minimap_shape=None,
            sound=None, playeffect=None):
        """
        General filtering template for rare items.
        """
        self.base.write_rule(
            description=description, class_text=class_text, base_text=base_text,
            item_level=item_level, rarity='Rare', quality=quality,
            linked_sockets=linked_sockets, socket_group=socket_group, sockets=sockets,
            height=height, width=width,
            has_influence=has_influence, map_tier=map_tier,
            background_color=background_color, border_color=border_color,
            text_color=text_color, font_size=font_size,
            minimap_size=minimap_size, minimap_color=minimap_color, minimap_shape=minimap_shape,
            sound=sound, playeffect=playeffect,
        )

    def uncommon_item(self, *args,
            description='Magic Type', class_text=None, base_text=None,
            item_level=None, quality=None,
            linked_sockets=None, socket_group=None, sockets=None,
            height=None, width=None,
            has_influence=None, map_tier=None,
            background_color=display_dict['standard_background'], border_color=display_dict['uncommon'],
            text_color=display_dict['uncommon_text'], font_size=display_dict['uncommon_font_size'],
            minimap_size=None, minimap_color=None, minimap_shape=None,
            sound=None, playeffect=None):
        """
        General filtering template for magic/uncommon items.
        """
        self.base.write_rule(
            description=description, class_text=class_text, base_text=base_text,
            item_level=item_level, rarity='Magic', quality=quality,
            linked_sockets=linked_sockets, socket_group=socket_group, sockets=sockets,
            height=height, width=width,
            has_influence=has_influence, map_tier=map_tier,
            background_color=background_color, border_color=border_color,
            text_color=text_color, font_size=font_size,
            minimap_size=minimap_size, minimap_color=minimap_color, minimap_shape=minimap_shape,
            sound=sound, playeffect=playeffect,
        )

    def common_item(self, *args,
            description='Common Type', class_text=None, base_text=None,
            item_level=None, quality=None,
            linked_sockets=None, socket_group=None, sockets=None,
            height=None, width=None,
            has_influence=None, map_tier=None,
            background_color=display_dict['standard_background'], border_color=display_dict['normal'],
            text_color=display_dict['normal_text'], font_size=display_dict['default_font_size'],
            minimap_size=None, minimap_color=None, minimap_shape=None,
            sound=None, playeffect=None):
        """
        General filtering template for common/normal items.
        """
        self.base.write_rule(
            description=description, class_text=class_text, base_text=base_text,
            item_level=item_level, quality=quality,
            linked_sockets=linked_sockets, socket_group=socket_group, sockets=sockets,
            height=height, width=width,
            has_influence=has_influence, map_tier=map_tier,
            background_color=background_color, border_color=border_color,
            text_color=text_color, font_size=font_size,
            minimap_size=minimap_size, minimap_color=minimap_color, minimap_shape=minimap_shape,
            sound=sound, playeffect=playeffect,
        )

    def rare_currency(self, *args,
            description=None, class_text=None, base_text=None,
            background_color=display_dict['standard_background'], border_color=display_dict['currency_border'],
            text_color=display_dict['currency_text'], font_size=display_dict['rare_font_size'],
            minimap_size=0, minimap_color=display_dict['minimap_color_currency'],
            minimap_shape=display_dict['minimap_icon_currency'],
            sound='4 175', playeffect=display_dict['minimap_color_currency']):
        """
        Template for rarer currency items.
        """
        self.base.write_rule(
            description=description, class_text=class_text, base_text=base_text,
            background_color=background_color, border_color=border_color,
            text_color=text_color, font_size=font_size,
            minimap_size=minimap_size, minimap_color=minimap_color, minimap_shape=minimap_shape,
            sound=sound, playeffect=playeffect,
        )

    def currency_recipe_quality(self, *args,
            description=None, class_text=None, base_text=None,
            quality=None,
            background_color=display_dict['standard_background'], border_color=display_dict['normal'],
            text_color=display_dict['text'], font_size=display_dict['min_font_size'],
            minimap_size=None, minimap_color=None, minimap_shape=None,
            sound=None, playeffect=None):
        """
        Template for quality currency recipe items.
        """
        self.base.write_rule(
            description=description, class_text=class_text, base_text=base_text,  quality=quality,
            background_color=background_color, border_color=border_color,
            text_color=text_color, font_size=font_size,
            minimap_size=minimap_size, minimap_color=minimap_color, minimap_shape=minimap_shape,
            sound=sound, playeffect=playeffect,
        )

    def currency_recipe_high_level(self, *args,
            description=None, class_text=None, base_text=None,
            item_level=None, rarity='Rare',
            linked_sockets=None, socket_group=None, sockets=None,
            width=None, height=None,
            background_color='{0} 100'.format(display_dict['standard_background']),
            border_color=display_dict['currency_orb_border'],
            text_color='{0} 50'.format(display_dict['text']), font_size=display_dict['min_font_size'],
            minimap_size=None, minimap_color=None, minimap_shape=None,
            sound=None, playeffect=None):
        """
        Template for high level currency recipe items.
        """
        self.base.write_rule(
            description=description, class_text=class_text, base_text=base_text,
            item_level=item_level, rarity=rarity,
            linked_sockets=linked_sockets, socket_group=socket_group, sockets=sockets,
            width=width, height=height,
            background_color=background_color, border_color=border_color,
            text_color=text_color, font_size=font_size,
            minimap_size=minimap_size, minimap_color=minimap_color, minimap_shape=minimap_shape,
            sound=sound, playeffect=playeffect,
        )

    def currency_recipe_low_level(self, *args,
            description=None, class_text=None, base_text=None,
            item_level=None, rarity='Rare',
            linked_sockets=None, socket_group=None, sockets=None,
            width=None, height=None,
            background_color='{0} 100'.format(display_dict['standard_background']), border_color=display_dict['rare'],
            text_color='{0} 50'.format(display_dict['text']),
            font_size=display_dict['min_font_size'],
            minimap_size=None, minimap_color=None, minimap_shape=None,
            sound=None, playeffect=None):
        """
        Template for low level currency recipe items.
        """
        self.base.write_rule(
            description=description, class_text=class_text, base_text=base_text,
            item_level=item_level, rarity=rarity,
            linked_sockets=linked_sockets, socket_group=socket_group, sockets=sockets,
            height=height, width=width,
            background_color=background_color, border_color=border_color,
            text_color=text_color, font_size=font_size,
            minimap_size=minimap_size, minimap_color=minimap_color, minimap_shape=minimap_shape,
            sound=sound, playeffect=playeffect,
        )

    def card_item(self, *args,
            description=None, class_text=None,base_text=None,
            background_color=display_dict['standard_background'], border_color=display_dict['card_border'],
            text_color=display_dict['card_text'], font_size=display_dict['default_font_size'],
            minimap_size=None, minimap_color=None, minimap_shape=None,
            sound='9 175', playeffect=None):
        """
        Because cards vary so much in purpose and usefulness, they get their own template.
        """
        self.base.write_rule(
            description=description, class_text=class_text, base_text=base_text,
            background_color=background_color, border_color=border_color,
            text_color=text_color, font_size=font_size,
            minimap_size=minimap_size, minimap_color=minimap_color, minimap_shape=minimap_shape,
            sound=sound, playeffect=playeffect,
        )

    def special_item(self, *args,
            description=None, class_text=None, base_text=None,
            has_mod=None,
            background_color=display_dict['standard_background'], border_color=display_dict['league_border'],
            text_color=display_dict['league_text'], font_size=display_dict['rare_font_size'],
            minimap_size=1, minimap_color=display_dict['minimap_color_special'],
            minimap_shape=display_dict['minimap_icon_special'],
            sound='4 175', playeffect=display_dict['minimap_color_special']):
        """
        Template for various special items, mostly consisting of league items.
        """
        self.base.write_rule(
            description=description, class_text=class_text, base_text=base_text,
            has_mod=has_mod,
            background_color=background_color, border_color=border_color,
            text_color=text_color, font_size=font_size,
            minimap_size=minimap_size, minimap_color=minimap_color, minimap_shape=minimap_shape,
            sound=sound, playeffect=playeffect,
        )

    def quest_item(self, *args,
            description=None, class_text=None, base_text=None,
            background_color=display_dict['standard_background'], border_color=display_dict['quest'],
            text_color=display_dict['quest'], font_size=display_dict['important_font_size'],
            minimap_size=None, minimap_color=None, minimap_shape=None,
            sound=None, playeffect=None):
        """
        Template for quest items.
        """
        self.base.write_rule(
            description=description, class_text=class_text,base_text=base_text,
            background_color=background_color, border_color=border_color,
            text_color=text_color, font_size=font_size,
            minimap_size=minimap_size, minimap_color=minimap_color, minimap_shape=minimap_shape,
            sound=sound, playeffect=playeffect,
        )

    def hidden_item(self, *args, description='Hide all other instances', class_text=None, base_text=None):
        """
        Template to hide items from showing.
        """
        self.base.write_rule(
            description=description, class_text=class_text, base_text=base_text, sound='None',
        )


class BaseTemplate():
    """
    Base-most template logic. All further template logic should build off this.
    """
    def __init__(self, filter_file, debug=False):
        self.filter_file = filter_file
        self.debug = debug

        if debug:
            logger.info('Initializing BaseTemplate class.')

    def write_rule(self, *args,
            description=None, show_item=True, class_text=None, base_text=None,
            item_level=None, rarity=None, quality=None,
            linked_sockets=None, socket_group=None, sockets=None,
            height=None, width=None,
            has_mod=None, has_influence=None, map_tier=None,
            background_color=None, border_color=None,
            text_color=None, font_size=None,
            minimap_size=None, minimap_color=None, minimap_shape=None,
            sound=None, playeffect=None):
        """
        Writes rule with provided values to filter file. Has minimal validation or formatting.
        For consistency, this rule should be used for all values written to file and
        all templates should build off this.

        Note that everything except one of either base_text or class_text is optional.
        :param description: Descriptive comment for rule.
        :param show_item: Boolean indicating if filter should show or hide matching items. Defaults to show.
        :param class_text: The "Class" text for rule. If not present, then base_text should be present.
        :param base_text: The "BaseType" text for rule. If not present, then class_text should be present.
        :param item_level: Rule selector based on level item was generated at.
        :param rarity: Rule selector based on rarity of item.
        :param quality: Rule selector based on quality of item.
        :param linked_sockets: Rule selector based on number of linked socket count of item.
        :param socket_group: Rule selector based on connected sockets of item.
        :param sockets: Rule selector based on overall socket values of item.
        :param height: Rule selector based on physical inventory height of item.
        :param width: Rule selector based on physical inventory width of item.
        :param has_mod: Rule selector based on explicit mods of item.
        :param has_influence: Rule selector based on end-game influence of item.
        :param map_tier: Rule selector based on map tier of item.
        :param background_color: Filter application to change background color of item.
        :param border_color: Filter application to change border color of item.
        :param text_color: Filter application to change text color of item.
        :param font_size: Filter application to change font size of item.
        :param minimap_size: Filter application to set minimap icon size of item.
        :param minimap_color: Filter application to set minimap color of item.
        :param minimap_shape: Filter applciation to set minimap shape of item.
        :param sound: Filter application to set drop sound of item.
        :param playeffect: Filter application to set glow aura of item.
        """
        if description is not None:
            self.filter_file.write('# {0}.\n'.format(description))
        if show_item:
            self.filter_file.write('Show\n')
        else:
            self.filter_file.write('Hide\n')

        # Limitations to filter on.
        if class_text is not None:
            self.filter_file.write('    Class {0}\n'.format(self._format_item_text(class_text)))
        if base_text is not None:
            self.filter_file.write('    BaseType {0}\n'.format(self._format_item_text(base_text)))
        if item_level is not None:
            self.filter_file.write('    ItemLevel {0}\n'.format(str(item_level).strip()))
        if rarity is not None:
            self.filter_file.write('    Rarity = {0}\n'.format(str(rarity).strip()))
        if quality is not None:
            self.filter_file.write('    Quality {0}\n'.format(str(quality).strip()))
        if linked_sockets is not None:
            self.filter_file.write('    LinkedSockets >= {0}\n'.format(str(linked_sockets).strip()))
        if socket_group is not None:
            self.filter_file.write('    SocketGroup >= {0}\n'.format(str(socket_group).strip()))
        if sockets is not None:
            self.filter_file.write('    Sockets {0}\n'.format(str(sockets).strip()))
        if height is not None:
            self.filter_file.write('    Height {0}\n'.format(str(height).strip()))
        if width is not None:
            self.filter_file.write('    Width {0}\n'.format(str(width).strip()))
        if has_mod is not None:
            self.filter_file.write('    HasExplicitMod {0}\n'.format(self._format_item_text(has_mod)))
        if has_influence is not None:
            self.filter_file.write('    HasInfluence {0}\n'.format(self._format_item_text(has_influence)))
        if map_tier is not None:
            self.filter_file.write('    MapTier {0}\n'.format(str(map_tier).strip()))

        # Values to set if filter match is found.
        if background_color is not None:
            self.filter_file.write('    SetBackgroundColor {0}\n'.format(str(background_color).strip()))
        if border_color is not None:
            self.filter_file.write('    SetBorderColor {0}\n'.format(str(border_color).strip()))
        if text_color is not None:
            self.filter_file.write('    SetTextColor {0}\n'.format(str(text_color).strip()))
        if font_size is not None:
            self.filter_file.write('    SetFontSize {0}\n'.format(str(font_size).strip()))
        if sound is not None:
            self.filter_file.write('    PlayAlertSound {0}\n'.format(str(sound).strip()))
        if minimap_size is not None or minimap_color is not None or minimap_shape is not None:
            # Check that all three are present.
            if minimap_color is None or minimap_size is None or minimap_shape is None:
                raise ValueError('Either all three minimap values must be provided, or none.')
            self.filter_file.write('    MinimapIcon {0} {1} {2}\n'.format(
                str(minimap_size).strip(),
                str(minimap_color).strip(),
                str(minimap_shape).strip(),
            ))
        if playeffect is not None:
            self.filter_file.write('    PlayEffect {0}\n'.format(str(playeffect).strip()))
        self.filter_file.write('\n')

    def _format_item_text(self, item_text):
        """
        Formats text of item by surrounding in quotes.
        If provided item text is in format of set, then recursively calls self on each value within set.
        :param item_text: Text of item to format.
        :return: Formatted text.
        """
        # Check format of item.
        if isinstance(item_text, list) or isinstance(item_text, tuple):
            # Item is array or tuple. Format each value within.
            formatted_text = ''

            # Loop through all values in set and format each.
            for item in item_text:
                if len(formatted_text) > 0:
                    formatted_text += ' '
                formatted_text += self._format_item_text(item)

            # Return formatted set.
            return formatted_text
        elif isinstance(item_text, str):
            # Strip possible outer whitespace.
            item_text = item_text.strip()

            # Check for starting quote.
            if item_text[0] != '"':
                item_text = '"' + item_text

            # Check for trailing quote.
            if item_text[:0] != '"':
                item_text = item_text + '"'

            # Return formatted item.
            return item_text
        else:
            # Item is neither set or string.
            raise TypeError('Passed item must be either set (list/tuple) or string value.')
