'''
Demonstrate Race Condition:
Race condition can happen in wither single or multi processor systems because processes can get preempted before complete execution of its non-atomic operation.

This can be overcommed using "Locks".
'''

from time import sleep
from threading import Thread

#demostrate race condition - print letters in pairs - get letters in pairs
#inputs:
#s1 - "AABBCCDDEEFF"
#s2 - "aabbccddeeff"
#result - "aaAAbbBBccCCddDDeeEEffFF"

sleepTime=0.5

def capPrinter():
    s1 = 'AABBCCDDEEFF'
    for i in s1:
        print(i,end="")
        sleep(sleepTime) #to make sure that this thread is PREEMPTED
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
    output obtained : AaAaBbBbCcCc.... ie the Critical Sections are not atomic since they are preempted,we can use locks to make them atomic.
    '''