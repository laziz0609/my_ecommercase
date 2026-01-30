import json
from hashlib import sha256

from models.users import User
from database.db import DB


db = DB()

class UserService:     
        
    def register(self, username: str, password: str, first_name: str, last_name: str) -> User:
        user = User(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        db.add_user(user)
        return user
    
    
    def login(self, username: str, password: str) -> User | None:
        shifr_password = password = str(sha256(password.encode()).hexdigest())
        data = db.login_user(username, shifr_password)
        if data != None:
            return User.cast_user(data) 
    
    
    def is_username_in_database(self, username: str) -> bool:
        return db.is_username_in_database(username)