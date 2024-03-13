class A:

    def __init__(self):
        print("INITIT A")
    def feature1(self):
        print("FEATURE 1-A")    
    def feature2(self):
        print("FEATURE 2-A")       

class B:

    def __init__(self):
        print("INITIT B")
    def feature1(self):
        print("FEATURE 1-B")    

class C(B,A):

    
    def __init__(self):
        super().__init__()
        print("INITIT C")
    def feat(self):
        super().feature2()    


c1=C()
c1.feature1()
c1.feat()
