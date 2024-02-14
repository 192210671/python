def incrementor(n):
  return lambda x:x+n
f=incrementor(50)

for i in range(0,10):
  print(f(i))




