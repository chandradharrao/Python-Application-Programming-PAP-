#generate iterable powers of 2 ie 1,2,4,8,16...

class powTwo:

    def __init__(self,m):
        self.maxpow = m

    def __iter__(self):
        self.i=0
        return self #return the iterable

    def __next__(self):
        if self.i<=self.maxpow:
            res = pow(self.i,2)
            self.i+=1
            return res
        else:
            raise StopIteration

p = powTwo(10)
p_iterable = iter(p)

while True:
    try:
        print(next(p_iterable))
    except:
        break
