numbers =[i for i in range(20)]
print(numbers)
    

def some_num(numbers:int)->int:
    numbers=int(input("число:"))
    numbers =[i for i in range(numbers+1)]
    return(numbers)
print(some_num(numbers))


import datetime
def current_time ():
    print(datetime.datetime.now())
    return current_time
a =[current_time() for i in range(1,50)]
print(a)


my_list =[1,1,1,2,3,1,2]
output = dict((i, my_list.count(i)) for i in set(my_list))
print(f"Output:{output}")


