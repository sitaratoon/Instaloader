#The repo is fully coded and modified by @Dypixx.
#Please do not sell or remove credits.

import os

API_ID = os.getenv("API_ID", "18946488")
API_HASH = os.getenv("API_HASH", "c163d4e28e63196c3806cf3b9b2885de")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN = int(os.getenv("ADMIN", "6692613520"))

DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-1002451946366")) #Channel Id
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002320080278"))

DB_URI = os.getenv("DB_URI", "mongodb+srv://Renamest:Renamest@cluster0.prfhc.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.getenv("DB_NAME", "Ajay")

IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Force Subscribe Enable
AUTH_CHANNELS = os.environ.get("AUTH_CHANNEL", "-1002355394644") # Add Multiple Channels iD By Space
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")] # DONT TOUCH

ENABLE_FLOOD_WAIT = bool(os.getenv("ENABLE_FLOOD_WAIT", True)) # Set "True" For Enable Floodwait
FLOOD_WAIT_TIME = int(os.getenv("FLOOD_WAIT_TIME", 15)) #5min
