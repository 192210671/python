

def add(a,b):
    print("SUM:",a+b)
def sub(a,b):
    print("DIFF:",a-b)
def mul(a,b):
    print("PRODUCT:",a*b)
def div(a,b):
    if b==0:
        print("DIVISION NOT POSSIBLE")
    else:
        print("DIVISION:",a//b)


a=int(input("Enter the Number"))
b=int(input("Enter the Number:"))

add(a,b)
sub(a,b)
mul(a,b)
div(a,b)

