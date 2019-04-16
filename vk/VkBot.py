import psycopg2
from random import randint

class VkBot:
    def __init__(self, message_id, user_id, hw):
        self.message_id = message_id
        self.user_id = user_id
        self.hw = hw

        self.admin_list = [246776577, 160229003, 152292384, 245270656]
    
    def new_message(self, inp):
        message = []
        for i in map(lambda a: a.split(), inp.split('\n')):
            message += i
        out = []
        if(message[0].lower() == "запрос"):
            message = message[1:]
            for lesson in message:
                if(self.hw.check(lesson)):
                    forward_messages = list(map(str, self.hw.get(lesson, 3)))
                    for forward_message in forward_messages:
                        out.append({'forward_messages': forward_message, 
                                    'user_id': self.user_id,
                                    'random_id': self.get_random_id()})
                    if(not len(forward_messages)):
                        out.append({'message': f'Задания по предмету {lesson} не найдено',
                                    'user_id': self.user_id,
                                    'random_id': self.get_random_id()})
                else:
                    out.append({'message': f'Урок {lesson.lower()} не найден',
                                'user_id': self.user_id,
                                'random_id': self.get_random_id()})
        elif(message[0].lower() == "оповещение"):
            if(self.admin_list.count(self.user_id)):
                out.append({'forward_messages': self.message_id,
                            'user_ids': ','.join(map(lambda a: a[:-1], open("userlist.txt").readlines())),
                            'random_id': self.get_random_id()})
            else:
                out.append({'message': 'Отказано в доступе',
                            'user_id': self.user_id,
                            'random_id': self.get_random_id()})
        elif(self.hw.check(message[0].lower())):
            self.hw.add(message[0].lower(), self.message_id)
            out.append({'message': 'Успешно добавлено',
                        'user_id': self.user_id,
                        'random_id': self.get_random_id()})
        else:
            out.append({'message': f'Предмет {message[0].lower()} не найден',
                        'user_id': self.user_id,
                        'random_id': self.get_random_id()})
        return out
    
    @staticmethod
    def get_random_id():
        return(randint(0, 2**32 - 1))