'''
process : program under execution.
Code + PC + registers + stacks and so one..

thread : lightweight process handled by scheduler
share code segment but has its own

ti = threading.Thread(target=func_pointer,args=(params_to_func))
ti.start()
....
..
.
ti.join() ****imp***

main thread runs on its own without waiting for the inner threads to finish execution and hence terminates itself.Because main thread's job is only to create threads and start them.Hence make main thread wait for t1 and t2 to complete.
'''
import threading
import time

def printCubes(x):
    time.sleep(10000)
    print(x*x*x)

def printSqr(x):
    time.sleep(10000)
    print(x*x)

def multiply(x,y):
    print(x*y)

if __name__=="__main__":
    t3 = threading.Thread(target=multiply,args=(10,20))
    t1 = threading.Thread(target=printCubes,args=(12,))
    t2 = threading.Thread(target=printSqr,args=(12,))

    t3.start()
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("T1 and T2 done,hence main thread exitting...")

'''
x=20 #global
def f1():
    x=30 #local
    print(x)->30

x=20
def f1():
    x+=1
    print(x)->error : global variables can only be accessed and not manipulated without explicitly mentioning that tey are global variables

def f1():
    global x
    x+=1
    print(x)->21
'''

#global variable
x=0

def incrGlobal():
    global x
    x+=1

def taskOfThread():
    for _ in range(10000000):
        incrGlobal()


def main():
    global x
    x=0

    #both tring to inc same shared global variable -> hence use locks
    t1 = threading.Thread(target=taskOfThread)
    t2 = threading.Thread(target=taskOfThread)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    for i in range(10):
        main()
        print(i,x)

'''
Main thread is present by default
along with that there would be the threads created by us
'''
import threading
import time

def iAmLegend():
    time.sleept(10)
    print("thread")

th = threading.Thread(target=iAmLegend,name="thread_1")
th.start()
print("state of ",th.getName(),"is ",th.is_alive())
print("Current number of threads = ",threading.active_count()) #total number of active threads in the program = 1 + 1 = 2

th.join()
print("after joining,si the thread still alive?",th.is_alive())

#main thread is executing no matter what
print("Main thread",threading.main_thread().name)



