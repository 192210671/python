#remove punctuation
def removepunc(string):
    new_text=""
    for i in string:
        if i.isalpha():
            new_text+=i
        elif i.isalnum():
            new_text+=i
        else:
            new_text+=" "
    return new_text

string=input("Enter the String:")

print(removepunc(string))
