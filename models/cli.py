import sys
from getpass import getpass

from termcolor import colored, cprint


from serivices import UserService#, ProductService




class Cli:
    
    def __init__(self):
        self.current_user = None
        self.userservice = UserService()
        #self.productservice = ProductService()
        
        
    def run(self) -> None:
        while True:
            if self.current_user == None:
                self.print_login_menu()
                
                choice = input(colored("> ", "blue"))
                if choice == "1":
                    print("-------------------Products-------------------\n")
                    # self.show_products()
                    
                elif choice == "2":
                    self.login()
                    
                elif choice == "3":
                    self.register()
                        
                elif choice == "0":
                    self.quit()

                else:
                    cprint("bunday menu mavjud emas\n", "yellow")
                
            else:
                self.print_logout_menu()
                choice = input(colored("> ", "blue"))
                
                if choice == "1":
                    print("-------------------Products-------------------\n")
                
                elif choice == "2":
                    pass
                
                elif choice == "3":
                    cprint("logout\n", "yellow")
                    self.current_user = None
                    
                elif choice == "0":
                    self.quit()
                
                else:
                    cprint("bunday menu mavjud emas\n", "yellow")
                
    
    # def show_products(self) -> None:
    #     data = self.productservice.products_name()
        
    
                 
    def login(self) -> None:
        while True:
            cprint("bosh sahifaga qaytish uchun shunchaki enter tugmasini bosing", "yellow")
            username = input("username: ").strip()
            if username == "":
                break
            password = getpass("password: ").strip()
            if password == "":
                break

            checker = self.userservice.login(username, password)
            if checker != None:
                cprint("siz login qilindingiz\n", "green")
                self.current_user = checker
                break
            else:
                cprint("username yoki password xato !!!\n", "red")

              
    def register(self) -> None:
        loop = True
        while loop:
            cprint("bosh sahifaga qaytish uchun shunchaki enter tugmasini bosing", "yellow")
            username = input("username: ").strip()
            if username == "":
                break
            if self.validate_username(username):
                if not self.userservice.is_username_in_database(username):
                    cprint("bunday username mavjud\n", "red")
                    continue  
            else:
                cprint("username faqat harf, son va tagchiziqlardan iborat bo'lishligi kerak\n", "red")
                continue
    
            password = getpass("password: ").strip()
            if password == "":
                break 
            if not self.validate_password(password):
                cprint("password 4 ta belgidan ko'p bo'lishligi kerak\n", "red")
                continue
            
            coniform = getpass("coniform password: ").strip()
            if coniform == "":
                break
            if coniform != password:
                cprint("coniform pasword va password bir xil bo'lishligi kerak\n", "red")
                continue
            
            first_name = input("first name: ").strip()
            if first_name == "":
                break

            last_name = input("last name: ").strip()
            if last_name == "":
                break
            
            self.current_user = self.userservice.register(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            cprint("muvafaqqiyatli ro'yxatdan o'tdingiz\n", "green")
            break 
            
    
    def print_login_menu(self) -> None:
        menu = "-------------------Menu-------------------\n"
        menu += "1. Products\n"
        menu += "2. Login\n"
        menu += "3. Register\n"
        menu += "0. Quit\n"
        print(menu)
        
        
    def print_logout_menu(self) -> None:
        menu = "-------------------Menu-------------------\n"
        menu += "1. Products\n"
        menu += "2. My Cart\n"
        menu += "3. Logout\n"
        menu += "0. Quit\n" 
        print(menu)      
    
    
    def quit(self):
        cprint("ko'rishguncha", "blue")
        sys.exit()
       
    
    
        
    @staticmethod  
    def validate_username(username: str) -> bool:
        result = username.replace("_", "")
        return result.isalnum()

    @staticmethod
    def validate_password(password: str) -> bool:
        return len(password) >= 4



