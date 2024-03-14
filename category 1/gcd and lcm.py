a=int(input("Enter the number="))

b=int(input("Enter the number="))
x=a
y=b
while b!=0:
    temp=b
    b=a%b
    a=temp
gcd=a
print("GCD of {} and {} is {}".format(x,y,gcd))
lcm=int((x*y)/gcd)
print("LCM of {} and {} is {}".format(x,y,lcm))
