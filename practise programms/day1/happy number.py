def is_happy(n):
    def get_next(num):
     
        total_sum = 0
        while num > 0:
            digit = num % 10
            total_sum += digit ** 2
            num //= 10
        return total_sum

   
    slow = n
    fast = n
    while True:
        slow = get_next(slow)         
        fast = get_next(get_next(fast))  

        if slow == fast:  
            return False

        if slow == 1 or fast == 1:  
            return True


number_to_check = 19
result = is_happy(number_to_check)
print(f"{number_to_check} is a happy number: {result}")
