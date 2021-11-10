'''
Invented by Dijkstra 
synchronization **PRIMITIVE**
p() , v() -> used by Dijstra
manages an internal counter which reduces its count when acquired and increases is count when released
'''

from threading import Semaphore , BoundedSemaphore

s1 = Semaphore(5) #5 processes can enter CS
print(s1._value)

s1.acquire() #boolean value indicating whether acquired or not,also reduces s1's value by 1
print(s1._value)

s1.release()
print(s1._value)

s1.release()
print(s1._value) #so we are able to release without acquiring :). meaning less,hence use bounded semaphores

s2 = BoundedSemaphore(10)
s2.acquire() #if s2._value <0,ten it will sleep until some other thread has called for release.By default Blocking parameter is true,else it will not block and it will return FALSE immediately.
print(s2._value)

s2.release() #no params
print(s2._value)

s2.release() #releasing without acquiring -> valueError Exception : semaphore released too many times.Hence we need to write try except blocks
print(s2._value)