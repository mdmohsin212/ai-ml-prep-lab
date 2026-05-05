import string

def check_all_alphabet(s):
    alphabet = set(string.ascii_lowercase)
    return set(s.lower()) >= alphabet

s = "The quick brown fox jumps over the lazy dog"
print(check_all_alphabet(s))