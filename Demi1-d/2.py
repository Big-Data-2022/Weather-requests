users = []

while True:
    text = int(input('''
            1 >>> Зарегистрироваться
            2 >>> Авторизоваться
            >>> '''))
    if text == 1:   
        login = input('введите свой логин - ')
        pas = input('введите свой пароль - ')
        users.append(login)
        users.append(pas)
    elif text == 2:
                login = input('введите свой логин - ')
                pas = input('введите свой пароль - ')
    if login not in users or pas not in users:
            print('НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ')
            continue
    else:           
            print('ДОБРО ПОЖАЛОВАТЬ')