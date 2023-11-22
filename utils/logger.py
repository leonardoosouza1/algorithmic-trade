# utils/logger.py

import logging
import pandas as pd

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_entry_exit_signals(entry_signals, exit_signals, position_size):
    logger.info("Entry Signals:")
    # Display DataFrame without index
    logger.info(entry_signals.to_string(index=False))

    logger.info("Exit Signals:")
    # Display DataFrame without index
    logger.info(exit_signals.to_string(index=False))

    logger.info(f"Position Size: {position_size}")
