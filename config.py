import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "1923471"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fcdc178451cd234e63faefd38895c991")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "880087645"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "savecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
