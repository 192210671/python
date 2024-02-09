def generate_parentheses(n):
    def backtrack(s='', l
                  eft=0, right=0):
        if len(s) == 2 * n:
            combinations.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    if n <= 0:
        return []

    combinations = []
    backtrack()
    return combinations


print(generate_parentheses(3)) 
print(generate_parentheses(1))  
print(generate_parentheses(5)) 
print(generate_parentheses(-1))
print(generate_parentheses(0))  
