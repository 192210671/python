class A:

    def __init__(self):
        print("INITIT A")
    def feature1(self):
        print("FEATURE 1-A")    

class B:

    def __init__(self):
        print("INITIT B")
    def feature1(self):
        print("FEATURE 1-B")    

class C(B,A):

    
    def __init__(self):
        super().__init__()
        print("INITIT C")
c1=C()
c1.feature1()
