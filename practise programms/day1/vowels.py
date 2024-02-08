def count_sorted_vowel_strings(n):
   
    vowel_count = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

   
    for _ in range(n - 1):
      
        vowel_count['e'] += vowel_count['a']
        vowel_count['i'] += vowel_count['e']
        vowel_count['o'] += vowel_count['i']
        vowel_count['u'] += vowel_count['o']

   
    total_count = sum(vowel_count.values())

    return total_count

print(count_sorted_vowel_strings(1))  # Output: 5
print(count_sorted_vowel_strings(2))  # Output: 15
