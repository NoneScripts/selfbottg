from pyrogram.errors import BadRequest
from datetime import datetime, timedelta
from functions import *

async def ban(client, message):
    ban = message.text.split()
    
    time_ban = ' '.join(ban[3:])
    try:
        time = timer(time_ban)
    except ValueError:
        await message.reply_text('**🚫Неправильный формат времени🚫**')
    else:

        try:
            if time and time >= timedelta(seconds=30) and timedelta(days=366) >= time:
                await client.ban_chat_member(ban[1], ban[2], datetime.now() + time)
                await message.reply_text(f'**🔨Участник @{ban[2]} был забанен на {time}🔨**')
            else:
                await client.ban_chat_member(ban[1], ban[2])
                await message.reply_text(f'**🔨Участник @{ban[2]} был забанен навсегда🔨**')
        except BadRequest:
            await message.reply_text(f'**🚫Не удалось забанить участника @{ban[2]}, возможно у вас недостаточно прав, либо участника или чата не найдено🚫**')
        except IndexError:
            await message.reply_text('**🚫Вы ввели недостаточно значений!🚫**')