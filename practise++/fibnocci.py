def fib(n):
    a=0
    b=1
    print("Fibnocci series is:")
    print(a)
    for i in range(n-1):
        c=a+b
        a=b
        b=c
        print(a)
n=int(input("Enter the Number:"))
fib(n)
