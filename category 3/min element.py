li=[4,7,3,8,9,10]
left=0
right=len(li)-1
while left<right:
    mid=left+(right-left)//2
    if li[mid]>li[right]:
        left=mid+1
    else:
        right=mid
min_element=li[left]
print(min_element)     
