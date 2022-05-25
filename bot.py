import vk_api, json
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import datetime
import re

cmds = ['kick', 'кик']

vk_session = vk_api.VkApi(token = "bd0bad70d5169d9d298b705ca5e159f1a4d34dc272287969dc8da141892d84d517d06d0ab084e5c5f68ed")
longpoll = VkBotLongPoll(vk_session, 213308439)

def sender(id, text):
    vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})


def kikuser(id, user):
    vk_session.method("messages.removeChatUser", {"chat_id": id, "user_id": user, "random_id": 0})


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            id = event.chat_id
            msg = event.object.message['text']
            cmd = msg.split(' ')[0].replace('/', '')
            iduser = event.message.get('from_id')

            if cmd in cmds and '[' in msg and ']' in msg:
                try:
                    idd = re.findall(rf'/{cmd} \[id(\d*)\|.*]', msg)[0]
                    try:
                        msg1 = msg.split(' ')[2]
                        msg4 = msg.split(' ')[3]
                        if msg4 == '1':
                            biba = 'С возможностью восстановления'
                        if msg4 == '0':
                            biba = 'Без возможности восстановления'
                        kikuser(id, idd)
                        sender(id, f"@id{idd}(Пользователь) успешно исключён из беседы.\nАдминистратор: @id{iduser}(Администратор)\n"
                                   f"Дата:  {datetime.datetime.now().strftime(' %d.%m.%Y')}\nВремя:{datetime.datetime.now().strftime(' %H:%M:%S')}\n"
                                   f"Причина: {msg1}\nТип кика: {biba}")
                        sender(15, f"@id{iduser}(Администратор) кикнкул @id{idd}(Пользователя)\nБеседа выполненной команды: {id}\nПричина: {msg1}\nТип кика:{biba}")
                    except:
                        msg3 = msg.split(' ')[2]
                        if msg3 == '1':
                            boba = 'С возможностью восстановления'
                        if msg3 == '0':
                            boba = 'Без возможности восстановления'
                        kikuser(id, idd)
                        sender(id,
                               f"@id{idd}(Пользователь) успешно исключён из беседы.\nАдминистратор: @id{iduser}(Администратор)\n"
                               f"Дата:  {datetime.datetime.now().strftime(' %d.%m.%Y')}\nВремя:{datetime.datetime.now().strftime(' %H:%M:%S')}\n"
                               f"Причина: Нет причины\nТип кика: {boba}")
                        sender(15, f"@id{iduser}(Администратор) кикнкул @id{idd}(Пользователя)\nБеседа выполненной команды: {id}\nПричина: {msg1}\nТип кика:{biba}")
                except:
                    sender(id, f'@id{iduser}(Администратор), пожалуйста, проверь правильность выполнения команды.\n/kick Пользователь Причина Тип кика\n\nДоступные типы кика: 1 - с возможностью восстановления\n0 - без возможности восстановления')
                    sender(15, f"@id{iduser}(Администратор) с конференции {id} неверно использовал функцию kick")

            if msg in ['/time']:
                sender(id, f"Текущее время и дата. \n\nНа данный момент в Москве: {datetime.datetime.now().strftime(' %H:%M:%S')}\nДата: {datetime.datetime.now().strftime(' %d.%m.%Y')}")
            if msg in ['/kick', '/кик']:
                sender(id, 'Ошибка при использовании команды!\nИспользуйте /kick Пользователь Причина Тип кика (0, 1) \n\nУчтите, что все Ваши действия логгируются!\n\nВ случае, если причина не будет указана Вас могут снять с поста!')
                sender(15, f"@id{iduser}(Администратор) с конференции {id} неверно использовал функцию kick")
            if msg == 'test':
                sender(id, f"{datetime.datetime.now().strftime('%H:%M:%S')}")
                sender(15, f"Тестовое сообщение")

            if msg in ['/help', '/хелп', '/помощь', 'help', 'хелп', 'помощь']:
                sender(id, f'🔑  Команды доступные основателю:\n\n'
                           f'/setowner - выдать права основателя в конференции\n'
                           f'/setspecadmin - выдать права специального администратора конференции\n'
                           f'/hallotext - установка приветственного сообщения\n/setting - установить различные настройки конфереции\n'
                           f'/checkpublick - проверить подписку на указанную группу\n\n'
                           f'⚙  Команды специального администратора:\n\n'
                           f'/rkick - исключить людей, которых инвайтнули менее 24 часов назад\n/setadmin - добавить администратора\n'
                           f'/addfilter - добавить слово в фильтер\n/addmentionlist - добавить запрет на упоминание человека\n\n'
                           f'⚔  Команды администратора:\n\n'
                           f'/setmoderation - добавить модератора\n/removeroles - снять привелегии\n'
                           f'/setnick - установить имя игроку\n/nicklist - просмотреть список ников\n/removenick - снять ник игрока\n'
                           f'/getnick - просмотреть ник\n/getnicksuser - получить вконтакте игрока через ник\n\n'
                           f'🔧  Команды модератора:\n\n'
                           f'/mute - выставить затычку\n/unmute - снять затычку\n/mutelist - список замученых игроков\n/warn - выдать предупреждение\n'
                           f'/unwarn - снять предупреждение\n/warnlist - список пользователей с предупреждением\n/kick - исключить пользователя\n'
                           f'/ban - заблокировать пользователя\n/unban - разблокировать пользователя\n/banlist - список заблокированных пользователей\n'
                           f'/getmute - просмотреть информацию о муте\n/getwarn - посмотреть информацию о варне\n/checkpunish - посмотреть наказания\n'
                           f'/help - список команд\n/reg - просмотреть дату регистрации аккаунта\n/cc - очистить чат\n/online - просмотреть пользователей онлайн\n'
                           f'/stats - просмотреть статистику человека ')

            if msg == '/cc':
                sender(id, f'&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\n&#4448;\nЧат был очищен @id{iduser}(Администратором) конференции.')
                sender(15, f"@id{iduser}(Администратор) использовал функцию очистки чата.\nИндивидуальный номер конференции: {id}")
            if msg.startswith('/in_all_conference'):
                sender(18, 'Сообщение от имени разработчика отправлено.')
                for i in range(15, 18):
                    sender(i, f'Оповещение от @id{iduser}(разработчика): {msg}'.replace('/in_all_conference', ''))
