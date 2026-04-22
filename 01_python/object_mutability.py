def modify_data(list_items, strings):
    list_items.append(99)
    strings = strings + " World"
    
    print("Inside Function - List:", list_items)
    print("Inside Function - String:", strings)
    print("-" * 20)
    

original_list = [1, 2, 3]
original_string = "Hello"
modify_data(original_list, original_string)

print("Outside Function - List:", original_list)
print("Outside Function - String:", original_string)