with open("data.txt", "r", encoding='utf-8') as f:
    all_data = f.read()
    print("Total Word :", len(all_data.split()))


total_word = 0
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        words = line.strip()
        total_word += len(words)
    print("Total Word :", len(all_data.split()))