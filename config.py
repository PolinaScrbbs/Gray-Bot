from dotenv import load_dotenv
import os

os.environ.pop("BOT_TOKEN", None)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
