from .bot import bot
import emoji

@bot.event
async def on_ready():
    print("Connected to discord")


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    
    if ":rolling_on_the_floor_laughing:" in emoji.demojize(msg.content) or ":face_with_tears_of_joy:" in emoji.demojize(msg.content):
        await msg.reply("kys")
