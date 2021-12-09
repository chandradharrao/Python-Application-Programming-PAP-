from threading import Thread

x = 0

def inc():
    global x
    x+=1

def dec():
    global x
    x-=1

def task1(n):
    for i in range(n):
        inc()

def task2(n):
    for i in range(n):
        dec()

if __name__=="__main__":
    x=0
    print(x)

    t1 = Thread(target=task1,args=(1000000,))
    t2 = Thread(target=task2,args=(1000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(x)
    print("Done")

'''
expected:1000000+1000000=2000000
output:215999
'''