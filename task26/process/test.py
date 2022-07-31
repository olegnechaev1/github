import multiprocessing


def cube(num):
    print(f'Cube:{num*num*num}')
      

if __name__ == '__main__':
    x1 = multiprocessing.Process(print(cube(5, )))
    x2 = multiprocessing.Process(print(cube(2, )))
      
    x1.start()
    x1.join()
    x2.start()
    x2.join()