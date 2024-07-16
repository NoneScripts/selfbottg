from pyrogram.errors import BadRequest
import json
async def userinfo(client, message):

    await message.delete()
    try:
        member = await client.get_users(message.command[1])
        with open('config.json', 'r', encoding='utf-8') as read:
            result = json.load(read)
        text = f"""
**🔢 ID: `{member.id}`
🤖 Использование личного бота: {'Да' if member.is_self else 'Нет'} 
✏️ В контактах: {'Да' if member.is_contact else 'Нет'}
🤝 Взаимные контакты: {'Да' if member.is_mutual_contact else 'Нет'}
🗑️ Удалённый аккаунт: {'Да' if member.is_deleted else 'Нет'} 
👾 Бот: {'Да' if member.is_bot else 'Нет'}
☑️ Верифицированный/ая: {'Да' if member.is_verified else 'Нет'}
❌ Ограничение в отправки сообщений: {'Да' if member.is_restricted else 'Нет'}
💰 Мошенник/ца: {'Да' if member.is_scam else 'Нет'}
👨‍💻 Поддельный аккаунт: {'Да' if member.is_fake else 'Нет'}
🔑 Поддержка: {'Да' if member.is_support else 'Нет'}
🔒 Премиум: {'Да' if member.is_premium else 'Нет'}
👨 Имя пользователя: @{member.username if member.username else 'Пусто'}
✏️ Заметки: {result['notes'][str(member.id)] if str(member.id) in result['notes'].keys() else 'Заметок нет'}
**"""
        
        await message.reply_text(text)
    except BadRequest:
        await message.reply_text('**🤷Имя пользователя не найдено🤷**')
    except IndexError:
        await message.reply_text('**🚫Вы ввели недостаточно значений!🚫**')
