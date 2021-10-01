#special functions in py start with __spl_func_name__
#classes have attribute and methods
class Movie:
    def __init__(self,name,rating): #called implicitly when object is created
        self.mName=name #use self. to assign the name to specific instance
        self.mRating=rating

    def show(self): #pass self to refer to specific instance
        return (self.mName,self.mRating)

#object creation
m1=Movie("bahubali",4) #Movie.__init__(m1,"bahubali",4) behind the scenes
m2=Movie("dangal",5) #Movie.__init__(m2,"dangal",5)
