import bs4
import requests
from HW import HW
from datetime import datetime as dt
from pytz import timezone

class VkBot:
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.username = self.get_user_name_from_vk_id(user_id)
        self.hw = HW()
    
    def new_message(self, message):
        def pretty_date():
            mounth = {
                1:'января',
                2:'февраля',
                3:'марта',
                4:'апреля',
                5:'мая',
                6:'июня',
                7:'июля',
                8:'августа',
                9:'сентября',
                10:'октября',
                11:'ноября',
                12:'декбря'}
            
            date = dt.now(tz=timezone('Asia/Yekaterinburg')).timetuple()
            return f'{date[2]} {mounth[date[1]]} в {date[3]}:{date[4]}'
        
        message = tuple(map(lambda a: a.split(), message.split('\n')))
        out = ''
        if(message[0][0].lower() == "добавить"):
            for line in message[1:]:
                if(self.hw.open(line[0].lower())):
                    new_data = f'{self.hw.name} добавлено {self.username} {pretty_date()} - {" ".join(line[1:])}'
                    self.hw.add(new_data)
                    out += new_data + '\n'
                else:
                    out += f'Не найден предмет {line.split()[0].lower()}\n'
                self.hw.close()
        elif(message[0][0].lower() == "запрос"):
            lst = []
            for i in message:
                lst += i
            for request in lst[1:]:
                if(self.hw.open(request.lower())):
                    if(len(self.hw.get())):
                        if(len(lst) == 2):
                            out += '\n'.join(self.hw.get())
                        else:
                            out += self.hw.get(1)
                    else:
                        out += f'Отсутствует домашнее задание по предмету {self.hw.name}\n'
                else:
                    out += f'Не найден предмет {request}\n'
                self.hw.close()
        return out
        
    def get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        
        user_name = self.clean_all_tag_from_str(bs.findAll("title")[0])
        
        return user_name.split()[0]
    
    @staticmethod
    def clean_all_tag_from_str(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True
        
        return result
        