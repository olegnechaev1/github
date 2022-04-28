import re
class TXTService:
    with open("users.txt","w") as users_file:
        my_email = users_file.write("oleg@gmail.com\n")
        my_password = users_file.write("12345nechaev")
        
    @staticmethod
    def log_in(email: str, password: str):
        with open("users.txt","r") as users_file:    
            email_txt = users_file.readline().strip()
            password_txt = users_file.readline().strip()
        if email == email_txt and password == password_txt:
            print("\033[4m\033[31m\033[44m{}\033[0m".format("Рады приветствовать Вас Олег!!!!"))
        else:
            print("\033[4m\033[31m\033[44m{}\033[0m".format("Что то пошло не так,повторите попытку снова"))
            
    @staticmethod
    def sign_up(email: str, password: str):
        with open("users.txt","a") as users_file:
            users_file.write("\n")
            users_file.write(email)
            users_file.write("\n")
            users_file.write(password)

class User:
    @staticmethod
    def validate_credentials(email: str, password: str):
        email_rgx = re.compile(r'''\b([0-9A-Za-z]{1,}([0-9A-Za-z!#=?/^_`{|}~%&'*+-]{0,}[.]{0,1}
        |[.]{0,1}[0-9A-Za-z!#=?/^_`{|}~%&'*+-]{0,})[0-9A-Za-z]{1,})+@([A-Za-z0-9]{1,}[A-Za-z0-9-]{0,}
        [A-Za-z0-9]{1,}\.[A-Za-z0-9]{1,}[A-Za-z0-9-]{0,}[A-Za-z0-9]{1,}){0,63}\b''',re.X)
        password_rgx = r'[a-z0-9]{8,}'
        if re.fullmatch(email_rgx, email) and re.fullmatch(password_rgx, password):
            TXTService.sign_up(email, password)
            print("\033[4m\033[31m\033[44m{}\033[0m".format('Ваш email и password принят ,вы зарегистрированы'))
        else:
            print("\033[4m\033[30m\033[42m{}\033[0m".format('Проверьте правильность ввода email или password'))
    
class Menu:
    def __init__(self, choice):
        self.choice = choice
    @staticmethod
    def show_menu():
       print("\033[4m\033[30m\033[43m{}\033[0m".format("Введите enter для входа или registr для регистрации:"))

    @staticmethod
    def get_choice():
        return(input("Ввод:"))

    @staticmethod
    def ask_credentials():
        email = input("введите email:")
        password = input("введите password:")
        return (email, password)

    def processing_user_choice(self):
        if self.choice == 'enter': 
            email, password = self.ask_credentials()
            TXTService.log_in(email, password)
        elif self.choice == 'registr':
            email, password = self.ask_credentials()
            with open("users.txt","r") as users_file:    
                email_txt = users_file.readline().strip()
                password_txt = users_file.readline().strip()
            if email == email_txt and password == password_txt:
                print("\033[4m\033[30m\033[42m{}\033[0m".format('Такие данные уже есть'))
            else:    
                User.validate_credentials(email, password)
            
def main():
    while True:
        Menu.show_menu()
        user_choice = Menu.get_choice()
        user = Menu(user_choice)
        user.processing_user_choice()
        return main()
main()
