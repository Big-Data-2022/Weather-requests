cities = []
while True:
    
    text = input(''' Выберите действие:
    1. Добавить новый город
    2. Отобразить список городов
    3. Заменить город
    4. Удалить город
    5. Выход
    >>>  ''')

    if text == '1':
        new_city = input('Введите название города: ')
        if new_city in cities:
            print('Такой город уже есть!')
        elif new_city.isalpha() == False:
            print('Некорректное название!')
        else:
            cities.append(new_city)
            
    elif text == '2':
        for i in cities:
            print(cities.index(i), i)
            
    elif text == '3':
        current_city = input('Текущий город: ')
        replace_city = input('Новый город: ')
        if current_city not in cities:
            print('Текущий город отсутствует')
        elif replace_city in cities:
            print('Такой город уже есть!')
        elif replace_city.isalpha() == False:
            print('Некорректное название!')
        else:
            cities.remove(current_city)
            cities.append(replace_city)
            print('Город заменен.')

    elif text == '4':
        remove_city = input(' Введите название города: ')
        if remove_city not in cities:
            print('Текущий город отсутствует.')
        elif remove_city.isalpha() == False:
            print('Некорректное название!')
        else:
            cities.remove(remove_city)
            print('Город удален!')

    elif text == '5':
        print('Программа завершена!')
        break