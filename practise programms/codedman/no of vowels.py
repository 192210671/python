def count_vowels(input_string):
    # Initialize a dictionary to store vowel counts
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Convert the input string to lowercase for case-insensitivity
    input_string_lower = input_string.lower()

    # Iterate through the string and count vowels
    for char in input_string_lower:
        if char in vowel_counts:
            vowel_counts[char] += 1

    return vowel_counts

# Example function calls and printing their outputs
if __name__ == "__main__":
    example1 = count_vowels("Hello World")
    example2 = count_vowels("Python Programming is Awesome")
    example3 = count_vowels("Myths")  # String with no vowels
   

    print("Example 1:", example1)
    print("Example 2:", example2)
    print("Example 3:", example3)
 
