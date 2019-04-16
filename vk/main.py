import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from VkBot import VkBot
from random import random
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
            bot = VkBot(event.message_id, hw)
            
            print("NEW MESSAGE")
            print(f"By : {event.user_id}")
            print(f"Text: {message}")
            
            try:
                answers = bot.new_message(message)
            except BaseException as err:
                answers = [["Ошибка", []]]
                print(err)
            for answer in answers:
                if(answer[0] == "оповещение"):
                    vk.method('messages.send', {'user_ids': ",".join(map(lambda a: a[:-1], open("userlist.txt").readlines())), 
                                                'forward_messages': answer[1], 'random_id': random()})
                else:
                    args = {'user_id': event.user_id, 'random_id': random()}
                    if(len(answer[0])):
                        args['message'] = answer[0]
                    if(len(answer[1])):
                        for forward_message in answer[1]:
                            args['forward_messages'] = str(forward_message)
                            vk.method('messages.send', args)
                    else:
                        vk.method('messages.send', args)