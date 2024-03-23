
def sort(list):
    for i in range(len(list)):
        minpos=i
        for j in range(i,len(list)):
            if list[j]<list[minpos]:
                minpos=j
        temp=list[i]
        list[i]=list[minpos]
        list[minpos]=temp
        print(list)


list=[2,6,9,4,6,10,3,7]
sort(list)
print(list)
