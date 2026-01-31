import json
from hashlib import sha256

from models.users import User
from database.db import DB
from models.products import Product


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
    
    
    
    
class ProductService:
    
    def products_name(self) -> list[Product]:
        data = db.get_all_products()
        
        return [Product.from_dict(product) for product in data]
        
        



class Cart:
    def __init__(self):
        self.cartitem = CartItem()        
        
        
    def add_product_to_cart(self, user: User, product_id: int) -> None:
        cart_item = self.cartitem
        db.add_product_to_cart(user.id, )  
    
        
class CartItem:
    def __init__(self, product_id: int, quantity: int = 1):
        pass