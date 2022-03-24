numbers = [i for i in range(20)]
print(numbers)
    

def some_num(numbers:int)->int:
    numbers = int(input("число:"))
    numbers = [i for i in range(numbers+1)]
    return(numbers)
print(some_num(numbers))


import datetime
def current_time (num):
    time = []
    for i in range(num):
        date = datetime.datetime.now()
        i = date.time().strftime("%H:%M:%S")
        time.append(i)
    print(time)
    return time
a = [i for i in current_time(6)]


my_list =[1,1,1,2,3,1,2]
output = dict((i, my_list.count(i)) for i in set(my_list))
print(f"Output:{output}")


