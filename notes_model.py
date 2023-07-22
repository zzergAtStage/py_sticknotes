import json
import datetime

class Note:
    """Describes the Note properties and default note behavior"""
    def __init__(self, body):
        """Default constructor of the class instances"""
        self.creation_date = datetime.datetime.now()
        self.modification_date = self.creation_date
        self.body = body[:2000] #Maximal size of the note
    
    def modify(self, new_body):
        """Provide the note bode modification. Fixes the date&time of modification"""
        self.body = new_body[:2000]
        self.modification_date = datetime.datetime.now()
    
    def __str__(self):
        """prints note as string with captions"""
        return f"Created: {self.creation_date}, Modified: {self.modification_date}, Body: {self.body}"


