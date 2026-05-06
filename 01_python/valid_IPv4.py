def valid_ipv4(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    
    for item in parts:
        num = int(item)
        if not item.isdigit():
            return False
        
        if num < 0 or num > 255:
            return False
        
    return True

address = "192.168.1.1"
print(valid_ipv4(address)) 