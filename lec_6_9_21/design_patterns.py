'''
design patters:resusable soln templates for certain problems.
Observe/Learn pattern from problems and use them for new problems
used as a template and NOT A SOLUTION

chars:
.lang indepent
.dynamic
.scalable
.generic

categoized into:
1.creational - how to create objects?
2.structural - decoupling interface and implementation of classes and objects 
3.behaviourial - focuses on communication between classes and objects
'''

'''
creational design patterns
-how to instantiate objects??

1)Singleton - creates only one object for a class

FLOW:
1.create object of class GM
2.this calls __init__ of gm.
3.since instance is none,the object itself is the instance
4.then to get the current instance,we call getInstance()
5.since instance already exists,instance is returned
6.else Singleton() is called which creates the object and assigns to instance recursively.
7.this is now returned.
'''
class GameManager:
    #class variable 
    instance = None

    #class emthod
    @classmethod
    def get_instance(): #either return a new instance or the existing instance when called
        if GameManager.instance != None:
            GameManager() #create object if not already present
        return GameManager.instance

    def __init__(self):
        if GameManager.instance != None: #if already exists
            raise Exception("Trying to violate Singleton!")
        else: #if trying to create first time
            GameManager.instance = self

gm = GameManager()
print(gm) #reference to the class instance

print(GameManager.get_instance()) #same as gm as singleton