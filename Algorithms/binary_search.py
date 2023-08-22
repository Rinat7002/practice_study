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

number = 1
#print(binary_search(elements, number))

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

number2 = 1
#print(binary_search2(elements, number2))


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# O log2(n)    log2(16) = 4   (для нашего массива макс 4 итерации для поиска)
def binary_search_best(array, item):
    count = 0
    start = 0
    end = len(array)
    middle = 0
    found = False
    position = -1

    while found == False and start <= end:
        count += 1
        middle = (start + end) // 2
        if array[middle] == item:
            found = True
            position = middle
            print("Count : " + str(count))
            return position

        if (item < array[middle]):
            end = middle - 1
        else:
            start = middle + 1


    return position

item = 15
print(binary_search_best(array, item))








