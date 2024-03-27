def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

k=int(input("Enter the No of Numbers:"))

if k<=0:
    print("Enter the Positive Numbers")
else:
    print("Fibnocci series is:")
    for i in range(k):
        print(fib(i),end=" ")
