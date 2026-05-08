def is_isogram(word):
    word = word.lower()
    return len(word) == len(set(word))

word = "background"
print(is_isogram(word))