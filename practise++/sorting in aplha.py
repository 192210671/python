def order(string):
    words=string.split()
    words.sort()
    return ("".join(words))




string=input("Enter the String:")

print(order(string))
