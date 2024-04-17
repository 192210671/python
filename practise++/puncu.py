def remove_punctuations(string):
    new_string=""
    for char in string:
        if char.isalpha() or char.isalnum() or char.isspace():
            new_string+=char

        else:
            new_string+=""
    return new_string
string="Hello, World!"
print(remove_punctuations(string))
