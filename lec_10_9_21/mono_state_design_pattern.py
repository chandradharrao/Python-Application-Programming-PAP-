'''
all objs in py have an attr called __dict__ which is a dict obj containing all attributes defined for that object in a dictionary
'''

class A:
    pass
print(A.__dict__) #empty dictionary as class has empty

class B:
    def __init__(self,name):
        self.cname=name
print(B.__dict__) #contains info abt class in key,val pairs

class C:
    def __init__(self,name):
        self.cname=name
c = C('chandra')
print(c.__dict__) #contains onfo abt the obj of C type in key value pairs

'''
Both _dict and _shared point to the same dictionary and hence updating _dict updates the dictionary pointed by _shared too.
'''
_shared = {}
_dict = _shared

_dict["x"]=1
_dict['y']=2

print(_shared) #output: {'x': 1, 'y': 2}

'''
philosophy of borg design patter(under creational design patter):many instances possible but all of them use the same data!
Hence syntacticaly sugar over sigleton.
no headache of maintaining "single" instance
'''
#parent class
class MonoState:
    #class variable
    _shared = {} 

    def __init__(self): #self here is the Obj created using User Class
        self.__dict__ = MonoState._shared #py dicts assignment is bidirectional assignment

#User objs shld follow mono state paradigm
class User(MonoState):
    def __init__(self,name,password):
        super().__init__() #assign __dict__ of the object passed through self with class variable so that the state of the object passed though self is same as that of class variable _shared

        self.name=name
        self.passkey=password
        #these statements will clear self.__dict__ and update name,password into self.__dict__.This will also change _shared

o1 = User('chandra','xxx')
o2 = User('ajinkya','yyy')

print(o1.name)
print(o2.name)

