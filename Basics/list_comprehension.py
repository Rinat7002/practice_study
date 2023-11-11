# newlist = [expression for item in iterable (if condition)]

# iterable - перебираемый источник данных (список, множество, последовательность, функция, напр range)
# item - извлекаемый из источника данных элемент
# condition - (необязательное) условие которому должны соответствовать извлекаемые элементы

# Первое решение
numbers = [-3, -2, -1, 0, 1, 2, 3]
positive_numbers = []
for n in numbers:
    if n > 0:
        positive_numbers.append(n)
print(positive_numbers)  # [1, 2, 3]

# 2 решение с помощью list_comprehension
numbers = [-3, -2, -1, 0, 1, 2, 3]
positive_numbers = [n for n in numbers if n > 0]
print(positive_numbers)  # [1, 2, 3]

# Пример с range
numbers = [n for n in range(10)]
print(numbers)      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Создать из словаря список ключей
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
words = [word for word in dictionary]
print(words)    # ['red', 'blue', 'green']

numbers = [-3, -2, -1, 0, 1, 2, 3]
new_numbers = [n * 2 for n in numbers]
print(new_numbers)      # [-6, -4, -2, 0, 2, 4, 6]

numbers = [-3, -2, -1, 0, 1, 2, 3]
new_numbers = [n * 2 if n > 0 else n for n in numbers]
print(new_numbers)      # [-3, -2, -1, 0, 2, 4, 6]

dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
words = [f"{key}: {dictionary[key]}" for key in dictionary]
print(words)    # ['red: красный', 'blue: синий', 'green: зеленый']

# Выберем только те ключи из словаря, длина которых больше 3:
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
words = [f"{key}: {dictionary[key]}" for key in dictionary if len(key) > 3]
print(words)    # ['blue: синий', 'green: зеленый']