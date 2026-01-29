from uuid import uuid4
from hashlib import sha256



class User:
    
    def __init__(self, username: str, password: str, first_name: str, last_name: str, id: str | None = None):
        self.username = username
        self.password = str(sha256(password.encode()).hexdigest())
        self.first_name = first_name
        self.last_name = last_name

        if id:
            self.id = id
        else:
            self.id = str(uuid4())
                
                
    def return_dict(self):
        result = {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
        return result
        