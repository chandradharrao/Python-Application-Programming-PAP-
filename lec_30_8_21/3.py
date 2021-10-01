class CSFaculty:
    def __init__(self,name,experience):
        self.name = name
        self.experience = experience
    
    def expertise(self,domain):
        print(domain)

cs1 = CSFaculty("rama","20")
cs1.expertise("ml")