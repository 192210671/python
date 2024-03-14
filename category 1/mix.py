'''29.Write a python program to find the difference between sum of square and square of sum N numbers
Sample input: N=5
Sample output: Diff=170
'''

x = int(input("Enter the Number: "))
a = (x * (x + 1) * (2 * x + 1)) / 6
b = ((x * (x + 1)) / 2) ** 2
z = a - b
print(z)
print("Difference:",z)
