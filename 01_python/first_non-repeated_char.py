def non_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char in s:
        if char_count[char] == 1:
            return char


s = "swiss"
print(non_repeated_char(s))