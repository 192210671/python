#prime numbers in range
y=int(input("Enter the number="))
for n in range(2,y):
 for x in range(2,n):
  if n % x== 0:
    print(n,'equals',x,'*',n//x)
    break
 else:
      print(n,' is a prime number')
