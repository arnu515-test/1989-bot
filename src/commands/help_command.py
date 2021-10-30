from . import commands


def help_command(prefix: str):
    to_return = "Available commands:\n"

    for name in commands.keys():
        command = commands[name]
        to_return += f"**{prefix}{name}** - {command.get('description') or name}\n"
        if command.get("usage"):
            to_return += f"Usage: {prefix}{name} {command.get('usage')}\n\n"
        else:
            to_return += f"Usage: {prefix}{name}\n\n"

    return to_return
