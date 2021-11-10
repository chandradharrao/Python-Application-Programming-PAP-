from multiprocessing import Lock,Process,Value
from os import rename
from time import sleep, time

lock = Lock() #lock object needs to be acquired BEFORE making changes to the shared var and released AFTER making changes.Also we cannot declare it inside the main function but SHOULD be a global variable

def deposit(total):
    for i in range(100):
        sleep(0.01)
        lock.acquire()
        total.value+=5
        lock.release()
    return total

def withdraw(total):
    for i in range(100):
        sleep(0.01)
        lock.acquire()
        total.value-=5
        lock.release()
    return lock

if __name__=="__main__":
    total = Value('i',500)
    for i in range(5):
        add = Process(target=deposit,args=(total,))
        sub = Process(target=withdraw,args=(total,)) #shared variable total
        add.start()
        sub.start()

        add.join()
        sub.join()

    print("After 5 iter",total.value) #now consstency maintained