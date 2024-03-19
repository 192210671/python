n="A man,a plan,a canal:Panama"
s=n.lower()
text=""
for i in s:
    if i.isalpha():
        text+=i
x=text[::-1]
if x==text:
    print("palindrome")
else:
    print("not palindrome")            
