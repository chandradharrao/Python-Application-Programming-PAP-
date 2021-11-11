from threading import Semaphore, Thread
from time import sleep

s = Semaphore(1) #default is 1

def f1():
    print("func1 starting")

    s.acquire() #acquire semaphore
    for i in range(5):
        print("func1 working...")
        sleep(1)
    s.release() #done with critical section
    print("Done func1...")

def f2():
    print("func2 starting")

    s.acquire()
    for i in range(5):
        print("func2 working...")
        sleep(1)
    s.release()
    print("Done func2")


t1=Thread(target=f1)
t2=Thread(target=f2)
t1.start()
t2.start()

t1.join()
t2.join()

'''
output:
func1 starting
func1 working...
func2 starting
func1 working...
func1 working...
func1 working...
func1 working...
Done func1...
func2 working...
func2 working...
func2 working...
func2 working...
func2 working...
Done func2


Simulate spin lock using
while not s.aqcuire(blocking=False): #returns False if it cannot acquire semaphore since its made non blocking
    #blocking=False=>no blocking but ret False immediately
    print("func2 blocked since no semaphore avaiable")
    sleep(1)

'''