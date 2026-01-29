import json

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
    
    
    def login(self, username: str, password: str):
        pass
    
    def is_username_in_database(self, username: str):
        return db.is_username_in_database(username)