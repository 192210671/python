string=input("Enter the string:")
vcount,ccount=0,0
vowels="AaEeIiOoUu"
c=[]
v=[]
for i in range(len(string)):
  if string[i] in vowels:
    vcount+=1
    v.append(string[i])
  elif string[i]!=" " and string[i] not in vowels:
    ccount+=1
    c.append(string[i])

print("Total no of vowels: {}and consonanats: {}".format(vcount,ccount))
