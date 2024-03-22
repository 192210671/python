file=open("mydata",'r')

f1=open("other",'w')
for data in file:
    f1.write(data)

f2=open("other",'a')
f2.write("BYE")    


