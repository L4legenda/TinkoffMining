import os
from dotenv import load_dotenv
load_dotenv()


TOKEN = os.getenv("TOKEN")
TELEGRAM_TOKEN = os.getenv("TOKEN_TELEGRAM")
ID_ACCOUNT_TELEGRAM = os.getenv("ID_ACCOUNT_TELEGRAM")

CURRENT_TICKER = os.getenv("CURRENT_TICKER")