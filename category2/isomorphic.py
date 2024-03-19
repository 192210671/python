def isomorphic(s1,s2):
  if len(s1)!=len(s2):
   return False
  else:
    m1,m2={},{}
    for i in range(len(s1)):
      ch1,ch2=s1[i],s2[i]
      if ch1 not in m1:
        m1[ch1]=ch2
      print(m1) 
      if ch2 not in m2:
        m2[ch2]=ch1
      print(m2)
      if m1[ch1]!=ch2 or m2[ch2]!=ch1:
        return False
  return True         


s1="egg"
s2="add"

print(isomorphic(s1,s2))
