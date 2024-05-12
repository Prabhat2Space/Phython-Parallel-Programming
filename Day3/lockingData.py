#!/usr/bin/python3

from os import getpid
from threading import Thread,Lock
from time import sleep

data = 0
size = 1000000

lock = Lock() # synchronize the access to shared data..

def myFun():
    global data
    print(f'Remember ... {getpid()}--> data: {data}')
    with lock:
        for _ in range(size):
            data+=1

    print('*' * 40)


if __name__ == '__main__':
    print(f'In main... {getpid()}')
    with lock:
        for _ in range(size):
            data+=1

    t1 = Thread(target=myFun)
    t1.start()
    print('-' * 40)
    with lock:
        for _ in range(size):
            data+=1
    print(f'Intermediary data: {data}')
    t2 = Thread(target=myFun)
    t2.start()

    t1.join()
    t2.join()
    print('$' * 40)
    print(f'Finally before exiting  data: {data}')

