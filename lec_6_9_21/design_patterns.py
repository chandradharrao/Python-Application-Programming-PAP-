'''
design patters:resusable solns for certain problems.
Observe/Learn pattern from problems and use them for new problems
used as a template and NOT A SOLUTION

char:
.lang indepent
.dynamic
.scalable
.generic

categoized into:
1.creational - how to create objects?
2.structural - decoupling interface and implementation of classes and objects 
3.behaviourial - focuses on relationship/communication between classes and objects
'''

'''
creational design patterns
-how to instantiate objects??

1)Singleton - creates only one object for a class
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