class HW:
    
    def __init__(self):
        self.synonyms = {
            "матика": "алгебра",
            "матека": "алгебра",
            "матеша": "алгебра",
            "матан": "алгебра",
            "алгебра": "алгебра",
            "математика": "алгебра",
            "геома": "геометрия",
            "стереометрия": "геометрия",
            "геометрия": "геометрия",
            "общество": "обществознание",
            "общага": "обществознание",
            "обществознание": "обществознание",
            "инфа": "информатика",
            "информатика": "информатика",
            "физан": "физика",
            "физеша": "физика",
            "физика": "физика",
            "русич": "русский",
            "русский": "русский",
            "родной": "родной",
            "англ": "английский",
            "инглиш": "английский",
            "английский": "английский",
            "обж": "обж",
            "геогр": "география",
            "география": "география",
            "история": "история",
            "хим": "химия",
            "химия": "химия",
            "био": "биология",
            "биология": "биология"}
        self.file = None
        self.name = None
        self.data = []
        print(list(self.synonyms.values()))
    
    def open(self, name):
        if(self.synonyms.get(name) != None):
            self.file = open(self.synonyms[name] + ".txt")
            self.name = self.synonyms[name]
            for line in self.file:
                self.data.append(line)
            return True
        else:
            return False
    
    def close(self):
        if(self.file != None):
            self.file.close()
            self.file = open(self.name + ".txt", 'w')
            for line in self.data:
                self.file.write(line)
            self.file.close()
            self.file = None
            self.name = None
            self.data.clear()

    def add(self, new_data):
        while(len(self.data) >= 10):
            self.data.pop()
        self.data.insert(0, new_data + '\n')
    
    def get(self, count = None):
        if(len(self.data)):
            if(count == None):
                return self.data
            elif(count == 1):
                return self.data[0]
            else:
                return self.data[:min(count, len(self.data))]
        else:
            return []