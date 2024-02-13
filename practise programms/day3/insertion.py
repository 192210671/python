#insertion
words=['Eswar','Sriram','Vamsi']
for w in words[:]:
  if len(w)>5:
    words.insert(2,w)

    print(words)
