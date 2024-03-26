
from cmath import *
a=float(input("Enter the co-efficient of x^2:"))
b=float(input("Enter the co-efficient of x:"))
c=float(input("Enter the constant:"))

d=(b**2)-(4*a*c)
sq=sqrt(d)
sol1=(-b-sq)/2*a
sol2=(-b+sq)/2*a

print("solution of Quadratic Equations is:{} and {}".format(sol1,sol2))
