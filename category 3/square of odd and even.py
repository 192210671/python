l=[]
while True:
    num=int(input("Enter the number:"))

    if num==-1:
     break
    else:
     l.append(num)

    neg_array,pos_array=[],[] 

    for i in l:
      if i<0:
        neg_array.append(i)
      else:
        pos_array.append(i)  
    neg_sum,pos_sum=0,0 
    for i in neg_array:
      neg_sum+=i  
    for i in pos_array:
      pos_sum+=i   

print("Array is:",l)
print("Negative elements:{} with sum {}".format(neg_array,neg_sum))
print("Positive elements:{} with sum :{}".format(pos_array,pos_sum))