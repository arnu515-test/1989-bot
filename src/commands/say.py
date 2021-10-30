from discord import Message


async def handler(msg: Message, *args: str):
    await msg.delete()
    await msg.channel.send(" ".join(args))


command = {
    "description": "Make the bot say something",
    "usage": "<message>",
    "handler": handler
}
