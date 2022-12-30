words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 
            'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 
            'слова', 'фраза', 'введите', 'слово', 'кнопку',]
palindroms = []
for i in words:
    if i == i[::-1]:
        palindroms.append(i)
        print(f'слово {i} - палиндром')
    else:
        continue
print('Эти слова являются палнидромами')
print(*palindroms)