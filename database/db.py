import json
from models.users import User



class DB:
    def __init__(self):
        self.file_name = "C:/Users/user/Desktop/najotTalim_Darslari/dars28/my_ecommercase/database/db.json"


    def read_db_json(self) -> dict:
        with open(self.file_name) as json_file:
            data = json.loads(json_file.read())
            
        return data
    
    
    def write_db_json(self, data: json) -> None:
        with open(self.file_name, "w") as file:
            file.write(json.dumps(data, indent=4))
    
   
    def get_all_products(self) -> list[dict[str, int | str]]:
       data = self.read_db_json()
       return data["products"]
   
    
    def is_username_in_database(self, username: str) -> bool:
        data = self.read_db_json()

        for user in data["users"]:
            if user["username"] == username:
                return False
                
        return True
        
    
    def add_user(self, user: User) -> None:
        data = user.return_dict()
        content = self.read_db_json() 
        content["users"].append(data)
            
        self.write_db_json(content)
            
    
    def login_user(self, username: str, password) -> dict | None:
        data = self.read_db_json()
        users: list = data["users"]
        for user in users:
            if user["username"] == username and user["password"] == password:
                return user
                
        
    

