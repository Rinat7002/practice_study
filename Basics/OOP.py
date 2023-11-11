# class Person:
#     type = "Person"
#     description = "Describes a person"
#
#     default_name = "Undefined"
#
#     def __init__(self, name):
#         if name:
#             self.name = name
#         else:
#             self.name = Person.default_name
#
#
# print(Person.type)
# print(Person.description)
#
# Person.type = "Class Person"
# print(Person.type)  # Class Person
#
# Tom = Person("Tom")
# Bob = Person("Bob")
# print(Tom.type)
# print(Bob.type)
#
# Person.type = "Class Person"
# print(Tom.type)
#
# Vasya = Person("Vasya")
# Andy = Person("")
# print(Vasya.name)  # Vasya
# print(Andy.name)  # Undefined

# ---------------------------------------#
class Person:
    name = "Undefined"
    def print_name(self):
        print(self.name)

tom = Person()
bob = Person()
tom.print_name()
bob.print_name()

bob.name = "Bob"
bob.print_name()










