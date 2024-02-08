def sumsquare(l):
    odd_sum = 0
    even_sum = 0

    for num in l:
        if num % 2 == 0:
            even_sum += num ** 2
        else:
            odd_sum += num ** 2

    return [odd_sum, even_sum]


n = int(input("Enter the number of elements: "))
input_list = []
for i in range(n):
    element = int(input("Enter the element: "))
    input_list.append(element)


result = sumsquare(input_list)
print(result)
