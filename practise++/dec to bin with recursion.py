def binary(n):
    if n>1:
        binary(n//2)

    print(n%2,end="")

n=int(input("Enter the decimal:"))

binary(n)
