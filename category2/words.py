string='''This is the most straightforward way to count the number
of lines in a text file in Python. The readlines() method reads all
lines from a file and stores it in a list. Next, use the len() function
to find the length of the list which is nothing but total lines present in a file.'''

str1=string.split(".")
str1.pop()
print("No of lines:",len(str1))
print("No of words in each line:")
for i in range(len(str1)):
  words=str1[i].split()
  print("Line:",i+1,len(words))
