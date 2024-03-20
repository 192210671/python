li=[1,2,4,3,5,6,7,8,9,10]
prime=[]

for i in li:
    if i<2:
        continue
    for j in range(2,i):
        if i%j==0:
            break
        else:
            prime.append(i)
            break
print("Priime NUmbers:",prime)        
