import psycopg2

class VkBot:
    def __init__(self, message_id, hw):
        self.message_id = message_id
        self.hw = hw
    
    def new_message(self, inp):
        message = []
        for i in map(lambda a: a.split(), inp.split('\n')):
            message += i
        out = []
        if(message[0].lower() == "запрос"):
            message = message[1:]
            for lesson in message:
                if(self.hw.check(lesson)):
                    data = self.hw.get(lesson, 3)
                    if(len(data)):
                        out.append(["", data])
                    else:
                        out.append([f"Задания по предмету {lesson} не найдено", []])
                else:
                    out.append([f"Урок {lesson.lower()} не найден", []])
        elif(message[0].lower() == "оповещение"):
            out.append(["оповещение", [self.message_id]])
        elif(self.hw.check(message[0].lower())):
            self.hw.add(message[0].lower(), self.message_id)
            out.append(["Успешно добавлено", []])
        else:
            out.append([f"Урок {message[0].lower()} не найден", []])
        return out
