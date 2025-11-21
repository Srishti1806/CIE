import sys
original = sys.argv[1]
rev = original[::-1]
if original == rev:
    print("The given string is palindrome.")
else:
    print("The given string is not palindrome.")
