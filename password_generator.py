import random
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 'abcdefghijklmnopqrstuvwxyz'
c = '01234567890123456789'
d = '!@%&!@%&!@%&!@%&!@%&'

all = a + b + c + d
#length = int(input('Введите размер пароля: '))
length = 10

password = "".join(random.sample(all, length))
print(password)