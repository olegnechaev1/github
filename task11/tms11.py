class MyCustomException(Exception):
    pass

class Menu:
    def __init__(self, choice):
        self.choice = choice
    @staticmethod
    def show_menu():
       print("Вы в калькуляторе , выберете операцию :  + , - , * , / , % :")

    @staticmethod
    def get_choice():
        return(input("Операция:"))

    @staticmethod
    def ask_number():
        num_1 = float(input("Введите  число:"))
        if  num_1 > 1000000:
          raise  MyCustomException("так не надо,слишком большие числа")
        num_2 = float(input("Введите  число:"))
        return(num_1, num_2)

    @staticmethod    
    def ask_number_1():
        num_1 = float(input("Введите  число:"))
        return num_1
    def obtain_user_choice(self):
        if self.choice == "+":
            num_1,num_2 = self.ask_number()
            Calculator.get_sum(num_1, num_2)
        elif self.choice == "-":
            num_1, num_2 = self.ask_number()
            Calculator.get_subtraction(num_1, num_2)
        elif self.choice == "*":
            num_1, num_2 = self.ask_number()
            Calculator.get_multiplication(num_1, num_2)
        elif self.choice == "/":
            num_1, num_2 = self.ask_number()
            Calculator.get_division(num_1, num_2)
        elif self.choice == "%":
            num_1 = self.ask_number_1()
            Calculator.get_percent(num_1)
            return(num_1) 
        return(num_1, num_2) 

class Calculator:
    @staticmethod
    def get_sum(num_1, num_2):
        print(num_1 + num_2)

    @staticmethod
    def get_subtraction(num_1, num_2):
        print(num_1 - num_2)

    @staticmethod
    def get_multiplication(num_1, num_2):
        print(num_1 * num_2)

    @staticmethod
    def get_division(num_1, num_2):
        print(num_1 / num_2)

    @staticmethod
    def get_percent(num_1):
        print(num_1 /100)

def main():
    while True:
        try:
            Menu.show_menu()
            user_choice = Menu.get_choice()
            user = Menu(user_choice)
            user.obtain_user_choice()
            return main()
        except ZeroDivisionError:
            print("\033[4m\033[31m\033[44m{}\033[0m".format("На ноль делить нельзя!!!!"))
        except ValueError:
            print("\033[4m\033[30m\033[43m{}\033[0m".format("Только числа!!!!"))
        except MyCustomException:
            print("\033[4m\033[31m\033[45m{}\033[0m".format("так не надо,слишком большие числа"))
        except UnboundLocalError:
            print("\033[4m\033[30m\033[42m{}\033[0m".format("Ввод неверный"))    

main()
