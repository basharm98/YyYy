# Bot Config File 
# Requier Bot Modules 
from pyrogram import Client , enums
import os 
# Requier Database Modules Class 
from Utils.database import Database


# Bot Config
class config:
    API_KEY : str = "7404344462:AAEfCAGjRw9UHl0tEtPgRfmRocKPHMKWvq4" # The API key or Bot Token
    API_HASH: str = "160b2bf653ee7dd974bd6d09a7968cd1" # UsrBot Api Hash
    API_ID  : int = 25829176 # User Bot Api Id
    SUDO    : int = 7246248054 # Sudo Id
 


# Check Bot DIrctory
if not os.path.exists('./.session'): # Sesisons FIle 
    os.mkdir('./.session')


if not os.path.exists('./database'): #  Databesas FIle 
    os.mkdir('./database')


# Get Database 
database = Database()

# Temp status 
temp = {'broadcast':False}

# Start Pyrogram Client
app = Client(
    name="./.session/rad", 
    bot_token=config.API_KEY, 
    api_hash=config.API_HASH,
    api_id=config.API_ID, 
    plugins=dict(root="Plugins"), 
    parse_mode=enums.ParseMode.DEFAULT
)

