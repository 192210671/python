class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
    def __str__(self):
        return self.m1,self.m2
    

s1=student(60,70)
s2=student(70,90)
s3=s1+s2
print(s3.m1)
print(s1.__str__())
