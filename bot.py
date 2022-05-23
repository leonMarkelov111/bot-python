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
                    kick_type = 'С возможностью возвращения'
                    try:
                        msg1 = msg.split(' ')[2]
                        kikuser(id, idd)
                        sender(id,
                               f"@id{idd}(Пользователь) успешно исключён из беседы.\nАдминистратор: @id{iduser}(Администратор)\n"
                               f"Дата:  {datetime.datetime.now().strftime(' %d.%m.%Y')}\nВремя:{datetime.datetime.now().strftime(' %H:%M:%S')}\n"
                               f"Причина: {msg1}\nТип кика: {kick_type}")
                        print(iduser, 'use command kick', idd)
                    except:
                        kikuser(id, idd)
                        sender(id,
                               f"@id{idd}(Пользователь) успешно исключён из беседы.\nАдминистратор: @id{iduser}(Администратор)\n"
                               f"Дата:  {datetime.datetime.now().strftime(' %d.%m.%Y')}\nВремя:{datetime.datetime.now().strftime(' %H:%M:%S')}\n"
                               f"Причина: Нет причины\nТип кика: {kick_type}")
                        print(iduser, 'use command kick', idd)
                except Exception as e:
                    sender(id,
                   f'@id{iduser}(Администратор), за это тебя могут снять!\n\nВозможные причины появления данного сообщения:'
                   f'\n1. Вы попытались кикнуть человека старше Вас рангом.\n'
                   f'2. Вы не указали причину для кика\n'
                   f'3. Вы гей')
            print('Администратор с id', iduser, ' Попытка кикнуть одного из членов whitelist')
            if msg in ['/time']:
                sender(id, f"Текущее время и дата. \n\nНа данный момент в Москве: {datetime.datetime.now().strftime(' %H:%M:%S')}\nДата: {datetime.datetime.now().strftime(' %d.%m.%Y')}")
            if msg in ['/kick', '/кик']:
                sender(id, 'Ошибка при использовании команды!\nИспользуйте /kick пользователь причина \n\nУчтите, что все Ваши действия логгируются!\n\nВ случае, если причина не будет указана Вас могут снять с поста!')
            if msg == 'test':
                sender(id, f"{datetime.datetime.now().strftime('%H:%M:%S')}")
            if msg in ['/help', '/хелп', '/помощь', 'help', 'хелп', 'помощь']:
                sender(id, f'Команды доступные основателю:\n\n/setowner - выдать права основателя в конференции\n/setspecadmin - выдать права специального администратора конференции\n/hallotext - установка приветственного сообщения\n/setting - установить различные настройки конфереции\n/checkpublick - проверить подписку на указанную группу\n\nКоманды специального администратора:\n\n/rkick - исключить людей, которых инвайтнули менее 24 часов назад\n/setadmin - добавить администратора\n/addfilter - добавить слово в фильтер\n/addmentionlist - добавить запрет на упоминание человека\n\nКоманды администратора:\n\n/setmoderation - добавить модератора\n/removeroles - снять привелегии\n/setnick - установить имя игроку\n/nicklist - просмотреть список ников\n/removenick - снять ник игрока\n/getnick - просмотреть ник\n/getnicksuser - получить вконтакте игрока через ник\n\nКоманды модератора:\n\n/mute - выставить затычку\n/unmute - снять затычку\n/mutelist - список замученых игроков\n/warn - выдать предупреждение\n/unwarn - снять предупреждение\n/warnlist - список пользователей с предупреждением\n/kick - исключить пользователя\n/ban - заблокировать пользователя\n/unban - разблокировать пользователя\n/banlist - список заблокированных пользователей\n/getmute - просмотреть информацию о муте\n/getwarn - посмотреть информацию о варне\n/checkpunish - посмотреть наказания\n/help - список команд\n/reg - просмотреть дату регистрации аккаунта\n/cc - очистить чат\n/online - просмотреть пользователей онлайн\n/stats - просмотреть статистику человека ')
