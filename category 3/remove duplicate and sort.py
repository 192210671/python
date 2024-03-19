li=[1,3,2,1]
u=[]
for i in li:
    if i not in u and li.count(i)==1:
        u.append(i)
print(list(sorted(u)))        
