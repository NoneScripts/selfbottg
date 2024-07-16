from pyrogram.errors import BadRequest, FloodWait
import time
import json
with open('config.json', 'r', encoding='utf-8') as read:
    jsonconfig = json.load(read)

async def crash(client, message):

    index = 0

    try:
        members = [m async for m in client.get_chat_members(message.command[1])]
        await message.reply_text('**💣Начался краш чата💣**')
        try:
            me = await client.get_me()
            photo = open(jsonconfig['photo_crash'], 'rb')
            await client.set_chat_photo(message.command[1], photo=photo)
            await client.set_chat_title(message.command[1], 'Chat hacked by ' + me.first_name)
        except BadRequest:
            pass
        except FloodWait:
            pass


        for ban_members in members:
            try:
                await client.ban_chat_member(message.command[1], ban_members.user.id)
                index += 1
            except BadRequest:
                if me.id == ban_members.user.id:
                    pass
                else:
                    await message.reply_text(f'**🚫Не удалось забанить пользователя @{ban_members.user.username}, возможно у вас недостаточно прав!🚫**')
            except FloodWait as e:
                time.sleep(e.x)
        if index != 0:
            await message.reply_text('**💥Краш завершен💥**')
        else:
            await message.reply_text('**😭Не удалось крашнуть чат, возможно у вас не хватает прав администратора или модератора😭**')
                


    except BadRequest:
        await message.reply_text('**🤷Чат не найден🤷**')