from os import getpid
from multiprocessing import Process, Pipe

def childProcess(myPipeWrite):
    myPipeWrite.send([1001,"Some name here", 93745.234])
    print(f'Writing into the pipe done --> {getpid()}')
    myPipeWrite.close()


if __name__ == '__main__':
    print(f'Main/Parent Process here {getpid()}')

    pRead,pWrite = Pipe()

    pObj = Process(target = childProcess, args=(pWrite, ))
    pObj.start()

    print(f'Recieved... {pRead.recv()}')

    pObj.join()  # wait for the child process to complete

