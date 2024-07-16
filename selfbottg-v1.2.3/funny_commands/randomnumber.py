import random
import time

async def randomnumber(client, message):
    try:
        number = random.randint(int(message.command[1]), int(message.command[2]))
    except IndexError:
        await message.reply_text('**🚫Вы ввели только одно значение!🚫**')
    except ValueError:
        await message.reply_text('**⚠️Ошибка значений⚠️**')
    else:
        for i in range(3):
            await message.edit_text('**🎲Секунду.**')
            time.sleep(0.1)
            await message.edit_text('**🎲Секунду..**')
            time.sleep(0.1)
            await message.edit_text('**🎲Секунду...**')
            time.sleep(0.1)
        await message.delete()
        await message.reply_text(f'**🎉Вам выпало число: {number}🎉**')
