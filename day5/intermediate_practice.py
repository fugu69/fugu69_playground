"""
List comprehensions provide a concise way to create lists. 
Common applications are to make new lists where each element is the result of some operations applied to each member 
of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

The Syntax

newlist = [expression for item in iterable if condition == True]

expression means what to do with an element (leave as is, double * 2, square it ** 2, convert str(item) etc.)

The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits] - replace 'banana' with 'orange'
"""

# Create a list of squares from 1 to 10.

squares = [i**2 for i in range(10)]
print(squares)


"""
Tuple packing/unpacking: Swap two variables without using a temporary variable.
"""

x, y = 5, 10
x, y = y, x

print(x, y)

"""
Dictionary Iterations + Advanced concepts
"""


person = {"name": "Alice", "age": 25, "city": "New York"}

for i in person:
    print (f"The dict key is: {i}, value is: {person[i]}")
    
for key, value in person.items():
    print(f"{person['name']}, lives in {person['city']} and is {person['age']} old.")

print(", ".join([f"{key}: {value}" for key, value in person.items()]))

"""
Filtering Dictionary Data
Syntax is similar to list comprehension but with key: value mapping (expression, iteration, condition)
"""

people = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 22,
    "David": 35,
}

thirty_younger = {name: age for name, age in people.items() if age < 30}
print(thirty_younger)


"""
Nested Dictionary Iteration

.get() method is common and very important. It allows to get access to values in different data stractures
and prevent raising KeyError and others. It is save and convinient way to retrieve data.
"""

data = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 30, "city": "London"},
    "Charlie": {"age": 22, "city": "Paris"}
}

for name, details in data.items():
    city = details.get("city", "Unknown")
    print(f"{name}: {details['age']} years old, from {details['city']}")

"""
Dictionary Comprehension for Data Transformation
"""

prices = {"apple": 2, "banana": 1, "cherry": 3}

discounted_prices = {item: round(price*0.2, 2) for item, price in prices.items() if price >= 1}

print(discounted_prices)
