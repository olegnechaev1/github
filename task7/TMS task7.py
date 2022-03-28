from datetime import datetime
def get_function_description(func):
    """ Декоратор показывает время выполнения функции,количество аргументов и их соотвнтственно """
    def wrapper(*args,**kwargs) :
        start = datetime.now()
        func(*args,**kwargs)
        end = datetime.now()
        diff = end - start
        print(f"Время выполнения функции : {diff.total_seconds()/60}")
        func_1 = len(args) + len(kwargs)
        print(f"Количество аргументов : {func_1}")
        argss = [repr(arg) for arg in args]
        kwargss = [repr(kwarg) for kwarg in kwargs]
        func_2 = ",".join(argss+kwargss)
        print(f"Аргументы в функции : {func_2} ")
 #не мог красиво вывести результат через str,поэтому пришлось почитать и применить repr и join       
    return  wrapper    
@get_function_description                 
def get_personal_data(names,surname: str)-> str:
    return f"hello {names} {surname}" 
get_personal_data("oleg","nechaev")
@get_function_description
def num (a, b, c: int)-> int:
    return a + b + c
num(2, 5, 8)

print(get_function_description.__doc__ )

my_list = [-1, 20, -80, -10, 66, 70, -19, 33, 34, 35, 66 ,-77]
my_list = list(filter(lambda x : x < 0 , my_list))
print(my_list)
