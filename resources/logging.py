"""
Logging initialization.
Returns an instance of the project logger.
If first time call, then also sets up logging values for project.

Note: Standard log priority is "NOTSET" > "DEBUG" > "INFO" > "WARNING" > "ERROR" > "CRITICAL".
    See wiki for full list of non-standard values.
"""

# System Imports.
import os
import logging.config


# Variables to help run logging.
LOG_VERSION = 2.0
first_logging_call = True
log_handler_class = "logging.handlers.RotatingFileHandler"
log_handler_file_max_bytes = 1024 * 1024 * 10
log_handler_file_backup_count = 10


def get_logger(caller):
    """
    Returns an instance of the logger. Always pass the __name__ attribute.
    By calling through here, guarantees that logger will always have proper settings loaded.
    :param caller: __name__ attribute of caller.
    :return: Instance of logger, associated with caller's __name__.
    """
    # Initialize logger.
    if first_logging_call:
        _initialize_logger_settings()

    # Return logger instance, using passed name.
    return logging.getLogger(caller)


def cond_logger(logger, type, message, create_log, exc_info=False):
    """
    A conditional logger for when logging is not always called.
    Ex: There's no reason to log precautionary measures that are okay to fail silently.
    Creating a method helps prevent many small if statements from cluttering code.
    :param logger: Instance of logger to use.
    :param type: Logging type. IE, debug, info, etc.
    :param message: Message to log.
    :param create_log: Boolean dictating if this instance of log is printed.
    """
    if create_log:
        getattr(logger, type)(str(message), exc_info=exc_info)


def _initialize_logger_settings(debug=False):
    """
    Creates log directories (if not found) and initializes logging settings.
    :param debug: Boolean to indicate if test log messages should also be displayed after initialization.
    """
    # Determine logging path.
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(project_dir, "resources/logs")

    # Check if logging path exists.
    if not os.path.exists(log_dir):
        print('Creating logging folders at "{0}".'.format(log_dir))
        os.makedirs(log_dir)

    # Load dictionary of settings into logger.
    logging.config.dictConfig(_create_logging_dict(log_dir))

    # Now that logging has been initialized once, we don't need to call this function
    # again for the duration of program runtime. Set "first_logging_call" variable accordingly.
    global first_logging_call
    first_logging_call = False

    # Optionally test that logging is working as expected.
    if debug:
        logger = logging.getLogger(__name__)
        logger.info("Logging initialized.")
        logger.debug("Logging directory: {0}".format(log_dir))


def _create_logging_dict(log_directory):
    """
    Creates dictionary-styled logging options.
    :param log_directory: Directory to use for saving logs.
    :return: Dictionary of logging options.
    """
    return {
        "version": 1,
        "filters": {
            # Default level filters.
            "exclude_info_plus": {
                "()": _ExcludeInfoPlusFilter,
            },
            "exclude_warnings_plus": {
                "()": _ExcludeWarningsPlusFilter,
            },
            "exclude_error_plus": {
                "()": _ExcludeErrorPlusFilter,
            },
        },
        "formatters": {
            # Minimal logging. Only includes message.
            "minimal": {
                "format": "%(message)s",
            },
            # Simple logging. Includes message type and actual message.
            "simple": {
                "format": "[%(levelname)s] [%(filename)s %(lineno)d]: %(message)s",
            },
            # Basic logging. Includes date, message type, file originated, and actual message.
            "standard": {
                "format": "%(asctime)s [%(levelname)s] [%(filename)s %(lineno)d]: %(message)s",
            },
            # Verbose logging. Includes standard plus the process number and thread id.
            "verbose": {
                "format": "%(asctime)s [%(levelname)s] [%(filename)s %(lineno)d] || %(process)d %(thread)d || %(message)s",
            },
        },
        "handlers": {
            # Sends log message to the void. May be useful for debugging.
            "null": {
                "class": "logging.NullHandler",
            },
            # To console.
            "console": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "simple",
            },
            # Debug Level - To to file.
            "file_debug": {
                "level": "DEBUG",
                "class": log_handler_class,
                "filename": os.path.join(log_directory, "debug.log"),
                "maxBytes": log_handler_file_max_bytes,
                "backupCount": log_handler_file_backup_count,
                "formatter": "standard",
            },
            # Info Level - To file.
            "file_info": {
                "level": "INFO",
                "class": log_handler_class,
                "filename": os.path.join(log_directory, "info.log"),
                "maxBytes": log_handler_file_max_bytes,
                "backupCount": log_handler_file_backup_count,
                "formatter": "standard",
            },
            # Warn Level - To file.
            "file_warn": {
                "level": "WARNING",
                "class": log_handler_class,
                "filename": os.path.join(log_directory, "warn.log"),
                "maxBytes": log_handler_file_max_bytes,
                "backupCount": log_handler_file_backup_count,
                "formatter": "verbose",
            },
            # Error Level - To file.
            "file_error": {
                "level": "ERROR",
                "class": log_handler_class,
                "filename": os.path.join(log_directory, "error.log"),
                "maxBytes": log_handler_file_max_bytes,
                "backupCount": log_handler_file_backup_count,
                "formatter": "verbose",
            },
        },
        "loggers": {
            # All basic logging.
            "": {
                "handlers": ["console", "file_debug", "file_info", "file_warn", "file_error"],
                "level": "NOTSET",
                "propagate": False,
            },
        },
    }


def add_logging_level(levelName, levelNum, methodName=None):
    """
    Code directly imported from
    https://stackoverflow.com/questions/2183233/how-to-add-a-custom-loglevel-to-pythons-logging-facility

    Comprehensively adds a new logging level to the `logging` module and the
    currently configured logging class.
    `levelName` becomes an attribute of the `logging` module with the value
    `levelNum`. `methodName` becomes a convenience method for both `logging`
    itself and the class returned by `logging.getLoggerClass()` (usually just
    `logging.Logger`). If `methodName` is not specified, `levelName.lower()` is
    used.
    To avoid accidental clobberings of existing attributes, this method will
    raise an `AttributeError` if the level name is already an attribute of the
    `logging` module or if the method name is already present
    Example
    -------
    >> addLoggingLevel('TRACE', logging.DEBUG - 5)
    >> logging.getLogger(__name__).setLevel("TRACE")
    >> logging.getLogger(__name__).trace('that worked')
    >> logging.trace('so did this')
    >> logging.TRACE
    5
    """
    if not methodName:
        methodName = levelName.lower()

    if hasattr(logging, levelName):
        raise AttributeError("{} already defined in logging module".format(levelName))
    if hasattr(logging, methodName):
        raise AttributeError("{} already defined in logging module".format(methodName))
    if hasattr(logging.getLoggerClass(), methodName):
        raise AttributeError("{} already defined in logger class".format(methodName))

    # This method was inspired by the answers to Stack Overflow post
    # http://stackoverflow.com/q/2183233/2988730, especially
    # http://stackoverflow.com/a/13638084/2988730
    def logForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(levelNum):
            self._log(levelNum, message, args, **kwargs)

    def logToRoot(message, *args, **kwargs):
        logging.log(levelNum, message, *args, **kwargs)

    logging.addLevelName(levelNum, levelName)
    setattr(logging, levelName, levelNum)
    setattr(logging.getLoggerClass(), methodName, logForLevel)
    setattr(logging, methodName, logToRoot)


# region Logging Filters


class _ExcludeInfoPlusFilter(logging.Filter):
    """
    Class to filter out log messages of a given level.
    See https://stackoverflow.com/a/53257669 for more info.
    """

    def filter(self, record):
        """
        Filters out log messages with log level(s):
            (20) INFO
        """
        return record.levelno < 20


class _ExcludeWarningsPlusFilter(logging.Filter):
    """
    Class to filter out log messages of a given level.
    See https://stackoverflow.com/a/53257669 for more info.
    """

    def filter(self, record):
        """
        Filters out log messages with log level(s):
            (30) WARNING
        """
        return record.levelno < 30


class _ExcludeErrorPlusFilter(logging.Filter):
    """
    Class to filter out log messages of a given level.
    See https://stackoverflow.com/a/53257669 for more info.
    """

    def filter(self, record):
        """
        Filters out log messages with log level(s):
            (40) Error
        """
        return record.levelno < 40


# endregion Logging Filters
