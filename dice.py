from random import randint

def still():
    still = input('Чтобы сыграть еще, введите "y" : ')
    if still == 'y':
        run_game()
    else:
        return

def roll_dice():
    result = randint(1, 6)
    return result

def run_game():
    first = roll_dice()
    second = roll_dice()
    print('First: ' + str(first) + '\nSecond(you): ' + str(second))
    if first > second:
        print('Вы проиграли =(')
        still()

    elif second > first:
        print('Вы выиграли! =)')
        still()
    else:
        print('Ничья')
        still()

run_game()
