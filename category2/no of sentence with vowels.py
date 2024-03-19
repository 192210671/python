def countstring(n,start):
  if n==0:
    return 1
  count=0
  for i in range(start,5):
    count+=countstring(n-1,i)

  return count    
def vowelstring(n):
  return countstring(n,0)  
n=int(input("n="))
print(vowelstring(n))  
