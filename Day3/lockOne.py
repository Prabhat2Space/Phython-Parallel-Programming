#!/usr/bin/python3

from time import sleep
from random import randint
from threading import Thread, RLock

def doSomeJob(lock, ident, value):
    #acquire the lock
    with lock:
        print(f'Thread ID: {ident} got the lock going to sleep for {value} secs')
        sleep(value)
        with lock: #already lock trying to acquire again...
            pass #dead lock occurs



if '__main__' == __name__: 
    lock = RLock() # re-entrant lock

    for i in range(5):
        Thread(target=doSomeJob,args=(lock, i+1,randint(1,3))).start()  
        

