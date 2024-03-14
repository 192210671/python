'''11.	Find the number of factors for the given number and print the 1st N factors of the given number.
Sample Input: Given number: 100
N: 4
Sample Output: Number of factors = 9
1st 4 factors are: 1, 2, 4, 5
'''


n=int(input("Enter the number:"))
factors=[]
for i in range(1,n+1):
  if n%i==0:
    factors.append(i)

print(factors[:4])    
