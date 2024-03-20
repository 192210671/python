n1=1
n2=10

if n1>n2:
    print("Invalid")
else:
    result=[(i,i**2) for i in range(n1,n2+1)]
print(result)        
