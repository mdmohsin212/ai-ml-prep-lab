import json

def safe_access(file_path, keys, default=None):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        for key in keys:
            if isinstance(data, dict) and key in data:
                data = data[key]
            else:
                return default
        return data
    
    except FileNotFoundError:
        print("File Not found")
        return default


email = safe_access("./data/info.json", ["personal_life", "contact", "email"])
print(email)


perm_city = safe_access("./data/info.json", ["address", "permanent", "city"], "Not Found")
print("Permanent City:", perm_city)