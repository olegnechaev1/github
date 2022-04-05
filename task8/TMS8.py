with open("users.txt","w") as users_file:
    my_email = users_file.write("oleg@gmail.com\n")
    my_password = users_file.write("12345nechaev")
with open("users.txt","r") as users_file:    
    email = users_file.readline().strip()
    password = users_file.readline().strip()

def check_email_and_password():
    email2 = input("введите новый email:")
    password2 = input("введите новый password:")
    password3 ="".join(i for i in password2 if password2.isalnum())
    with open("users.txt","a") as users_file:
        if email2.count("@") == 1 and email2[0] != "@" \
            and email2.count(".") >= 1 \
            and email2.rfind(".") >  email2.find("@") and len(password2) >= 8 and password2==password3\
            and email2 != email and password2 != password:    
            users_file.write("\n")
            users_file.write(email2)
            users_file.write("\n")
            users_file.write(password2)
            print("Правильный логин и пароль вы зарегистрировались")
        else:
            print("Неправильный пароль или логин")

admin = input("Введите enter для входа или registr для регистрации:")
if admin=="enter":
    email1 = input("введите email:")
    password1 = input("введите password:")
    if email1==email and password1==password:
        print("Рады приветствовать Вас Олег!!!!")
elif admin=="registr":
    check_email_and_password()
else:
    print("что то пошло не так,повторите попытку снова")



    
    