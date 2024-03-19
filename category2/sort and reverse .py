string=input("Enter the string:")
string=string.upper()
str1=sorted(string)

str2="".join(str1)
rev=str2[::-1]
print(str2)
print(rev)
