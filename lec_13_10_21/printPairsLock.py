from time import sleep, time
from threading import Thread,Lock

lock = Lock()

#demostrate race condition - get letters in pairs
#s1 - "AABBCCDDEEFF"
#s2 - "aabbccddeeff"

sleepTime=0.5

def capPrinter():
    s1 = 'AABBCCDDEEFF'
    for i in s1:
        #acquire lock before printing each pair so that it is not preemted
        lock.acquire()
        print(i,end="")
        sleep(sleepTime)
        print(i,end='')
        lock.release()
        sleep(sleepTime)

def smallPrinter():
    s2 = "aabbccddeeff"
    for i in s2:
        lock.acquire()
        print(i,end='')
        sleep(sleepTime)
        print(i,end='')
        lock.release()
        sleep(sleepTime)

if __name__=="__main__":
    t1 = Thread(target=capPrinter)
    t2=Thread(target=smallPrinter)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")

    '''
    actual output expected : AAaaBBbbCCcc...
    output obtained : AaAaBbBbCcCc.... ie the functions are not atomic,we can use locks to make them atomic
    '''