'''
Invented by Dijkstra 
oldest synchronization mechanism and its **PRIMITIVE**
p() , v() -> used by Dijstra
manages an internal counter which reduces its count when acquired and increases is count when released

A semaphore CAN be released more times than ACQUIRED but a bounded semaphore CANNOT be incremented above its starting value and throws an exception if we try to do so.
'''

from threading import Semaphore , BoundedSemaphore

s1 = Semaphore(5) #5 processes can enter CS
print(s1._value) #access its count

s1.acquire() #boolean value indicating whether acquired or not,also reduces s1's value by 1
print(s1._value)

s1.release() #increments value but returns boolean indicating if operation was a success or not
print(s1._value)

s1.release()
print(s1._value) #so we are able to release without acquiring :). meaning less,hence use bounded semaphores

s2 = BoundedSemaphore(10)
s2.acquire() #if s2._value <0,then the thread/process will sleep until some other thread has called for release.By default the parameter "BLOCKING" is set to true.If we se it to False,it will NOT block the thread when the _value of semaphore becomes less than zero,but it would return FALSE immediately.Hence we would have to impleent a while loop by ourselves to do spin lock.
print(s2._value)

s2.release() #no params
print(s2._value)

s2.release() #releasing WITHOUT acquiring in Bounded Semaphore -> valueError Exception : semaphore released too many times.Hence we need to use try except blocks
print(s2._value)