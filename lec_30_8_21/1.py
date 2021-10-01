a=10 #object of class Int
print(type(a))

class Movie:
    def genre(self): #self is not a keyword,but a pointer pointing to a specific instance,if no self then typeError
        print("in genre")

Movie.genre() #without creating object

movie1 = Movie() #object of class Movie
movie2 = Movie()

Movie.genre(movie1) #behind the scenes,we pass the object to the class function
Movie.genre(movie2)

#industry standard
movie1.genre()





