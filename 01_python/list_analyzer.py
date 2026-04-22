def list_analyze(items : list):
    unique = set(items)
    sorted_unique = sorted(unique)
    
    freq_list = {item : items.count(item) for item in unique}
    
    return unique, sorted_unique, freq_list

a = [5, 4, 5, 2, 2, 1]
u, s, f = list_analyze(a)

print("Set:", u)
print("Sorted:", s)
print("Frequency:", f)