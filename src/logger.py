import logging
import os
from datetime import datetime

# Log file ka unique naam (date & time ke saath)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# logs folder ka path
logs_path = os.path.join(os.getcwd(), "logs")

# Agar folder exist nahi karta toh bana do
os.makedirs(logs_path, exist_ok=True)

# Complete log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# ---------------- MAIN BLOCK ----------------
if __name__ == "__main__":
    logging.info("Logging has started")
