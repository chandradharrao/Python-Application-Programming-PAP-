
class Father:
    def __init__(self):
        print("Dad init")

    def method1(self):
        print("I am in meth1")

    def m1(self):
        print("in father")

class Mother:
    def method_m(self):
        print("Mother")

    #same name as father's memeber func
    def m1(self):
        print("In mother")
    
class Child(Father):
    def __init__(self):
        print("child init")
        #call init of super class
        super().__init__()

    def method2(self):
        print("In method2")

#derived class with multiple inheritance
#MRO - Father and then Mother
class Offsprint(Father,Mother):
    print("in m3")

#how to call init of parent?
#A: use super method in child
c1 = Child()

#method resolution operator works from left to right operation when inherited function with same name is called in child
#hence m1 of Father is called.
c1.m1()