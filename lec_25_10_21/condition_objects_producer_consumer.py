'''
producer : generate data -> keep in buff 
consumer : consume data -> remove from buff

Hindrance : consumption from empty buffer
            producer produces into full buff

global buffer shared variable
producer thread
consumer thread

Suppose **consumer** has consumed entire buffer and **producer** is still executing its Critical Section( due to time.sleep() ).Then the consumer should wait until producer produces items,which could lead to starvation.

Hence we need to use **condition objects** which allows one or more threads to wait until NOTIFIED by another thread ie consumer should wait until notified by the producer.Hence the two threads can **communicate** between each other.

Hence we can assocate a condition with tasks. 
acquire() and release() with the lock
'''

#using condition object

from threading import Thread,Condition
from time import sleep
from random import choice

buffer = []
buffer_max = 5 #max buffer size
condition = Condition() #condition object

class ProducerThread(Thread): #inherit from thread class
    options = range(1,6) 

    def produce(self):
        return choice(self.options)

    def run(self): #override thread run method

        #every 1 seconds produce an item
        while True:
            item = self.produce()

            #acquire lock before using wait() or notify() ONLY AFTER acquiring the lock
            condition.acquire()
            global buffer
            if len(buffer)==buffer_max:
                print("Queue full,hence producer going to sleep...")
                condition.wait() #block the thread and make it wait until notified by consumer ie dont execute further until woken
                print("Space avaiable now.Hence pushing...")

            #once woken or there is free space in buffer
            buffer.append(item)
            condition.notify() #wakeup the consumer if it is sleeping because no item was there in the queue
            condition.release()
            sleep(1)
            
class ConsumrThread(Thread):
    global buffer
    def consume(self):
       return buffer.pop()

    def run(self):
        #consume every 1 second
        while True:
            condition.acquire() #**cannot wait before acquiring lock**
            if not buffer: #if no items
                print("Consumer gong to sleep...")
                condition.wait()

            #if buffer is not empty or thread is woken up
            print("Item was pushed to queue.Hence waking up..")
            x = self.consume()
            print("consumed ",x)
            condition.notify() #wakeup producer if it was waiting for buff to become empty
            condition.release()
            sleep(1)


ProducerThread().start()
ConsumrThread().start()