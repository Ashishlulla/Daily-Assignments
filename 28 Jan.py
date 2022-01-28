# 1. Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}
a = {'c1': 'Red', 'c2': 'Green', 'c3': None}
b = {}
for key, val in a.items():
    if val is not None:
        b[key] = val
    else:
        pass

print(b)

# 2. Write a Python program to filter the height and width of students, which are stored in a dictionary.
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), ,'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg : {'Cierra Vega': (6.2, 70)}


a = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
b = {}
for key, val in a.items():
    if val[0] >= 6 and val[1] >=70:
        b.update({key: val})
        print(f'Height > 6ft and Weight> 70kg: {b}')
    else:
        pass

# 3. Write a Python program to sort a tuple by its float element.
# Sample Data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]


a = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
b = sorted(a, key=lambda x: float(x[1]), reverse=True)
print(b)
