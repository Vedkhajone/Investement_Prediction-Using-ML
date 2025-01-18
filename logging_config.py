# logging_config.py
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set to DEBUG for more detailed logs
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app_log.log"),  # Write logs to app_log.log file
        logging.StreamHandler()  # Logs to console (terminal)
    ]
)

# Get the logger instance
logger = logging.getLogger(__name__)
