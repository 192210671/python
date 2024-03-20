li=[1,2,3,1]

new=[]

if len(li)==1 or li[0]>=li[1]:
    new.append(li[0])
if li[-1]>=li[-2]:
    new.append(li[-1])

for i in range(1,len(li)-1):
    if li[i]>=li[i-1] and li[i]>=li[i+1]:
        new.append(li[i])

print(new)
