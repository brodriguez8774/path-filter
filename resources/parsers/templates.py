"""
General filter templates to make filters more consistent.
"""

# System Imports.

# User Imports.
from resources import logging as init_logging


# Initialize Logger.
logger = init_logging.get_logger(__name__)


class FilterTemplates():
    def __init__(self, filter_file, debug=False):
        self.filter_file = filter_file
        self.base = BaseTemplate(filter_file, debug)
        self.debug = debug

        if debug:
            logger.info('Initializing FilterTemplates class.')

class BaseTemplate():
    """
    Base-most template logic. All further template logic should build off this.
    """
    def __init__(self, filter_file, debug=False):
        self.filter_file = filter_file
        self.debug = debug

        if debug:
            logger.info('Initializing BaseTemplate class.')

    def write_rule(self,
                   description=None, show_item=True, base_text=None, class_text=None,
                   item_level=None, rarity=None, quality=None,
                   linked_sockets=None, sockets=None,
                   height=None, width=None,
                   has_influence=None, map_tier=None,
                   background_color=None, border_color=None,
                   text_color=None, font_size=None,
                   minimap_size=None, minimap_color=None, minimap_shape=None,
                   sound=None, playeffect=None
                   ):
        """
        Writes rule with provided values to filter file. Has minimal validation or formatting.
        For consistency, this rule should be used for all values written to file and
        all templates should build off this.

        Note that everything except one of either base_text or class_text is optional.
        :param description: Descriptive comment for rule.
        :param show_item: Boolean indicating if filter should show or hide matching items. Defaults to show.
        :param base_text: The "BaseType" text for rule. If not present, then class_text should be present.
        :param class_text: The "Class" text for rule. If not present, then base_text should be present.
        :param item_level: Rule selector based on level item was generated at.
        :param rarity: Rule selector based on rarity of item.
        :param quality: Rule selector based on quality of item.
        :param linked_sockets: Rule selector based on number of linked sockets of item.
        :param sockets: Rule selector based on overall socket values of item.
        :param height: Rule selector based on physical inventory height of item.
        :param width: Rule selector based on physical inventory width of item.
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
        # Validate provided rule syntax before continuing.
        self._validate_rule(base_text, class_text)

        # Rule appears to be valid at cursory check. Write filter.
        if description is not None:
            self.filter_file.write('# {0}.\n'.format(description))
        if show_item:
            self.filter_file.write('Show\n')
        else:
            self.filter_file.write('Hide\n')

        # Limitations to filter on.
        if base_text is not None:
            self.filter_file.write('    BaseType {0}\n'.format(self._format_item_text(base_text)))
        else:
            self.filter_file.write('    Class {0}\n'.format(self._format_item_text(class_text)))
        if item_level is not None:
            self.filter_file.write('    ItemLevel <= {0}\n'.format(str(item_level).strip()))
        if rarity is not None:
            self.filter_file.write('    Rarity = {0}\n'.format(str(rarity).strip()))
        if quality is not None:
            self.filter_file.write('    Quality <= {0}\n'.format(str(quality).strip()))
        if linked_sockets is not None:
            self.filter_file.write('    LinkedSockets <= {0}\n'.format(str(linked_sockets).strip()))
        if sockets is not None:
            self.filter_file.write('    Sockets {0}\n'.format(str(sockets).strip()))
        if height is not None:
            self.filter_file.write('    Height {0}\n'.format(str(height).strip()))
        if width is not None:
            self.filter_file.write('    Width {0}\n'.format(str(width).strip()))
        if has_influence is not None:
            self.filter_file.write('    HasInfluence {0}\n'.format(str(has_influence).strip()))
        if map_tier is not None:
            self.filter_file.write('    MapTier <= {0}\n'.format(str(map_tier).strip()))

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

    def _validate_rule(self, base_text, class_text):
        """
        Check that provided rule values are valid.
        :param base_text: Rule "base" text.
        :param class_text: Rule "class" text.
        """
        if base_text is None and class_text is None:
            raise ValueError('Rule must set either base text or class text.')
        elif base_text is not None and class_text is not None:
            raise ValueError('Rule must set only one of base text or class text.')

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
            formatted_text = []

            # Loop through all values in set and format each.
            for item in item_text:
                formatted_text.append(self._format_item_text(item))

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
                item_text = '"' + item_text

            # Return formatted item.
            return item_text
        else:
            # Item is neither set or string.
            raise TypeError('Passed item must be either set (list/tuple) or string value.')
