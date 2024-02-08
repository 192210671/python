def modify_string(s):
   
    char_freq = {}
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

  
    modified_string = ''
    for char in s:
        frequency = char_freq[char]
        distance = (ord(char) - ord('a') + frequency) % 26
        modified_char = chr(ord('a') + distance)
        modified_string += modified_char

    return modified_string


print(modify_string("ghee"))      
print(modify_string("elephant"))  
print(modify_string("apple"))     
print(modify_string("orange"))    
print(modify_string("lion"))     
