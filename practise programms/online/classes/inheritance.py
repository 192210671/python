
class A:
    def feature1(self):
        print("A")
    def feature2(self):
        print("B")    
class B:
    def feature3(self):
        print("C")   
    def feature4(self):
        print("D")    
class C(A,B):
    def feature5(self):
        print("E")
             


a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.feature3()   
b1.feature4()     
c1=C()
c1.feature1()
