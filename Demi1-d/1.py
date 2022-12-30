while True:
    db = open('db.txt', 'a+')
    operator = input('Марсель сделал запрос на: (+ - / * % ): ')
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    if operator == '+':
        result = num1 + num2
        print(f'{num1} + {num2} = {result}')
        db.write(f' \n Пользователь запросил: {num1} + {num2} = {result} ')
    elif operator == '-':
        result = num1 - num2
        print(f'{num1} - {num2} = {result}')
        db.write(f' \n Пользователь запросил: {num1} - {num2} = {result} ')
    elif operator == '/':
        result = num1 / num2
        print(f'{num1} / {num2} = {result}')
        db.write(f' \n Пользователь запросил: {num1} / {num2} = {result} ')
    elif operator == '*':
        result = num1 * num2
        print(f'{num1} * {num2} = {result}')
        db.write(f' \n Пользователь запросил: {num1} * {num2} = {result} ')
    elif operator == '%':
        result = num1 % num2
        print(f'{num1} % {num2} = {result}')
        db.write(f' \n Пользователь запросил: {num1} % {num2} = {result} ')
    else:
        print('error')
        
    cont = input('Would you want to continue? Yes/No ')
    if cont == 'Yes':
        print()
    elif cont == 'No':
        print()
        break
    else:
        print('error')
        break