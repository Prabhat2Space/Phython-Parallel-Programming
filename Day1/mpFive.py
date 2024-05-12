'''
    multi-processing with arguments
'''
import multiprocessing as mp
from time import sleep, perf_counter
from os import getpid 

def doSomeJob(args):
    print(f'Job Started...{getpid()}, {args}')
    sleep(args) 
    print(f'Job Completed...')
    print('*' * 40)


if __name__ == '__main__':
    start = perf_counter()

    pObj = mp.Process(target=doSomeJob, args=(2,)) 
    pObj.start()

    pObj.join()
    
    end = perf_counter()

    print(f'Time taken: {round(end-start,3)} secs')
