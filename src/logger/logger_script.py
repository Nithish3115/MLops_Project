import logging
import os
from datetime import datetime

# Create a unique log file name with milliseconds
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S_%f')}.log"

log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

if __name__ == '__main__':
    try:
        logging.info("Starting the logging test.")
        # Simulate some processing
        logging.info("Here again I am testing.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")