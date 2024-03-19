s=input("Enter the string:")
vowels="AaEeIiOoUu"
news=""
for i in range(len(s)):
  if s[i] not in vowels:
    news+=s[i]
print("String after removing vowels:")
s=news
print(s)    
