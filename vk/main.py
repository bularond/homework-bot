import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from VkBot import VkBot
from random import random

token = "66857d38795be673003e9e2951d66b7b5a0f458c7451ea58fef1eb8430f74d84ca08d0c13e5e433663c67"

lessons = ('алгебра', 'алгебра', 'алгебра', 'алгебра', 'алгебра', 'алгебра', 'геометрия', 'геометрия', 'геометрия', 'обществознание', 'обществознание', 'обществознание', 'информатика', 'информатика', 'физика', 'физика', 'физика', 'русский', 'русский', 'родной', 'английский', 'английский', 'английский', 'обж', 'география', 'география', 'история', 'химия', 'химия', 'биология', 'биология')
for i in lessons:
    open(i + ".txt", 'a').close()

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)
print("Server started")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text
            bot = VkBot(event.user_id)
            
            print("NEW MESSAGE")
            print(f"By {bot.username}")
            print(f"Text: {message}")
            
            try:
                answer = bot.new_message(message)
            except BaseException:
                answer = "Ошибка"
            if(len(answer)):
                vk.method('messages.send', {'user_id': event.user_id, 'message': answer, 'random_id': random()})
                print(f'Anwer: {answer}')