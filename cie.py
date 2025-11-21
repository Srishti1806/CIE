import sys
if len(sys.argv) != 2:
    sys.exit(1)
original = sys.argv[1]
rev = original[::-1]
if original == rev:
    print("The given string is palindrome.")
else:
    print("The given string is not palindrome.")
