def letter_combinations(digits):
    if not digits:
        return []

    digit_mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return

        current_digit = digits[index]
        for letter in digit_mapping[current_digit]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])

    return combinations


print(letter_combinations("23"))  
print(letter_combinations(""))    
print(letter_combinations("2"))   
print(letter_combinations("9"))   
print(letter_combinations("87"))  

