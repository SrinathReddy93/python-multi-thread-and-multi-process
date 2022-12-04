from multiprocessing import Lock
from threading import Thread


import time

def red_robot(lock1, lock2):
    while True:
        print('Red Accuring lock 1...')
        lock1.acquire()
        print('Red Acquire lock 2...')
        lock2.acquire()
        print('Red locks acquired...')
        lock2.release()
        lock1.release()
        print('Red lock released...')
        time.sleep(0.5)

def blue_robot(lock1, lock2):
    while True:
        print('Blue Accuring lock 2...')
        lock2.acquire()
        print('Blue Acquire lock 1...')
        lock1.acquire()
        print('Blue locks acquired...')
        lock1.release()
        lock2.release()
        print('Blue lock released...')
        time.sleep(0.5)


mutex1 = Lock()
mutex2 = Lock()

red = Thread(target=red_robot, args=(mutex1, mutex2))
blue = Thread(target=blue_robot, args=(mutex1, mutex2))

red.start()
blue.start()