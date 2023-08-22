elements = [1, 4, 6, 3, 7, 8, 0, 2, - 1, -5, 1000, -1000]

def bubble_sort(elements):
    for i in range(0, len(elements)):
        for j in range(i+1, len(elements)):
            if elements[i] > elements[j] and i != j:
                medium = elements[i]
                elements[i] = elements[j]
                elements[j] = medium


    return elements


print(bubble_sort(elements))