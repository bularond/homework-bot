import psycopg2

class HW:
    def __init__(self):
        self.synonyms = {
            "матика":         "алгебра",
            "матека":         "алгебра",
            "матеша":         "алгебра",
            "матан":          "алгебра",
            "алгебра":        "алгебра",
            "математика":     "алгебра",
            "геома":          "геометрия",
            "стереометрия":   "геометрия",
            "геометрия":      "геометрия",
            "общество":       "обществознание",
            "общага":         "обществознание",
            "обществознание": "обществознание",
            "инфа":           "информатика",
            "информатика":    "информатика",
            "физан":          "физика",
            "физеша":         "физика",
            "физика":         "физика",
            "русич":          "русский",
            "русский":        "русский",
            "родной":         "родной",
            "англ":           "английский",
            "инглиш":         "английский",
            "английский":     "английский",
            "обж":            "обж",
            "геогр":          "география",
            "география":      "география",
            "история":        "история",
            "хим":            "химия",
            "химия":          "химия",
            "био":            "биология",
            "биология":       "биология"
        }
        atributs = {
            "dbname=de029o1b0fpu7",
            "user=jowuxhiwbdxgak",
            "password=2075b275d79b4855354aadef07bba11a62faa2ec49e911bcfe2d2a568284bb95",
            "host=ec2-54-247-70-127.eu-west-1.compute.amazonaws.com",
            "port=5432"
        }
        self.conn = psycopg2.connect(' '.join(atributs))
        self.cur = self.conn.cursor()

        self.cur.execute("DELETE FROM homework WHERE date < (CURRENT_DATE - 30);")
        self.conn.commit()

    def check(self, lesson):
        if(list(self.synonyms.values()).count(lesson)):
            return True
        else:
            return False

    def add(self, lesson, messegeid):
        lesson = self.synonyms[lesson]
        self.cur.execute(f"INSERT INTO homework (date, lesson, messageid) \
            VALUES (current_date, '{lesson}', {messegeid});")
        self.conn.commit()

    def get(self, lesson, count = None):
        if count == None:
            count = 1
        self.cur.execute(f"SELECT messageid FROM homework WHERE lesson = '{lesson}' \
            ORDER by date DESC \
            LIMIT {count}")
        rows = self.cur.fetchall()
        return list(map(lambda a: a[0], rows))
