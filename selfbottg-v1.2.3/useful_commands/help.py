async def help(client, message):
    text = '''
**`-mailing` (name_chat)* (string)* - сделать рассылку в указанном чате каждому участнику чата
`-spam` (count) (delay) (string)* - повтор сообщения, указывая количество и промежуток времени между сообщениями
`-userinfo` (user_name/id)* - узнать информацию о пользователе
`-chatinfo` (name_chat/id)* - узнать ифнормацию о чате
`-crash` (name_chat/id_chat)* - уничтожить чат одной командой (если нет имени чата, то используйте ID)
`-ban` (name_chat/id_chat)* (user_name)* (time format=<seconds=120 minutes=30 hours=12 days=1>) - Забанить участника чата, если участник был забанен меньше 30 секунд или больше 366 дней, то он автоматически банится навсегда
`-unban` (name_chat/id_chat)* (user_name)* - разбанить участника чата
`-give_admin` (name_chat/id_chat)* (user_name)* - выдать админа участнику чата
`-get_chat_id` (title_chat)* - получить ID чата в котороом вы присутсвтуете. Команда не ищет чаты ботов или лс
`-onanswer` - включить авто-ответ на сообщение
`-offanswer` - выключить авто-ответ на сообщение
`-addanswer` (message)* (answer)* - Добавить сообщение и ответ на него
`-deleteanswer` (message)* - удалить сообщение с ответом
`-addnote` (user_name/id|name_chat/id)* (string)* - добавить заметку в ифнормацию о чате или пользователе
`-deletenote` (user_name/id|name_chat/id)* - удалить заметку в ифнормацию о чате или пользователе

`-random_number` (integer)* (integer)* - вызвать случайное число
`-cat` - случайная картинка кота
`-dog` - случайная картинка собаки
* - знак обязательного параметра**'''

    await message.delete()
    await message.reply_text(text)