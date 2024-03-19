text="Hello world"
char='l'
newtext=""
for i in range(len(text)):
    if text[i]!=char:
        newtext+=text[i]
text=newtext
print("Newtext:",text)        
