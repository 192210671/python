#inner classes


class student:


    def __init__(self,name,rollno):

         self.name=name
         self.rollno=rollno
         self.lap=self.laptop()


    def show(self):
         print(self.name,self.rollno)
         self.lap.show()      

    
    class laptop:
        def __init__(self):
              self.brand='Hp'
              self.config='i5'
              self.ram=8
        
        def show(self):
             print(self.brand,self.config,self.ram)
             



s1=student('Eswar',17)
s2=student('Sriram',18)
s1.show()





