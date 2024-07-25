from pyrogram.errors import BadRequest

async def giveadmin(client, message):
    try:
        await client.promote_chat_member(message.command[1], message.command[2])
        await message.delete()
        await message.reply_text(f'**🔑Вы успешно выдали права администратора пользователю: @{message.command[2]}🔑**')
    except IndexError:
        await message.reply_text('**🚫Вы ввели недостаточно значений!🚫**')
    except BadRequest:
        await message.reply_text('**🚫Не удалось выдать админа. У вас не хватает прав, либо вы ввели несуществующий чат или такого пользователя в чате нет!🚫**')