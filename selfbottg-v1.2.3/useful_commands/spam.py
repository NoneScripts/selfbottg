import time
from pyrogram.errors import FloodWait, BadRequest
from functions import isfloat

global Flag
Flag = True

async def spam(client, message):
    spam = message.text.split()
    FLAG = False
    flag = False
    await message.delete()


    
    try:
        if isfloat(spam[2]):
            await client.send_message('me', '**✅Чтобы остановить спам, напишите `-stopspam`✅**')
            FLAG = True
            for i in range(int(spam[1])):
                try:
                    await message.reply_text(" ".join(spam[3:]))
                    time.sleep(float(spam[2]))
                    flag = True
                    if Flag == False:
                        break
                except BadRequest:
                    break
    except FloodWait as e:
        time.sleep(e.x)
    except ValueError:
        await message.reply_text('**⚠️Ошибка значений⚠️**')
    except IndexError:
        pass
    else:
        if FLAG == False:
            await client.send_message('me', '**✅Чтобы остановить спам, напишите `-stopspam`✅**')
    finally:
        try:
            if spam[1].isdigit() and flag != True:
                for i in range(int(spam[1])):
                    try:
                        if spam[2:] != []:
                            await message.reply_text(" ".join(spam[2:]))
                            if Flag == False:
                                break
                        else:
                            # FLAG = True
                            await message.reply_text('**⁉️Вы забыли ввести текст⁉️**')
                            break
                    except BadRequest:
                        break
        
            elif flag != True:
                await client.send_message('me', '**✅Чтобы остановить спам, напишите `-stopspam`✅**')
                while Flag:
                    try:
                        await message.reply_text(" ".join(spam[1:]))
                    except BadRequest:
                        break
        except IndexError:
            await message.reply_text('**⁉️Вы забыли ввести текст⁉️**')
    

async def startspam(client, message):
    global Flag
    Flag = True
    await spam(client, message)

async def stopspam(client, message):
    global Flag
    Flag = False
    await message.delete()

