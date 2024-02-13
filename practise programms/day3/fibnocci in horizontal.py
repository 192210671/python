#fibnocci series in line

n=int(input("Enter the range="))
a,b=0,1
while a<n:
  print(a,end=',')
  a,b=b,a+b
