
def modify(s):
  f={}
  for char in s:
    f[char]=f.get(char,0)+1
  result=""

  for char in s:
    cd=ord(char)+f[char]
    if cd>122:
      cd-=26
    result+=chr(cd)
  return result    
s="ghee"
modified=modify(s)
print(modified)  
