#happy number
def happy(n):
  sum=0
  temp=n 
  while temp>0:
    r=temp%10
    sum+=r**2
    temp=temp//10
  return sum  

n=int(input("Enter the number="))
result=n
while result!=1 and result!=4:
  result=happy(result)

  if result==1:
   print("True")
  elif result==4:
   print("False")  

