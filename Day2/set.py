# Set creation
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Adding elements to a set
set1.add(6)
print(set1)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements from a set
set1.remove(3)
print(set1)  # Output: {1, 2, 4, 5, 6}

# Set union
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 4, 5, 6, 7}

# Set intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {4, 5, 6}

# Set difference
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Set symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 7}

# Set membership test
print(4 in set1)  # Output: True
print(8 in set1)  # Output: False

# Set length
print(len(set1))  # Output: 5

# Set iteration
for element in set1:
    print(element)

# Clearing a set
set1.clear()
print(set1)  # Output: set()
