dict1 = {'a': 5, 'b': 3, 'c': 10, 'd': 15, 'e': 20, 'f':30, 'g': 42, 'h': 50}

for key in dict1:
    if dict1[key] % 3 == 0 and dict1[key] % 5 == 0:
        print(f'{key} - Hi-Bye')
    elif dict1[key] % 5 == 0:
        print(f'{key} - Bye')
    elif dict1[key] % 3 == 0:
        print(f'{key} - Hi')
    else:
        continue