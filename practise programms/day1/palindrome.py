def is_palindrome(x):
 
    str_x = str(x)
    

    return str_x == str_x[::-1]


number_to_check = 121
result = is_palindrome(number_to_check)
print(f"{number_to_check} is a palindrome: {result}")
