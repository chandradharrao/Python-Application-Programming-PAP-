from threading import Thread,Lock
import time
import random

'''
issue : 
since we use random sleep,producer would be sleeping after execution of its critical section (ie after producing an item) but consumer would have ran its critical section (cunsumption code) more than once which causes it to consume more than one element from the queue leading to issues.

Hence error is caused when : consumer has consumed everything but producer has not produced anything.

Want: consumer should wait until notified by the producer
Hence use condition object.
'''

queue = []
lock = Lock()

class Item:
    def __init__(self,x):
        self.x = x

class Producer(Thread):
    def run(self):
        #produce iem every one second
        while True:
            lock.acquire()
            x = Item(100)
            print("produced",x.x)
            queue.append(x)
            lock.release()

            time.sleep(1*random.random())

class Consumer(Thread):
    def run(self):
        #every second conume item
        while True:
            lock.acquire()
            x = queue.pop()
            print("consumed",x.x)
            lock.release()

            time.sleep(1*random.random())

if __name__ == "__main__":
    p = Producer()
    c = Consumer()

    p.start()
    c.start()

    p.join()
    c.join()
