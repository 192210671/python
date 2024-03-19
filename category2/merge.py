l1="welcome"
l2="homely"
n=int(input("n="))
output=""
i,j=0,0
while i<len(l1) and j<len(l2):
  output+=l1[i:i+n]+l2[j:j+n]
  i+=n
  j+=n
output+=l1[i:]+l2[j:]
print(output)  
