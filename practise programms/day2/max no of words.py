def max_words_in_sentence(sentences):
    max_words = 0

    for sentence in sentences:
        words = sentence.split()
        max_words = max(max_words, len(words))

    return max_words

sentences1 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(max_words_in_sentence(sentences1))  

sentences2 = ["please wait", "continue to fight", "continue to win"]
print(max_words_in_sentence(sentences2))  

sentences3 = ["the heads", "of", "two", "sorted linked lists"]
print(max_words_in_sentence(sentences3)) 

sentences4 = ["python", "is", "an object-oriented programming language"]
print(max_words_in_sentence(sentences4))  

sentences5 = ["python", "is", "an interactive language"]
print(max_words_in_sentence(sentences5))  
