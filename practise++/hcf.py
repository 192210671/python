def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)
a=int(input("Enter the Number:"))
b=int(input("Enter the NUmber:"))

if hcf(a,b):
    print("The HCF of {} and {} is :{}".format(a,b,hcf(a,b)))
else:
    print("Enter correct Values")
