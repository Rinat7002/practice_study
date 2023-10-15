users = {
         1: "Tom",
         2: "Bob",
         3: "Bill"
         }

print(users[1]) # get value
users[1] = "Rinat" # change value
print(users.get(4, "nothing")) #get, but if not, return nothing
del users[2] # delete element by key
print(users)