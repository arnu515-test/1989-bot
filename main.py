import os
from dotenv import load_dotenv
from src import bot

load_dotenv()


if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))
