from email.policy import default
import multiprocessing
from multiprocessing.context import Process
import time

# use multiprocessing array, by default it will lock while other
# process updating

def print_array_content(arr):
    while True:
        print(*arr, sep=',')
        time.sleep(1)


if __name__ == "__main__":
    arr = multiprocessing.Array("i", [-1] * 10, lock=True)
    p = Process(target=print_array_content, args=([arr]))
    p.start()
    for j in range(10):
        time.sleep(2)
        for i in range(10):
            arr[i] = j