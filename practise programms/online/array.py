from array import *

arr=array('i',[])

n=int(input("Ente the Size of array"))

for i in range(n):
   x=int(input("Enter the Element"))
   arr.append(x)
print(arr)

val=int(input("Enter the element to search"))
k=0

for e in arr:
  if e==val:
    print("Index Value =",k)
    break
  k+=1
print(arr.index(val))

