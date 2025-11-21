
import sys

if len(sys.argv) != 2:
    print("Usage: python palindrome.py <string>")
    sys.exit(1)

s = sys.argv[1]
rev = s[::-1]

if s == rev:
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
