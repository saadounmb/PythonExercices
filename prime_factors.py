def prime_factors(n):
    # Function to find prime factors of n
    factors = []
    
    # Handle negative numbers
    if n < 0:
        factors.append(-1)
        n = abs(n)
    
    # Edge case for numbers less than 2
    if n < 2:
        return factors
    
    # Find prime factors
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors

# Test the function
number = 12  # You can test with different values, including negative values
print(f"The prime factors of {number} are: {prime_factors(number)}")