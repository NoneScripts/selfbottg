import time
from pyrogram.errors import BadRequest, FloodWait

async def mailing(client, message):
    mailing = message.text.split()
    try:
        members = [m async for m in client.get_chat_members(str(mailing[1]))]
        await message.delete()
        await message.reply_text('**✉️Рассылка началась✉️**')
    except BadRequest:
        await message.reply_text('**🤷Чат не найден🤷**')
    for m in members:
        try:
            await client.send_message(m.user.id, ' '.join(mailing[2:]))
        except FloodWait as e:
            time.sleep(e.x)
        except BadRequest:
            continue
    await message.reply_text('**✉️Рассылка завершена✉️**')