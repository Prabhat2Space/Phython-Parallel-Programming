#!/usr/bin/python3

from time import sleep
from threading import Thread


class MyThread(Thread):

    def run(self):
        print(f'Job started...')
        sleep(1)
        print(f'Job completed...')


if __name__ == '__main__':
    tObj = MyThread()
    tObj.start()
    print('Waiting for child thread to complete')
    tObj.join()

