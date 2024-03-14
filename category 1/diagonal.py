#diagonal summ

a=[[1,2,3],
   [1,2,3],
   [1,2,3]]

sum=0

for i in range(len(a)):
  for j in range(len(a)):
    if i==j:
      sum=sum+a[i][j]

print("Sum of diagonal elements=",sum)      

