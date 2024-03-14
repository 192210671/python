n=int(input("Enter the number:"))
factors=[]
for i in range(1,n+1):
  if n%i==0:
    factors.append(i)

print(factors)
print("No of factors=",len(factors))

k=int(input("Enter the position="))
print("Element at {} position is {}".format(k,factors[k-1]))
