from random import randint

random_number = randint(0, 200)
print(random_number)
print()

number = int(input('Угадай какое число я загадал: '))

if number == random_number:
    print('Правильно!')

while number != random_number:
    if number > random_number:
        print('Много!')
        number = int(input('Угадай какое число я загадал: '))

    elif number < random_number:
        print('Мало!')
        number = int(input('Угадай какое число я загадал: '))

if number == random_number:
    print('Правильно!')