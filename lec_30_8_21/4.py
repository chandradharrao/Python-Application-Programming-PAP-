#eg:https://colab.research.google.com/drive/17fJvV7E84S5AL-AFdYkdLN_A8yo5elZg#scrollTo=YV-slKxVTchc

#variables types - instance,class and static variables
    #class var - inside class but outside functions,belongs to entire class
    #instance variables - belongs to only the instances

#methods types - instance methods,class methods,static methods
    #static method cannot use either class variable nor instance variables
    #class methods cannot use instance variables but can use class varaibles using "cls" since they don't take in "self" as parameter
    #instance methods can use both class variables and instance variables

#classmethods can access only class variables using cls.It cannot access instance variables

#staticmethods cannot access niether class variables nor instance variables

#instance method can access both class and instance variables

class Movie:
    num_of_movie_objs = 0

    def __init__(self,name,rating): 
        self.mName=name 
        self.mRating=rating

    def show(self): 
        return (self.mName,self.mRating)

    @classmethod #class method decorator
    def class_method(cls): #cls refers to the class
        print(cls.num_of_movie_objs)

    @staticmethod #a static method
    def static_methods():
        print("I am static meth")

print(Movie.num_of_movie_objs)
Movie.num_of_movie_objs+=100
try:
    m1 = Movie("x",5)
    print(m1.num_of_movie_objs)

    m2 = Movie("t",6)
    print(m2.num_of_movie_objs)
except:
    pass

Movie.class_method()
Movie.static_methods()
