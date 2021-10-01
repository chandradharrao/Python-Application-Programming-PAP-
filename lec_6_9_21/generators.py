#yields a value from an iterator
#generator funcs allow us to declare a function to behave as an iterator
#the generator func is a normal func except that it has yield keyword
#the position of the yield statement is remembered by the generator
#when generator is exhausted,it raises stopIteration exception
#they are lazy

def shoot():
    print("hi")
    yield 100 #control returned to next statmeent

    print("Hello")
    yield 300

    print("good")
    yield 500 #one or more yield statements


f = shoot() #generator object returned for the first time excution

res = next(f)
print(res)

res = next(f)
print(res)

res = next(f)
print(res)

res = next(f)
print(res)
