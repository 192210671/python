from datetime import *


def findday(d,m,y):
    date=datetime(year,month,day)
    weekday=date.weekday()
  
    


    weekdays=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
   
    return weekdays[weekday]
 

day=16
month=12
year=2004


r=findday(day,month,year)
print(r)