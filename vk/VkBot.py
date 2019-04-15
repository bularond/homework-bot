import psycopg2

class VkBot:
    def __init__(self, message_id, hw):
        self.message_id = message_id
        self.hw = hw
    
    def new_message(self, message):
        message = sum(map(lambda a: a.split(), message.split('\n')))
        out = []
        if(message[0].lower() == "запрос"):
            message = message[1:]
            for lesson in message:
                if(self.hw.check(lesson)):
                    out.append(["", self.hw.get(lesson, 3)])
                else:
                    out.append([f"Урок {lesson.lower()} не найден", []])
        elif(self.hw.check(message[0].lower())):
            self.hw.add(message[0].lower(), self.message_id)
            out = ["Успешно добавлено", []]
        else:
            out.append([f"Урок {message[0].lower()} не найден", []])
        return out
