first_names = ["ivan", "maria", "petar"]
sur_names = ["ivanov", "popova", "petrov"]
names = []

for i in range(len(first_names)):
    names.append(f'{first_names[i].capitalize()} {sur_names[i].capitalize()}')

print(names)
