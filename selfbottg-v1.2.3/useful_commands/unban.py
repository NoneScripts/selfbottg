from pyrogram.errors import BadRequest

async def unban(client, message):


    try:
        await client.unban_chat_member(message.command[1], message.command[2])
        await message.reply_text(f'**🔨Участник @{message.command[2]} был разбанен🔨**')
    except BadRequest:
        await message.reply_text(f'**🚫Не удалось разбанить участника @{message.command[2]}, возможно у вас недостаточно прав, либо участника или чата не найдено🚫**')
    except IndexError:
        await message.reply_text('**🚫Вы ввели недостаточно значений!🚫**')