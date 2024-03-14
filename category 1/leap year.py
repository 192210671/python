#print leap year if not leap year print previous leap year

a=int(input("Enter the date="))
b=int(input("Enter the month="))
c=int(input("Enter the year="))
print("Date =",a,"/",b,"/",c)

if(c%4==0 and c%400==0 or c%100!=0):
  print("LEAP YEAR")
else:
  print("NOT LEAP YEAR")

x=c%4
if(x!=0):
  print("Previous leap year is:",c-x)
else:
  print("Next leap year is:",c+4)  



  
