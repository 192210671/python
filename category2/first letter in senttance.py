string="the cat on the wall"
l1=list(string.split())
print(l1)


for i in range(len(l1)):
    print(l1[i][0].upper(),end=".")
    continue
