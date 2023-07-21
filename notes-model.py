import datetime

class Note:
    def __init__(self, body):
        self.creation_date = datetime.datetime.now()
        self.modification_date = self.creation_date
        self.body = body[:2000] #Предельный размер заметки
    
    def modify(self, new_body):
        self.body = new_body[:2000]
        self.modification_date = datetime.datetime.now()
    
    def __str__(self):
        return f"Created: {self.creation_date}, Modified: {self.modification_date}, Body: {self.body}"
    