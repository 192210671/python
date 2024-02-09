def remove_common_words(s1, s2):
  
    words_s1 = set(s1.split())
    words_s2 = set(s2.split())

  
    common_words = words_s1.intersection(words_s2)

    modified_s1 = ' '.join(word for word in s1.split() if word not in common_words)
    modified_s2 = ' '.join(word for word in s2.split() if word not in common_words)

    return modified_s1, modified_s2


s1_1, s2_1 = "sky is blue in color", "Raj likes sky blue color"
result1 = remove_common_words(s1_1, s2_1)
print(result1[0])
print(result1[1])
print()

s1_2, s2_2 = "learn python", "python is easy to learn"
result2 = remove_common_words(s1_2, s2_2)
print(result2[0])
print(result2[1])
print()

s1_3, s2_3 = "raju likes apple", "apple is red in color"
result3 = remove_common_words(s1_3, s2_3)
print(result3[0])
print(result3[1])
print()

s1_4, s2_4 = "sita likes orange", "orange is rich in anti-oxidants"
result4 = remove_common_words(s1_4, s2_4)
print(result4[0])
print(result4[1])
print()

s1_5, s2_5 = "raj is travelling to Chennai in train", "the rain will reach Chennai at 8 pm"
result5 = remove_common_words(s1_5, s2_5)
print(result5[0])
print(result5[1])
