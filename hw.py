result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b

data = {10: 2, 2: 5, 123: 4, 18: 0, 8: 4}

try:
    for key in data:
        res = divider(key, data[kem])
        result.append(res)
except NameError:
    print("'Kem' does not exist, try changing this value to something else")

print(result)

