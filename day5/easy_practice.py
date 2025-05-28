print("Lists\n")
print("A list is an ordered, mutable collection")
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.remove('apple')
fruits[1] = 'grape'
print(fruits)
print("\n")
########################################
print("\n")
print("Tuples")
print("A tuple is an ordered, immutable collection")
coordinates = (10, 20, 30)
a, b, c = coordinates
print(a, b, c)
print("\n")
########################################
print("\n")
print("Sets")
print("A set is an unordered collection with unique elements")
colors = {'red', 'violet', 'green'}
cars = {'violet', 'black', 'pink', 'red'}
colors.add('yellow')
colors.discard('green')
print(cars.intersection(colors))
print("\n")
########################################
print("\n")
print("Dictionaries")
print("Dictionaries store key-value pairs")
person = {'name': 'Alice', 'age': 25}
print(person['name'])
person['city'] = 'New-York'
person['age'] = 30
print(person)
