#The repo is fully coded and modified by @Dypixx.
#Please do not sell or remove credits.
import os

API_ID = os.getenv("API_ID", "18946488")
API_HASH = os.getenv("API_HASH", "c163d4e28e63196c3806cf3b9b2885de")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "ST_Rename_Update") # Channel Username Without @
DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-1002320080278")) #Channel Id

ENABLE_FLOOD_WAIT = bool(os.getenv("ENABLE_FLOOD_WAIT", True)) # Set "True" For Enable Floodwait
FLOOD_WAIT_TIME = int(os.getenv("FLOOD_WAIT_TIME", 5)) #5min
