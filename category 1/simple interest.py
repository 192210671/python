

'''
10.	Write a program using function to calculate the simple interest. Suppose the customer is a senior citizen. She is being offered 15 percent rate of interest; he is being offered 12 percent rate of interest for all other customers, the ROI is 10 percent.
Sample Input:
Enter the principal amount: 200000 Enter the no of years: 3
Gender (m/f): m
Is customer senior citizen (y/n): n Sample Output:
Interest: 60000
'''

def simpleinterest(a,y,r):
  Interest=(a*y*r)/100
  print("Interest=",Interest)



a=int(input("Enter the amount="))
y=int(input("Enter no of years="))
g=str(input("Enter the gender(m/f)="))
c=str(input("Is customer is senior citizen(y/n)="))


if c=='y':
  if g=='m':
     r=12
  elif g=='f':
    r=15
elif c=='n':
  r=10
  

simpleinterest(a,y,r)  

