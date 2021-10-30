from .bot import bot
import emoji

xi = """
⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿
⣿⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿
⣿⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻
⡿⠟⠋⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣸⣿⡷⡇⠄⣴⣾⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣿⣿⠃⣦⣄⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⢸⣿⠗⢈⡶⣷⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
"""

@bot.event
async def on_ready():
    print("Connected to discord as " + bot.user.name)


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    
    if ":rolling_on_the_floor_laughing:" in emoji.demojize(msg.content) or ":face_with_tears_of_joy:" in emoji.demojize(msg.content):
        await msg.reply("kys")
        return
    
    if "taiwan" in msg.content.lower() or "hong kong" in msg.content.lower() or "hongkong" in msg.content.lower() or "tiananmen" in msg.content.lower() or "1989" in msg.content.lower():
        await msg.reply("Dear Citizen,\nYour Internet Activity has attracted our attention. You may have posted anti-CCP thoughts, which we all know is wrong. Please refrain from doing this in the future.\n\n尊敬的市民，\n您的互联网活动引起了我们的注意。 你可能发表了反中共的想法，我们都知道这是错误的。 以后请不要这样做\n"+xi)
        return
    
    if "muslim" in msg.content.lower() or "musalmaan" in msg.content.lower() or "allah" in msg.content.lower() or "bomb" in msg.content.lower():
        await msg.reply("https://i.imgur.com/ch6uLHh.png")
        return
    
    if "give up" in msg.content.lower() or "fisherman" in msg.content.lower():
        await msg.reply("https://cdn.discordapp.com/attachments/850058695467204629/902613970790281256/japanese_man_never_give_up.mp4")
        return
    
    if "windows" in msg.content.lower():
        await msg.reply("Convert to linux. My current favorite distro: https://pop.system76.com")
        return
    
    if msg.content == "1984":
        await msg.delete()
        await msg.channel.send("get silenced lmao")
        return
    
    if "mom" in msg.content.lower() or "mother" in msg.content.lower():
        await msg.reply("你妈妈是狗")
    
    if "japan" in msg.content.lower():
        await msg.reply("suicide :flag_jp: :sunglasses:")
