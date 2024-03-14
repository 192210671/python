def fact(n):
    if n==0 or n==1:
        return 1
    if n>1:
        return n*fact(n-1)

num=int(input("Enter the sum"))
sum=0
for i in range(1,num+1):
  sum+=fact(i) 
print(sum)
