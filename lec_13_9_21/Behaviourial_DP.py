#communication b/w classes and objects
#decoupling b/w implementation and interface

'''
Objects- subscribe to publisher class to recieve notifications and unsubscribe when not interested.
Publisher publishes notification to subscribers

Youtube analogy : youtube.com : users subscribe to interested channels and recieve notifications when the youtube channel uploads.
'''

#observer template
class Publisher:
    def __init__(self):
        pass
    def subscribe(self,user):
        pass #override : same function signature but different implentation
    def unubscibe(self,user):
        pass
    def notifyAll(self):
        pass

#subscriber template
class Subsciber:
    def __init__(self,name):
        pass
    def notifyMe(self,postData):
        pass

#functionality:
#option to subscribe
#subscibers shld get notified
class YoutubeChannel(Publisher):
    def __init__(self):
        self.subscribers=[] #set of subscribers

    #function to alow user subscibers
    def subscribe(self,user):
        if user not in self.subscribers:
            self.subscribers.append(user)
    
    #function to unsubsciber
    def unubscibe(self,user):
        if user in self.subscribers:
            self.subscribers.remove(user)

    #function to notify users
    def notifyAll(self,postName):
        for user in self.subscribers:
            user.notifyMe(postName) #call the function of the subscriber as user subscibers by passing address of a function to be called later
    
    #function to create new notification
    def newNotification(self,postName):
        self.notifyAll(postName)
    

class User(Subsciber):
    def __init__(self,name):
            self.name = name

    def notifyMe(self,postData):
        print(f"{self.name} recieved - {postData}!!")

if __name__ == "__main__":
    u1 = User("chandra")
    u2 = User("Ajinkyaye")
    u3 = User("Shardul")

    Tseries = YoutubeChannel()
    for u in [u1,u2,u3]:
        Tseries.subscribe(u)
    
    Tseries.newNotification("Tum hi ho song released")

    Tseries.unubscibe(u3)
    Tseries.newNotification("Channa mereya ho song released")