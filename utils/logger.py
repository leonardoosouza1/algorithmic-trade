# logger.py

import logging

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_entry_exit_points(entry_point, exit_point, position_size):
    logger.info(f"Entry point: {entry_point}")
    logger.info(f"Exit point: {exit_point}")
    logger.info(f"Position size: {position_size}")
