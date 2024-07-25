import json


class ClassAnswer:

    def __init__(self):
        self.Flag = False



    async def autoanswer(self, client, message):
        if self.Flag:

            with open('config.json', 'r', encoding='utf-8') as read:
                answer = json.load(read)['autoanswer']

            if message.text.lower() in answer.keys():
                await message.reply_text(answer[message.text.lower()])



    async def onanswer(self, client, message):
        self.Flag = True
        await message.reply_text('**🤖Автоответ на сообщения включён🤖**')



    async def offanswer(self, client, message):
        self.Flag = False
        await message.reply_text('**🤖Автоответ на сообщения выключен🤖**')



    async def addanswer(self, client, message):
        try:
            await message.delete()
            with open('config.json', 'r', encoding='utf-8') as read:
                edit = json.load(read)

            edit['autoanswer'][message.command[1].lower()] = message.command[2]

            with open('config.json', 'w', encoding='utf=8') as write:
                json.dump(edit, write, ensure_ascii=False, indent=4)

            await message.reply_text(f'**🤖Автоответ на сообщение {message.command[1]} добавлен🤖**')
        except IndexError:
            await message.reply_text('**🚫Вы ввели недостаточно значений!🚫**')



    async def deleteanswer(self, client, message):
        try:
            await message.delete()
            with open('config.json', 'r', encoding='utf-8') as read:
                edit = json.load(read)

            del edit['autoanswer'][" ".join(message.text.lower().split()[1:])]
            
            with open('config.json', 'w', encoding='utf-8') as write:
                json.dump(edit, write, ensure_ascii=False, indent=4)

            await message.reply_text(f'**🤖Автоответ на сообщение {" ".join(message.text.lower().split()[1:])} удалён🤖**')
        except IndexError:
            await message.reply_text('**🚫Вы ввели недостаточно значений!🚫**')




