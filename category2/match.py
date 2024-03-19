
def match(l1,l2):
  count=0
  for i in range(min(len(l1),len(l2))):
    if l1[i].lower()==l2[i].lower():
      count+=1
    return count  

l1="what"
l2="watch"

print(match(l1,l2))
