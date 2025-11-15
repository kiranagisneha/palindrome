# palindrome.py

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # ignore spaces and case
    return s == s[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string: ")

    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is NOT a palindrome.")
