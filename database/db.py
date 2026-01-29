import json
from models.users import User



class DB:
    def __init__(self):
        self.file_name = "C:/Users/user/Desktop/najotTalim_Darslari/dars28/my_ecommercase/database/db.json"

    def is_username_in_database(self, username: str) -> bool:
        with open(self.file_name) as json_file:
            data = json.loads(json_file.read())
            
            for user in data["users"]:
                if user["username"] == username:
                    return False
                
            return True
        
    
    def add_user(self, user: User):
        data = user.return_dict()
        with open(self.file_name) as json_file:
            content = json.loads(json_file.read())  
            content["users"].append(data)
            
        with open(self.file_name, "w") as file:
            file.write(json.dumps(content))