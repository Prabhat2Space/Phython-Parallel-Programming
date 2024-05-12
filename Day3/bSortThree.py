#!/usr/bin/python3

def bubbleSort(lst):
    size = len(lst)
    for i in range(size):
        swap = False
        for j in range(size-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swap = True
        if swap is False:
            break

if '__main__' == __name__ :
    from sys import argv,exit
    from random import randint
    from time import perf_counter
    from threading import Thread

    if len(argv) <= 1:
        print('pass size')
        exit(1)

    size = int(argv[1])
    lst = [randint(1, size * 10) for _ in range(size) ]
    start = perf_counter()
    print('Before List: ', lst)
    tObj = Thread(target=bubbleSort, args = [lst]) # first time sorting 
    tObj.start()
    tObj.join()
    print('After List: ', lst)
    end = perf_counter()
    print(f'Time taken: {round(end-start, 3)}')
        
