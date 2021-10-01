#Inheritance
#single level inheritance

class Parent:
    def __init__():
        print("Par init")
    def method1(self):
        print("I am in meth1")
    
#inherit from parent
class Child(Parent):
    def __init__():
        print("child init")
    def method2(self):
        print("In method2")

class GrandChild(Child):
    def __init__():
        print("Grand child init")
        
    def meth3(self):
        print("meth3")

c1=Child()
c1.method2()
c1.method1()

c3 = GrandChild()
c3.method1()

#if GrandChild doesnt have __init__(), then it will go to the available super class init method
