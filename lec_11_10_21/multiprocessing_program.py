'''
->multiprocessing : allows more than one **process** at the same time
->if single processor is present,then if we run multiple process on it,it has to interrupt/preempt processes to achieve concurrency
->if we have multiple processrs,then each processor can work with one process
'''
import multiprocessing

def printCubes(x):
    print(x*x*x)

def printSqr(x):
    print(x*x)

if __name__=="__main__":
    p1 = multiprocessing.Process(target=printSqr,args=(10,))
    p2 = multiprocessing.Process(target=printCubes,args=(10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main process Done...")