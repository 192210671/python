a=int(input("Enter the Number:"))

for i in range(2,a):
    if  a%i==0:
        print("It is not prime Number")
        break
    else:
        print("{} is prime number ".format(a))
