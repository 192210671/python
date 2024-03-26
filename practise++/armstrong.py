n=int(input("Enter the number:"))
sum=0
temp=n
for i in range(1,n+1):
    r=temp%10
    sum+=r**3
    temp=temp//10
if sum==n:
    print("It is armstrong number")
else:
    print("It is not armstrong number")
