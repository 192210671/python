def sum_of_n(n):
   sum=0
   for i in range(1,n+1):
    sum+=i
    i+=1
   return sum

# Test cases
print(sum_of_n(10))  # Expected output: 55
print(sum_of_n(25))  # Expected output: 325
print(sum_of_n(0))   # Expected output: 0
print(sum_of_n(100)) # Expected output: 5050
