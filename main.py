from src import bot
import os

if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))