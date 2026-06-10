# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Rkn_Bots(object):
    
    # Rkn client config  ( required.. 😥)
    API_ID = os.environ.get("API_ID", "26513107")
    API_HASH = os.environ.get("API_HASH", "f14ce4b58dc8812cfc9665588472f2d4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7849099046:")

    # start_pic
    RKN_PIC = os.environ.get("RKN_PIC", "https://envs.sh/50h.jpg")

    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "80"))

    # force subs channel ( required.. 😥)
    FORCE_SUB = os.environ.get("FORCE_SUB", "-1002204726881") 
    
    # database config ( required.. 😥)
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")     
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://Dawnload94:Dawnload94@cluster0.ursfl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    # default caption 
    DEF_CAP = os.environ.get("DEF_CAP", "<b><a href='telegram.me/MovieDawnloadHub'>{file_name}</a>\n\n#1ˢᵗ ᵒⁿ 🅃🄴🄻🄴🄶🅁🄰🄼 ᵐᵒᵛⁱᵉˢ ʷᵉᵇ ˢᵉʳⁱᵉˢ ᵃⁿᵈ ᵗᵛ ˢʰᵒʷˢ\n</b><blockquote>𝖩𝗈𝗂𝗇➥「<a href='telegram.me/MovieDawnloadHub'>Backup channel</a>」</blockquote>",)

    # sticker Id
    STICKER_ID = os.environ.get("STICKER_ID", "0")

    # admin id  ( required.. 😥)
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1928404158').split()]
    

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
