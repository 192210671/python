import itertools
p=itertools.permutations([1,1,2])
per=list(dict.fromkeys(list(p)))

permutations=[list(num) for num in per]
print(permutations)
