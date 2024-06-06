 # Tuple creation
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 5

# Immutable nature
# Trying to modify an element will raise an error
# my_tuple[0] = 10  # This will raise an error

# Nested tuples
nested_tuple = (1, (2, 3), 4)
print(nested_tuple[1])  # Output: (2, 3)

# Length of tuple
print(len(my_tuple))  # Output: 5

# Tuple unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Tuple repetition
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
