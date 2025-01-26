#The repo is fully coded and modified by @Dypixx.
#Please do not sell or remove credits.
import os

API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "ST_Rename_Update") # Channel Username Without @
DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-100")) #Channel Id

ENABLE_FLOOD_WAIT = bool(os.getenv("ENABLE_FLOOD_WAIT", True)) # Set "True" For Enable Floodwait
FLOOD_WAIT_TIME = int(os.getenv("FLOOD_WAIT_TIME", 300)) #5min
