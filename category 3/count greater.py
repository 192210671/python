li=[8,1,2,2,3]
li2=[]
for i in range(len(li)):
    c=0
    for j in range(len(li)):
        if li[i]>li[j]:
            c+=1
    li2.append(c)        

print(li2)