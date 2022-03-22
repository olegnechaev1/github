while True:
        num=input("введите число от 0 до 15 :")
        try:
            num = int(num)
            if num < 16:
                if num <=9 :
                    print("Ты серьезно, давай еще разок)")
                elif num >=11:
                    print("Не сдавайся,почти угадал)")
                else:
                    print("Урааа угадал)))") 
                    break
            else:
                print("неверный формат данных или число")
             
        except ValueError:
            print("неверный формат данных или число")