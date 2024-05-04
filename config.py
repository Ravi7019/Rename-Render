# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "13992749")

API_HASH = os.environ.get("API_HASH", "c8b1a7c3ce9aa1d1eec2fee774d48399")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6812650524:AAFzrAiV-uKPGM4XsQbqi14feTcA9hi_csM") 

FORCE_SUB = os.environ.get("FORCE_SUB", "KannadaMagaa") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "tamilrockers570")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://KF:KF@cluster0.m20cd4r.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/a1bdf9396749c6ba601ca.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
