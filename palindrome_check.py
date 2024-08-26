def is_palindrome(s):
    # Initialize an empty stack
    stack = []
    
    # Push each character of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Iterate through the string while compairing each character
    for char in s:
        # Pop the top character from the stack
        top_char = stack.pop()
        
        # Compare the popped character with the current character in the string. If they don't match, the string is not a palindrome
        if char != top_char:
            return False
    
    # If all characters matched, the string is a palindrome
    return True

# Test the function with different strings
if __name__ == "__main__":
    # List of test strings
    test_strings = ["radar", "hello", "level", "world", "madam"]

    # Iterate through each test string and check if it is a palindrome
    for string in test_strings:
        result = "is" if is_palindrome(string) else "is not"
        
        # Print the result
        print(f"'{string}' {result} a palindrome.")
