from abc import ABC,abstractmethod

class computer:
    @abstractmethod
    def process(self):
        pass

class programmer:
    def work(self,com):
        print("Solving problems")
        com.process()    
class laptop(computer):    
    def process(self):
        print("It is running")



com1=laptop()
prog=programmer()
prog.work(com1)

