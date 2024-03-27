x=[[1,2],
   [2,4],
   [4,6]]
r=[[0,0,0],[0,0,0]]

for i in range(len(x)):
      for j in range(len(x[0])):
            r[j][i]=x[i][j]
for i in r:
      print(i)
