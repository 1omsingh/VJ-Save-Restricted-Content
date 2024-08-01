import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26426018"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "db3addaeb6a7d9a1c8c4d5be80f68d8f")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://omsingh9star:7h318NC2FlN40Fbf@cluster0.bjxpq4k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
