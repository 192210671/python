

class A:
    def show(self):
        print("Father as fther")
class B(A):
    def show(self):
        print("son as Father")        

a1=B()
a1.show()        
