from threading import Thread

def doSomeJob():
    for _ in range(10): 
        print('X',end='')



if '__main__' == __name__ : # main thread
    tObj = Thread(target = doSomeJob) 
    tObj.start()
    tObj.join()

    for _ in range(10): 
        print('O', end='')
