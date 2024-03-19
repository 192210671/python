def removecommonwords(s1,s2):
    com=[]
    l1=list(s1.split())
    l2=list(s2.split())
    for i in l1:
        if i in l2:
            l1.remove(i)
            l2.remove(i)
            com.append(i)
            continue
    print(*l1)
    print(*l2)
    print("common words:",*com)
s1="sky is blue in color"
s2="raj likes sky blue color"
removecommonwords(s1,s2)

