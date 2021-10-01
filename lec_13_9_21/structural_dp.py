#decoupling implmentation and interface
#composition of object and classes
#hide inner details/complexity adn provide simplified frontend to the client
#facade - front of the building

'''
Facde design pattern
    Test automation framework:
        -each test has run() method
        -build a facade so that all the runs() neednt have to be called explicitly
'''
import time
class TestCase:
    def __init__(self,n) -> None:
        self.t_num = n
    def run(self):
        print(f"-----IN TEST{self.t_num}-----")
        time.sleep(1)
        print("Running test cae...")
        time.sleep(1)
        print("test case finished")

class Testrunner: #facade interface to all testcases
    def __init__(self) -> None:
        #create test case objects to be run
        self.t1 = TestCase(1)
        self.t2 = TestCase(2)
        self.t3 = TestCase(3)

    def runAll(self):
        self.t1.run()
        self.t2.run()
        self.t3.run()

Test = Testrunner()
Test.runAll()