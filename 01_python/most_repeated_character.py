def repeated_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    max_char = max(char_count, key=char_count.get)
    return max_char

s = "aabbbcdddde"
print(repeated_character(s))