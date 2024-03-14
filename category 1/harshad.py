#harshad number

n=int(input("Enter the number="))
sum=0
temp=n
while n>0:
  r=n%10
  sum+=r
  n=n//10
if temp%sum==0:
  print("harshad number")
else:
  print("Not heashad number")  



