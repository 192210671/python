

li=[1,2,3,1,1,3]
count=0
for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if li[i]==li[j] and i<j:
            print("Good Pairs:",li[i],li[j])
            print("(",i,j,")")
            count+=1

print("no of Good pairs ara:",count)


