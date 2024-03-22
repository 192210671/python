#Exception Handling


a=int(input('Enter the numerator:'))
b=int(input("Enter the denominator:"))


try:
    print("Program Opens")
    print("Division is:",a/b)
    k=int(input("Enter the some element:"))
    print("K=",k)

except Exception as e:
    print("Exception:",e) 

finally:
    print("program Ends")       
