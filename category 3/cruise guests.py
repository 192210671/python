t=int(input("Enter instance time:"))
e=[7,0,5,1,3]
l=[1,2,1,3,4]
x=[0,0,0,0,0]

for i in range(t):
    if t>len(e) and t>len(l):
        print("Out of index")
    else:
        x[i]=(x[i-1]+e[i])-l[i]
        print(x[i],end=" ")

print("MAx:",max(x))