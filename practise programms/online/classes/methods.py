class student:


    school="saraswathi"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    #instance methods
    def avg(self):

        return (self.m1+self.m2+self.m3)/3  
    
    #class method
    
    @classmethod
    def schoolinfo(cls):
        return cls.school
    
    #static method

    @staticmethod

    def info():

        print("It is good ")

s1=student(13,15,16)
s2=student(18,19,20)


print(s1.avg())

print(s2.avg())
print(student.schoolinfo())
student.info()
