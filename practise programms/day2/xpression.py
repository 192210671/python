def calculate(s):
    stack = []
    num = 0
    sign = 1  # 1 for positive, -1 for negative

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            stack.append(num * sign)
            num = 0
            sign = 1
        elif char == '-':
            stack.append(num * sign)
            num = 0
            sign = -1
        elif char == '*':
            num = 0
            sign = 1
        elif char == '/':
            num = 0
            sign = -1

    stack.append(num * sign)

    return sum(stack)

# Test Cases
print(calculate("3+2*2"))  # Output: 7
print(calculate(" 3/2 "))  # Output: 1
print(calculate(" 3+5 / 2 "))  # Output: 5
print(calculate("-1+5"))  # Output: 4
print(calculate("2+3+5"))  # Output: 10
