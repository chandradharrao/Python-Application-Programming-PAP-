'''
locks : impose limits on the shared resource : syn mechanizm
Class Lock ->acquire and release methods
Class "Value" -> simulate shared variable which itself is synchrized until mentioned with the Lock=False arg
'''

#without the lock mechanism
from multiprocessing import Process,Lock,Value
from time import sleep

def deposit(total):
    for i in range(100):
        sleep(0.01)
        total.value += 5
    return total

def withdraw(total):
    for j in range(100):
        sleep(0.01)
        total.value -= 5

if __name__=="__main__":
    total = Value("i",500,lock=False) #integer of value 500

    for i in range(5):
        add = Process(target=deposit,args=(total,))
        sub = Process(target=withdraw,args=(total,)) #shared variable total (not lock synchronized)

        add.start()
        sub.start()

        add.join()
        sub.join()

    print("After 5 iterations" , total.value)

'''total.value is not consistent,hence use locks'''

