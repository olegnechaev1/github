from datetime import datetime
def my_decor (func):
    """ Декоратор показывает время выполнения функции,количество аргументов и их соотвнтственно """
    def wrapper(*args,**kwargs) :
        start = datetime.now()
        func(*args,**kwargs)
        end = datetime.now()
        diff = end - start
        print(f"Время выполнения функции : {diff.total_seconds()/60}")
        func_1 = len(args) + len(kwargs)
        print(f"Количество аргументов : {func_1}")
        argss = [repr(arg)for arg in args]
        kwargss = [repr(kwarg)for kwarg in kwargs]
        func_2 = ",".join(argss+kwargss)
        print(f"Аргументы в функции : {func_2} ")
 #не мог красиво вывести результат через str,поэтому пришлось почитать и применить repr и join       
    return  wrapper    
@my_decor                 
def names (names,username):
    return f"hello {names} {username}" 
names("oleg","nechaev")
@my_decor
def num (a, b, c):
    return a + b + c
num(2, 5, 8)

print(my_decor.__doc__ )

my_list = [-1, 20, -80, -10, 66, 70, -19, 33, 34, 35, 66 ,-77]
my_list = list(filter(lambda x : x < 0 , my_list))
print(my_list)