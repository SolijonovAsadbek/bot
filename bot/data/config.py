import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = os.getenv("ADMINS")
ip = os.getenv("ip")

DB_NAME = os.getenv("DB_NAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

if __name__ == "__main__":
    print(BOT_TOKEN)
    print(ADMINS)
    print(ip)
    print(DB_NAME)
    print(USER)
    print(PASSWORD)
    print(HOST)
    print(PORT)
