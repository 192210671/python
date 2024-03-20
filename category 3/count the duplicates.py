li=[1,1,1,2,3,4,5,6,7,7,7,3,3,5,6]
li2=[]
for i in li:
    if li.count(i)>1:
        li2.append(i)


print(set(li2))

