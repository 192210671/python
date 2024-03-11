
def fact(x):
  if x==0:
    return 1
  else:
    return x*fact(x-1)  
x=5
result=fact(5)
print(result)    
