string=input("Enter the input")
alphabets,num,special,space=0,0,0,0
a=[]
d=[]
spl=[]

for i in range(len(string)):
  if(string[i].isalpha()):
    alphabets+=1
    a.append(string[i])
  elif(string[i].isdigit()):
    num+=1
    d.append(string[i])  
  elif(string[i].isspace()):
    space+=1
  else:
    special+=1
    spl.append(string[i])    

print("Alphabets:",alphabets,a)    
print("Numbers:",num,d)
print("Spaces:",space)
print("Special:",special,spl)
