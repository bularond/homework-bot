import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from VkBot import VkBot
from random import randint
from HW import HW

token = "2fcf9b3ccecbc851d3353cc0ba1b7ae31fb3e59cc3bf62416a3f6ecd2483228f35f05f5451037950d53b2"

vk = vk_api.VkApi(token=token)
hw = HW()

longpoll = VkLongPoll(vk)
print("Server started")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text
            bot = VkBot(event.message_id, event.user_id, hw)
            
            print("NEW MESSAGE")
            print(f"By : {event.user_id}")
            print(f"Text: {message}")
            
            try:
                answers = bot.new_message(message)
            except BaseException as err:
                answers = [{'messege': 'Ошибка',
                        'user_id': event.user_id,
                        'random_id': randint(0, 2 ** 32 - 1)}]
                print(err)
            for answer in answers:
                vk.method('messages.send', answer)
                print('Answer', answer)
