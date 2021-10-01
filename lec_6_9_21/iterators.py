'''https://www.programiz.com/python-programming/iterator'''
#iterable data structures eg : lists,tuples,dictionaries,strings
#strings and tuples are immutables
#iterators are iterable objects
#they are container class objects.
#container class supports iter function
'''
implementation of for loops:

#create iteratble object(hence return self in __iter__())
a = iter([1,2,3]) 
while(true):
    try: next(a)
    except: break
'''

#py iterables must implement iterator protocol => __iter__() and __next__()
#hence list is also an generator since it implements __next__()
class Contain:
    def __init__(self,i_list):
        self.array = i_list
        self.n = len(self.array)

    #convert the class instance to an ITERABLE class
    def __iter__(self):
        self.i = 0
        return self #returns the iterator object itself so that for loops can traverse

    def __next__(self):
        if self.i < self.n:
            self.i+=1
            return self.array[self.i-1]
        else:
            raise StopIteration

c = iter(Contain([1,2,3,4])) #create the iterable object by calling spl iter func ie iter(Contain.__iter__(c)) is called

while True:
    try:
        print(next(c)) #print(Contain.__next__(c))
    except:
        break
