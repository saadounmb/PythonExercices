def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(e.lower() for e in s if e.isalnum())
    
    # Check if the string equals its reverse
    return s == s[::-1]

# Prompting the user to enter a string
user_input = input("Enter a string: ")

# Checking if the string is a palindrome
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
