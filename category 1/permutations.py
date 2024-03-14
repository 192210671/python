import itertools
n=(input("Enter the number="))
p=list(itertools.permutations(n))
print(*["".join(x) for x in p])
