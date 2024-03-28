
def polindrome(string):
    new_str=string[::-1]
    return string==new_str
string=input("Enter the String:")
if polindrome(string):
    print("Polindrome")
else:
    print("Not Polindrome")
