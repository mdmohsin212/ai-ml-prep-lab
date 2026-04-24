data = [-3, 4, -1, 5, 0, 2]
result_for = []
for x in data:
    if x > 0:
        result_for.append(x ** 2)

def is_positive(x):
    return x > 0

def square(x):
    return x ** 2

filtered_data = filter(is_positive, data)
result_map_filter = list(map(square, filtered_data))

result_lambda = list(map(lambda x: x ** 2, filter(lambda x: x > 0, data)))

result_comp = [x ** 2 for x in data if x > 0]


print("For Loop:", result_for)
print("Map & Filter:", result_map_filter)
print("Lambda Pipeline:", result_lambda)
print("List Comprehension:", result_comp)