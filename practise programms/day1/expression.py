import re

def is_valid_number(s):
   
    pattern = re.compile(r'^[+-]?(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?$')

   
    match = pattern.match(s)

  
    return match is not None


print(is_valid_number("0"))      
print(is_valid_number("e"))      
print(is_valid_number(" "))       
print(is_valid_number("."))       
print(is_valid_number("%"))     
