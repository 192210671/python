'''Write a python program to insert an element in a specific index.
 Sample input: 
Enter the number of elements=5
Enter the elements: 47,34,21,89,12

Enter the element to be Inserted: 100
Position: 4

Sample output: [12,21,34,100,47,89]
'''
li=[]
n=int(input("Enter no of Elements:"))

for i in range(n):
    x=int(input("Enter the element:"))
    li.append(x)
print("Array is:",li)

k=int(input("Enter the position of element to insert:"))
ele_k=int(input("ENter the element"))
li.insert(k,ele_k)

print("Updated List is:",li)

