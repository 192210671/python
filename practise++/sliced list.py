#sliced list


list=[]
n=int(input("Enter the Range:"))
for i in range(n):
    x=int(input("Enter the Number:"))
    list.append(x)
print("List is:",list)
print("sliced List:",list[2:3])
