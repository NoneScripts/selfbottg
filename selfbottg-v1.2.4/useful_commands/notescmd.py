from pyrogram.errors import BadRequest, NotAcceptable
import json

async def writenote(client, message):
    await message.delete()
    try:
        chat = await client.get_chat(message.command[1])
    except BadRequest:
        try:
            chat = await client.get_users(message.command[1])
        except BadRequest:
            await message.reply_text('**🤷Имя чата или пользователя не найдено🤷**')
            return
        except NotAcceptable:
            await message.reply_text('**🚫Доступ к чату или пользователю заблокирован, скорее всего он приватный🚫**')
            return

    try:
        with open('config.json', 'r', encoding='utf-8') as read:
            edit = json.load(read)
        edit['notes'][chat.id] = ' '.join(message.text.split()[2:])
        with open('config.json', 'w', encoding='utf-8') as write:
            json.dump(edit, write, ensure_ascii=False, indent=4)
        await message.reply_text('**✏️Вы успешно добавили заметку✏️**')
    except IndexError:
        await message.reply_text('**🚫Вы ввели недостаточно значений!🚫**')

    
async def deletenote(client, message):
    await message.delete()
    try:
        chat = await client.get_chat(message.command[1])
    except BadRequest:
        try:
            chat = await client.get_users(message.command[1])
        except BadRequest:
            await message.reply_text('**🤷Имя чата или пользователя не найдено🤷**')
            return
        except NotAcceptable:
            await message.reply_text('**🚫Доступ к чату или пользователю заблокирован, скорее всего он приватный🚫**')
            return

    try:
        with open('config.json', 'r', encoding='utf-8') as read:
             edit = json.load(read)
        del edit['notes'][str(chat.id)]
        with open('config.json', 'w', encoding='utf=8') as write:
             json.dump(edit, write, ensure_ascii=False, indent=4)
        await message.reply_text('**✏️Вы успешно удалили заметку✏️**')
    except IndexError:
        await message.reply_text('**🚫Вы ввели недостаточно значений!🚫**')