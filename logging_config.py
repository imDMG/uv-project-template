import logging
import sys
from typing import TYPE_CHECKING

from loguru import logger


if TYPE_CHECKING:
    from loguru import HandlerConfig, Logger


class InterceptHandler(logging.Handler):
    def emit(self, record: "logging.LogRecord"):
        # Get the corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while (
            frame is not None and frame.f_code.co_filename == logging.__file__
        ):
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_logging() -> "Logger":
    # intercept everything at the root logger
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(0)

    # remove every other logger's handlers
    # and propagate to root logger
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    handlers: "list[HandlerConfig]" = [
        # Console — INFO and above
        {
            "sink": sys.stdout,
            "level": "INFO",
            "format": (
                "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>"
                " | <level>{level: <8}</level> | <level>{message}</level>"
            ),
        },
    ]
    logger.configure(handlers=handlers)

    return logger
