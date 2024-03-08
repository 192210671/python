def is_prime_number(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Sample Function Calls for testing
print(f"is_prime_number(3): {is_prime_number(3)}")  # Expected: True
print(f"is_prime_number(41): {is_prime_number(41)}")  # Expected: True
print(f"is_prime_number(6): {is_prime_number(6)}")  # Expected: False
print(f"is_prime_number(1): {is_prime_number(1)}")  # Expected: False
print(f"is_prime_number(-3): {is_prime_number(-3)}")  # Expected: False
print(f"is_prime_number(1.1): {is_prime_number(1.1)}")  # Expected: False
