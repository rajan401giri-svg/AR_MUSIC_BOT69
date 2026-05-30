import os

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

LOGGER_ID = int(os.getenv("LOGGER_ID", 0))
MONGO_URL = os.getenv("MONGO_URL")

STRING_SESSION = os.getenv("STRING_SESSION")
OWNER_ID = int(os.getenv("OWNER_ID", 0))
