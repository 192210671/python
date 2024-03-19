def anagrams(li):
    dict={}
    for word in li:
        sw="".join(sorted(word))
        if sw not in dict:
            dict[sw]=[word]
        else:
            dict[sw]+=[word]
    return [dict[i] for i in dict]            


li=['pop','bat','tab','opp','cat']
print(anagrams(li))


