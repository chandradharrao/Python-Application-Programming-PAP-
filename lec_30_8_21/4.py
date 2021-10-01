#variables - instance and class/static variables
#class var - inside cass but outside function,belongs to entire class

#methods - instance methods,class methods,static methods
#static method is not related to ie independent to any class,any instance is called static method
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