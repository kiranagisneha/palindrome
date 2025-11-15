# pal.py

import sys

def is_palindrome(s):
    """Check if a string is a palindrome (ignores spaces and case)."""
    s = s.replace(" ", "").lower()
    return s == s[::-1]

if __name__ == "__main__":
    # Default string if no input is provided
    default_string = "madam"

    # Check if a string parameter is passed via command-line
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # Use default string if no parameter provided
        user_input = default_string
        print(f"No input parameter provided. Using default string: '{user_input}'")

    # Check palindrome
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is NOT a palindrome.")
