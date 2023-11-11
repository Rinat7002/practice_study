from random import randint

def start():
    random_number = str(randint(1, 3))

    dicti = {
        '1': 'Камень',
        '2': 'Ножницы',
        '3': 'Бумага'
    }
    hod_comp = dicti.get(random_number)
    print(hod_comp)

    hod = input('Ваш ход су-е-фа: ')

    if hod == hod_comp:
        print('Ничья')

    elif hod == 'Камень' and hod_comp == 'Ножницы':
        print('Человек победил!')

    elif hod == 'Камень' and hod_comp == 'Бумага':
        print('Компьютер победил!')

    elif hod == 'Ножницы' and hod_comp == 'Бумага':
        print('Человек победил!')

    elif hod == 'Ножницы' and hod_comp == 'Камень':
        print('Компьютер победил!')

    elif hod == 'Бумага' and hod_comp == 'Камень':
        print('Человек победил!')

    elif hod == 'Бумага' and hod_comp == 'Ножницы':
        print('Компьютер победил!')

while True:
    start()