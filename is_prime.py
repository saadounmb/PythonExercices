def is_prime(num):
    # Check if the number is less than or equal to 1
    if num <= 1:
        return False
    
    # Check for factors from 2 to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number to check if it's prime: "))
    
    # Check if the number is prime and print the result
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

# Call the main function to execute the program
main()
