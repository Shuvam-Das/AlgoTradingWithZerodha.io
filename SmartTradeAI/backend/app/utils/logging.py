haaaaimport sys
from loguru import logger
from app.core.config import settings

# Remove default logger
logger.remove()

# Add custom logging format
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)

# Add file logging
logger.add(
    "logs/smarttradeai.log",
    rotation="1 day",
    retention="1 week",
    compression="zip",
    level="DEBUG"
)