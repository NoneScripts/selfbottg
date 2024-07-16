import json

async def set_prefix(client, message):
    with open('config.json', 'r') as read:
        config = json.load(read)
    config['prefix'] = message.command[1]
    with open('config.json', 'w') as write:
        json.dump(config, write, indent=4)
    await message.delete()
    await message.reply_text('**✒️Вы успешно сменили префикс✒️**')