a=input("Enter the first binary number=")
b=input("Enter the second binary number=")
c=input("Enter the third binary number=")
x=int(a,2)
y=int(b,2)
z=int(c,2)

if x>y and x>z:
  print("{} is greates".format(a))
elif y>x and y>z:
  print("{} is greates".format(b))
else:
  print("{} is greatest".format(c))    
