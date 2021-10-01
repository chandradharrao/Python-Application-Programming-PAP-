#creational design pattern - https://www.youtube.com/watch?v=ub0DXaeV6hA&ab_channel=DerkBanas
'''
If we want a method to return one of several possible classes but share a common super class 

Eg:
Create different types of enemy(each enemy would be an obj of diff enemy type classes) randomly in Unity
Here we need to choose the class type at runtime ie we dont know before hand what type of enemy (class )object we need to create
'''

#common super class interface
class Enemy:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    
    #superclass interfaces
    def getName(self):
        return self.name
    
    def getHealth(self):
        return self.health

#two types of enemies that could be creating at runtime (Just to demonstrate factory design)
class Type1(Enemy):
    def __init__(self, name, health):
        super().__init__(name, health)

#inherit common superclass type for interface
class Type2(Enemy):
    def __inti__(self,name,health):
        super().__init__(name,health)

#factory to generate object of different class types based on id
class EnemySpawner:
    def manufacture(self,i_id,name,health):
        if i_id==1:
            return Type1(name,health)
        if id==2:
            return Type2(name,health)

Factory = EnemySpawner()
enemy = Factory.manufacture(1,'xxx',100)
print(enemy.getName(),enemy.getHealth())

