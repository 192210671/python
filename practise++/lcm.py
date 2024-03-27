def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)
def lcm(a,b,x):
    y=(a*b)/x
    return int(y)
a=int(input("Enter the Number:"))
b=int(input("Enter the Number;"))

x=hcf(a,b)

print("The Lcm of {} and {}:{}".format(a,b,lcm(a,b,x)))

