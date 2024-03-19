s=input("Enter the string:")
s=s.lower()
r=[]



for i in range(0,len(s)):
  count=1
  for j in range(i+1,len(s)):
    if s[i]==s[j] and s[i]!=" ":
      count=count+1

      s=s[:j]+'0'+s[j+1:]
  if count>1 and s[i]!='0':
      r.append(s[i])
      print(s[i],count)

print("No of characters repeated:",len(r),r)
