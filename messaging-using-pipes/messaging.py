from multiprocessing import Process, Pipe

import time


def ping(pipe_con):
    while True:
        pipe_con.send(["ping", time.time()])
        pong = pipe_con.recv()
        print("ping 1", pong)
        time.sleep(1)

def pong(pipe_con):
    while True:
        pipe_con.send(["pong", time.time()])
        pong = pipe_con.recv()
        print("pong 1", pong)
        time.sleep(1)

def pong2(pipe_con):
    while True:
        pipe_con.send(["pong2", time.time()])
        pong = pipe_con.recv()
        print("pong 2", pong)
        time.sleep(1)


if __name__ == '__main__':
    pipe_end_a, pipe_end_b = Pipe()
    pipe_end_c, pipe_end_d = Pipe()
    Process(target=ping, args=(pipe_end_a,)).start()
    Process(target=pong, args=(pipe_end_b,)).start()
    Process(target=pong2, args=(pipe_end_c,)).start()
    Process(target=ping, args=(pipe_end_d,)).start()
