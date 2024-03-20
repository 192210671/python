n1=1
n2=50
result=[]
for i in range(n1,n2+1):
    sqrt=int(i**0.5)
    if sqrt*sqrt==i:
        d_sum=sum(map(int,str(i)))
        if d_sum<10:
            result.append(i)
print(result)            
