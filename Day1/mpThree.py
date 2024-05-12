'''
    working on single process --- no parallelism
'''
import multiprocessing as mp
from time import sleep, perf_counter
from os import getpid 

def doSomeJob():
    print(f'Job Started...{getpid()}')
    sleep(1) 
    print(f'Job Completed...')
    print('*' * 40)


if __name__ == '__main__':
    start = perf_counter()

    pObj = mp.Process(target=doSomeJob)
    pObj.start()

    pObj.join()
    
    end = perf_counter()

    print(f'Time taken: {round(end-start,3)} secs')
