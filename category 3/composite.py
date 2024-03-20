li=[33,45,66,23,45,56]
count=0
for num in li:
    if num<4:
        continue
    for i in range(2,num):
        if num%i==0:
            count+=1
            break
print("No of composite Numbers:",count)        
