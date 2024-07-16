async def get_chat_id(client, message):
    dialogs = client.get_dialogs()
    flag = False
    await message.delete()
    try:
        async for dialog in dialogs:
            if dialog.chat.title == " ".join(message.text.split()[1:]):
                await message.reply_text(f"ID чата: `{dialog.chat.id}`, Название чата: {dialog.chat.title if dialog.chat.title else "Пусто"}/@{dialog.chat.username if dialog.chat.username else 'Пусто'}")
                flag = True
                break
        if not flag:
            await message.reply_text("**🤷Текст чата не найдено🤷**")
    except IndexError:
        await message.reply_text('**🚫Вы ввели недостаточно значений!🚫**')