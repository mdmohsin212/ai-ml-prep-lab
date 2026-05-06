s = "swiss"
ans =""
count = {}

for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
        ans=char
    
print(count, ans)