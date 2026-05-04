import re

def is_palindrome(s):
    s = re.sub(r'[^a-z]', '', s.lower())
    return s == s[::-1]

def filter_palindrome(strings):
    return [s for s in strings if is_palindrome(s)]


words = ["radar", "python", "level", "world"]
print(filter_palindrome(words))