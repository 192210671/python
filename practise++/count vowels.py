
def count_vowels(string):
    count=0
    string=string.lower()

    for char in string:
        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
            count+=1
    return count




string=input("Enter the String:")

print("No of Vowels:",count_vowels(string))
