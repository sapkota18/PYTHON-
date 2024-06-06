# Dictionary creation
person = {"name": "John", "age": 30, "city": "New York"}

# Accessing values using keys
print(person["name"])  # Output: John
print(person["age"])   # Output: 30
print(person["city"])  # Output: New York

# Adding a new key-value pair
person["job"] = "Engineer"
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# Modifying the value of an existing key
person["age"] = 35
print(person)  # Output: {'name': 'John', 'age': 35, 'city': 'New York', 'job': 'Engineer'}

# Removing a key-value pair
del person["city"]
print(person)  # Output: {'name': 'John', 'age': 35, 'job': 'Engineer'}

# Checking if a key exists
print("name" in person)  # Output: True
print("city" in person)  # Output: False

# Iterating over keys
for key in person:
    print(key, "=", person[key])

# Iterating over key-value pairs
for key, value in person.items():
    print(key, "=", value)

# Length of the dictionary
print(len(person))  # Output: 3

# person = {"name": "John", "age": 30, "city": "New York"}
# print('Keys:',person.keys())
# print('Values:',person.values())
# print('items:',person.items())
# print('Name:',person.get('name'))
# person.pop('age')
# print("After Poping:",person)
