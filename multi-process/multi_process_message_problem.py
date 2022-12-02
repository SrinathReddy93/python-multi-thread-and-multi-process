from multiprocessing.context import Process
import time

# creating new process and running print_array_content method
# after from main process we are trying to update "arr", that update
# data is not showing in new process

def print_array_content(arr):
    while True:
        print(*arr, sep=',')
        time.sleep(1)


if __name__ == "__main__":
    arr = [-1] * 10
    p = Process(target=print_array_content, args=([arr]))
    p.start()
    for j in range(10):
        time.sleep(2)
        for i in range(10):
            arr[i] = j