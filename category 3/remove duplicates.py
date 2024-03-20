n=int(input("Enter the no of elements:"))
l=[]
for i in range(n):
    x=int(input("Enter the number:"))
    l.append(x)

li2=list(set(l))
print(li2)    

