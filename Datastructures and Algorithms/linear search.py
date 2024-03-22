#linear search

pos=-1
def search(list,n):
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True
       






list=[1,2,3,6,8,9]
n=int(input("Enter the element to search:"))

if search(list,n):
    print("FOund at:",pos+1)
else:
    print("Not Found")    
