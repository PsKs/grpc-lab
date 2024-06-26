# -*- coding: utf-8 -*-
from multiprocessing import Process
import client as client

if __name__ == '__main__':
    count = 2
    processes = {}
    
    for c in range(count):
        processes[c] = Process(target=client.run)

    for c in range(count):
        processes[c].start()
