class Person:
	def __init__(self, name, age):
		self.name = name
		self.__age = age

	def __str__(self):
		return f"name = {self.name}; __age = {self.__age}"

maria = Person("Maria Popova", 25)

# let's try to change Maria's age:
maria.__age = 100
print("maria.__age is set to ", maria.__age)
print(maria)

# # but __age is not hidden! Look:
maria._Person__age = 100
print("maria.__age is set to ", maria.__age)
print(maria)