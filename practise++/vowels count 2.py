
def count_vowels(string):
    count=0
    string=string.lower()
    vowels='aeiou'
    for i in range(len(string)):
        if string[i] in vowels:
            count+=1
    return count




string=input("Enter the String:")
print("Vowels:",count_vowels(string))
