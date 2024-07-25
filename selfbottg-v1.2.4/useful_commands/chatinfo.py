from pyrogram.errors import BadRequest, NotAcceptable
import json
async def chatinfo(client, message):

    await message.delete()

    try:
        chat = await client.get_chat(message.command[1])
        with open('config.json', 'r', encoding='utf-8') as read:
            result = json.load(read)
        text = f"""
**🔢 ID: `{chat.id}`
📁 Тип чата: {chat.type}
☑️ Верифицированный: {'Да' if chat.is_verified else 'Нет'}
❌ Ограничение: {'Да' if chat.is_restricted else 'Нет'}
💰 Мошеннический: {'Да' if chat.is_scam else 'Нет'}
👨‍💻 Поддельный чат: {'Да' if chat.is_fake else 'Нет'}
🖊 Описание: {chat.description if chat.description else 'Пусто'}
👥 Количество участников: {chat.members_count}
📓 Название чата: {chat.title if chat.title else "Пусто"}
✒️ Метка чата: {chat.username if chat.username else "Пусто"}
✏️ Заметки: {result['notes'][str(chat.id)] if str(chat.id) in result['notes'].keys() else 'Заметок нет'}
🔒 Разрешение чата:
    🔐 Копирование: {'Не разрешено' if chat.has_protected_content else 'Разрешено'}
    ✉️ Отправка сообщений: {'Разрешено' if chat.permissions.can_send_messages else 'Не разрешено'}
    📹 Отправка медиа: {'Разрешено' if chat.permissions.can_send_media_messages else 'Не разрешено'}
    📝 Изменять информацию: {'Разрешено' if chat.permissions.can_change_info else 'Не разрешено'}
    ➕ Добавлeние участников: {'Разрешено' if chat.permissions.can_invite_users else 'Не разрешено'}
    📌 Закреплять: {'Разрешено' if chat.permissions.can_pin_messages else 'Не разрешено'}**
    """
        await message.reply_text(text)
    except BadRequest:
        await message.reply_text('**🤷Имя чата не найдено🤷**')
    except IndexError:
        await message.reply_text('**🚫Вы ввели недостаточно значений!🚫**')
    except NotAcceptable:
        await message.reply_text('**🚫Доступ к чату заблокирован, скорее всего он приватный🚫**')
    except AttributeError:
        await message.reply_text('**🚫Канал не является чатом!🚫**')

