import vk_api
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
                    reason = msg.split(' ')[2]
                    kick_type = 'С возможностью возвращения'
                    kikuser(id, idd)
                    if {idd} == {iduser}:
                        sender(id, f'@id{iduser}(Вы) использовали свой идентификатор')
                    else:
                        sender(id, f"@id{idd}(Пользователь) успешно исключён из беседы.\nАдминистратор: @id{iduser}(Администратор)\nДата:  {datetime.datetime.now().strftime(' %d.%m.%Y')}\nВремя:{datetime.datetime.now().strftime(' %H:%M:%S')}\nПричина: {reason}\nТип кика: {kick_type}")
                        print(iduser, 'use command kick', idd)
                except:
                    sender(id, f'@id{iduser}(Администратор), за это тебя могут снять!\n\nВозможные причины появления данного сообщения:\n1. Вы попытались кикнуть человека старше Вас рангом.\n2. Вы не указали причину для кика\n3. Вы гей')
                    print('Администратор с id',iduser, ' Попытка кикнуть одного из членов whitelist')

            if msg in ['/kick', '/кик']:
                sender(id, 'Ошибка при использовании команды!\nИспользуйте /kick пользователь причина \n\nУчтите, что все Ваши действия логгируются!\n\nВ случае, если причина не будет указана Вас могут снять с поста!')
