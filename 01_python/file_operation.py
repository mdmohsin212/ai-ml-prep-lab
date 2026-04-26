path = "./data/data.txt"

with open(path, "r", encoding="utf-8") as f:
    print(f.read())


with open(path, "a+", encoding="utf-8") as f:
    f.write("\nHi, This is new line")
    f.close()
    
    
with open(path, "r", encoding="utf-8") as f:
    print(f.read())