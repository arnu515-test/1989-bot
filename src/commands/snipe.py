from discord import Message, Embed
import json
import os


async def handler(msg: Message, *args: str):
    dmesgs = {}
        
    if not os.path.exists("dmesg.json"):
        with open("dmesg.json", "w") as f:
            json.dump(dict(), f)

    with open("dmesg.json", "r") as f:
        dmesgs = json.load(f)
        if type(dmesgs) != dict:
            dmesgs = {}
    
    deleted = dmesgs.get(str(msg.channel.id))
    if not deleted:
        await msg.channel.send("No deleted messages found.")
        return
    embed = Embed(title="Deleted message")
    embed.add_field(name="From", value=deleted.get("from", "Anon"), inline=False)
    embed.add_field(name="Message", value=deleted.get("content", "No content"), inline=False)
    embed.set_footer(text=f"{deleted.get('name', 'Anon')}, don't be jewish again!")
    await msg.channel.send(embed=embed)
    return


command = {
    "description": "Get the last deleted message (if stored)",
    "usage": "",
    "handler": handler
}
