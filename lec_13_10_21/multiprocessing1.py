from multiprocessing import Process,Value

def task1(x):
    for i in range(10000):
        x.value+=1

def task2(x):
    for i in range(10000):
        x.value-=1

if __name__=="__main__":
    x = Value('i',0)
    print(x.value)

    p1 = Process(target=task1,args=(x,))
    p2 = Process(target=task2,args=(x,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(x.value)


'''
Locked Versions

def task1(x):
    for i in range(10000):
        with x.get_lock():
            x.value+=1

def task2(x):
    for i in range(10000):
        with x.get_lock():
            x.value-=1
'''