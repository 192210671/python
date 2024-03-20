
li=[1,-1,9,-2,7,-3]

avg=sum(li)/len(li)

for i in range(len(li)):
    if li[i]<0:
        li[i]=avg


print(sorted(li))
       
