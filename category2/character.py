string=input("Enter the string:")
c=input("Enter the element to find:")

res=None
j=0
while j<len(string):
  for i in range(0,len(string),1):
    if string[i]==c:
      res=True
      print(string[i],"index:",i)
    j+=1
      
if res==None:
  printf("Character not found")      



