def longest_common_prefix(strings):
    if not strings:
        return ""
    
    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix


strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))