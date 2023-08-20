elements = [1, 4, 6, 3, 7, 8, 0, 2]

#first vatiant
def binary_search(elements, number):
    elements2 = sorted(elements)
    l, r = 0, len(elements2)
    m = 0
    while l < r:
        m = (l + r) // 2

        if elements2[m] == number:
            return number

        elif elements2[m] < number:
            l = m + 1
        else:  # elements2[m] > number
            r = m
    return 'Нету'


#second variant
def binary_search2(elements, number2):
    elements2 = sorted(elements)
    l, r = 0, len(elements2) - 1
    m = 0
    while l <= r:
        m = (l + r) // 2

        if elements2[m] == number2:
            return number2

        elif elements2[m] < number2:
            l = m + 1
        else:  # elements2[m] > number
            r = m - 1
    return 'Нету'


number = 1
print(binary_search(elements, number))


number2 = 1
print(binary_search2(elements, number2))
