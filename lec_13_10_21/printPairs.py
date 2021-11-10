'''
Race condition can happen in single processor system  too because processes can get premted before completion of a non atomic operation.

Can be overcommed using Locks
'''

from time import sleep, time
from threading import Thread

#demostrate race condition - get letters in pairs
#s1 - "AABBCCDDEEFF"
#s2 - "aabbccddeeff"

sleepTime=0.5

def capPrinter():
    s1 = 'AABBCCDDEEFF'
    for i in s1:
        print(i,end="")
        sleep(sleepTime)
        print(i,end='')
        sleep(sleepTime)

def smallPrinter():
    s2 = "aabbccddeeff"
    for i in s2:
        print(i,end='')
        sleep(sleepTime)
        print(i,end='')
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