# palindrome.py

import sys

def is_palindrome(s):
    """Check if a string is a palindrome (ignores spaces and case)."""
    s = s.replace(" ", "").lower()
    return s == s[::-1]

if __name__ == "__main__":
    # If a command-line argument is provided, use it
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # Otherwise, prompt the user
        user_input = input("Enter a string: ")

    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is NOT a palindrome.")
