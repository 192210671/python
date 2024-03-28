def pyramid(height):
    for i in range(height):

        for j in range(i):
            print("*",end="")
        print(" ")



height=int(input("Enter the Height:"))
pyramid(height)
