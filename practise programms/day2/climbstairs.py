def climbStairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2

   
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]


print(climbStairs(2)) 
print(climbStairs(3)) 
print(climbStairs(4))  
print(climbStairs(1)) 
print(climbStairs(5))  
