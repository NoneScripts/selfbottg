import os
try:
    from pyrogram import Client, filters
except:
    os.system('pip install pyrogram==2.0.106')
    os.system('pip install tgcrypto==1.2.5')
    from pyrogram import Client, filters
try:
    from colorama import init, Fore
except:
    os.system('pip install colorama')
    from colorama import init, Fore
from beautifulTEXT import text
from useful_commands import *
from funny_commands import *
import json
import time

init()


Flag = False

if os.path.exists('account.session'):
    answer = input(Fore.GREEN + 'Зарегестрировать новый аккаунт? Напишите ' + Fore.CYAN + '"ok"' + Fore.GREEN + ' если да, нажмите enter или напишите всё что угодно кроме "ok" если нет\n\nRegister a new account? Write' + Fore.CYAN + '" ok "' + Fore.GREEN + 'if yes, press enter or write anything except "ok" if no\n')
    if answer == "ok":
        Flag = True
        os.remove('account.session')
else:
    Flag = True

if Flag:
    with open('config.json', 'r', encoding='utf-8') as read:
        jsonconfig = json.load(read)
    jsonconfig['id'] = input(Fore.RED + 'Введите' + Fore.YELLOW + ' api id' + Fore.LIGHTCYAN_EX + '\napi id и api hash можно взять на сайте' + Fore.RESET + ' https://my.telegram.org/auth\n\n' + Fore.RED + 'Enter' + Fore.YELLOW + ' api id' + Fore.LIGHTCYAN_EX + '\napi id and api hash can be found on the website' + Fore.RESET + ' https://my.telegram.org/auth\n')
    jsonconfig['hash'] = input(Fore.RED + 'Введите' + Fore.YELLOW + ' api hash' + Fore.RED + '\n\nEnter' + Fore.YELLOW + ' api hash\n')
    with open('config.json', 'w') as write:
        json.dump(jsonconfig, write, indent=4)

with open('config.json', 'r', encoding='utf-8') as read:
        jsonconfig = json.load(read)
prefix = jsonconfig['prefix']



app = Client('account', jsonconfig['id'], jsonconfig['hash'])

objectanswer = ClassAnswer()

@app.on_message(filters.command('spam', prefixes=prefix) & filters.me)
async def flood(client, message):
    await startspam(client, message)
@app.on_message(filters.command('stopspam', prefixes=prefix) & filters.me)
async def stop(client, message):
    await stopspam(client, message)

@app.on_message(filters.command(['mailing', 'mail'], prefixes=prefix) & filters.me)
async def mail(client, message):
    await mailing(client, message)

@app.on_message(filters.command(['userinfo', 'user_info', 'user'], prefixes=prefix) & filters.me)
async def user(client, message):
    await userinfo(client, message)
    
@app.on_message(filters.command(['chatinfo', 'chat_info'], prefixes=prefix) & filters.me)
async def chat(client, message):
    await chatinfo(client, message)

@app.on_message(filters.command('help', prefixes=prefix) & filters.me)
async def helper(client, message):
    await help(client, message)

@app.on_message(filters.command('crash', prefixes=prefix) & filters.me)
async def crashchat(client, message):
    await crash(client, message)

@app.on_message(filters.command('ban', prefixes=prefix) & filters.me)
async def ban_member(client, message):
    await ban(client, message)
@app.on_message(filters.command('unban', prefixes=prefix) & filters.me)
async def unban_member(client, message):
    await unban(client, message)

@app.on_message(filters.command(['get_chat_id', 'get_chat', 'get_dialog', 'chat_id', 'chatid', 'getchat', 'getdialog', 'getchatid', 'chatidget'], prefixes=prefix) & filters.me)
async def get(client, message):
    await get_chat_id(client, message)

@app.on_message(filters.command(["random_number", "randomnumber", "rn"], prefixes=prefix) & filters.me)
async def rn(client, message):
    await randomnumber(client, message)

@app.on_message(filters.command('cat', prefixes=prefix) & filters.me)
async def kitty(client, message):
    await cat(client, message)

@app.on_message(filters.command('dog', prefixes=prefix) & filters.me)
async def mydog(client, message):
    await dog(client, message)

@app.on_message(filters.command(['give_admin', 'giveadmin', 'giveadministator', 'give_administator'], prefixes=prefix) & filters.me)
async def give(client, message):
    await giveadmin(client, message)

@app.on_message(~filters.me)
async def answ(client, message):
    await objectanswer.autoanswer(client, message)
@app.on_message(filters.command(['onanswer', 'on_answer'], prefixes=prefix) & filters.me)
async def on(client, message):
    await objectanswer.onanswer(client, message)
@app.on_message(filters.command(['offanswer', 'off_answer'], prefixes=prefix) & filters.me)
async def off(client, message):
    await objectanswer.offanswer(client, message)
@app.on_message(filters.command(['addanswer', 'add_answer'], prefixes=prefix) & filters.me)
async def add(client, message):
    await objectanswer.addanswer(client, message)
@app.on_message(filters.command(['deleteanswer', 'delete_answer', 'remove_answer', 'removeanswer', 'del_answer', 'delanswer'], prefixes=prefix) & filters.me)
async def delete(client, message):
    await objectanswer.deleteanswer(client, message)

@app.on_message(filters.command(['addnote', 'add_note', 'writenote', 'write_note'], prefixes=prefix) & filters.me)
async def delete(client, message):
    await writenote(client, message)
@app.on_message(filters.command(['deletenote', 'delete_note', 'remove_note', 'removenote', 'del_note', 'delnote'], prefixes=prefix) & filters.me)
async def delete(client, message):
    await deletenote(client, message)



#В РАЗРАБОТКЕ!
# @app.on_message(filters.command(['setprefix', 'set_prefix', 'prefix'], prefixes=prefix) & filters.me)
# async def myprefix(client, message):
#     await set_prefix(client, message)


if __name__ == '__main__':
    print('The selfbot is running')
    text()
    try:
        app.run()
    except OverflowError:
        print('Не найден api hash и api id, создайте новый аккаунт и попробуйте ещё раз ввести\nThe api hash and api id were not found, create a new account and try to enter it again')
        time.sleep(5)

