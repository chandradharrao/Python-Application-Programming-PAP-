'''
producer : generate data -> keep in buff 
consumer : consume data -> remove from buff

Hindrance : consumption from empty buffer
            producer produces into full buff

global buffer
producer thread
consumer thread

Suppose consumer has consumed entire buffer and producer is still sleeping due to time.sleep().The the consumer should wait until producer produces items.
Hence we need to use **condition objects** which allows one or more threads to wait until NOTIFIED by another thread ie consumer should wait until notified by the producer.Hence the two threads can **communicate** between each other.

condtion is accociate with locks
acquire() and release() with the lock
'''

#using condition object

from threading import Thread,Condition
from time import sleep
from random import choice

buffer = []
buffer_max = 5
condition = Condition()

class ProducerThread(Thread): #inherit from thread class
    options = range(1,6) 

    def produce(self):
        return choice(self.options)

    def run(self): #override thread run method

        #every 1 seconds produce an item
        while True:
            item = self.produce()

            #acquire lock for shared variable
            condition.acquire()
            global buffer
            if len(buffer)==buffer_max:
                print("Queue full,hence producer going to sleep...")
                condition.wait() #block thread unti notified by consumer
                print("Space avaiable now.Hence pushing...")

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

            print("Item was pushed to queue.Hence waking up..")
            x = self.consume()
            print("consumed ",x)
            condition.notify() #wakeup producer if it was sleeping
            condition.release()
            sleep(1)


ProducerThread().start()
ConsumrThread().start()