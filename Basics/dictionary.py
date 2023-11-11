users = {
         1: "Tom",
         2: "Bob",
         3: "Bill"
         }

print(users[1]) # get value
users[1] = "Rinat" # change value
print(users.get(4, "nothing to get")) # get, but if not, return nothing
del users[2] # delete element by key
print(users)

key = 3
user = users.pop(key) # pop - delete and return element
print("Pop value: " + str(user))    # Bill

# delete all elements
# users.clear()

# copy dictionary
users2 = users.copy()
print("It's copy: " + str(users2))

# update ( merge/join/combine 2 dicts)
users3 = {4 : "Andy", 5: "Julia"}

users2.update(users3)
print("Merged 2 dicts (into Users2 merged users3): " + str(users2))

'''
 Но если необходимо, чтобы оба исходных словаря были без изменений, 
 а результатом объединения был какой-то третий словарь, 
 то можно предварительно скопировать один словарь в другой:
'''

users5 = users.copy()
users5.update(users2)

print("Users5: " + str(users5))
print("------------------------------------")

# Перебор словаря
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users:
    print(f"Phone: {key}  User: {users[key]} ")

print("#######################################")
# 2 способ
for key, value in users.items():
    print(f"Phone: {key}  User: {value} ")

print("#######################################")
# 3 способ (ключи вывести)
for key in users.keys():
    print(key)

print("#######################################")
# 4 способ (значения вывести)
for value in users.values():
    print(value)


# Вложненые словари

users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}

old_email = users["Tom"]["email"]
print("Old email(Tom/Email): " + str(old_email))
