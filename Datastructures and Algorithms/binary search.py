
pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while 1<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1    
    return False
list=[1,2,5,6,7,9,10,20]
n=20
if search(list,n):
    print("Found at:",pos+1)
else:
    print("Not found")    
