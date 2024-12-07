def find_permutations(s):
    """
    Recursive function to find all permutations of a given string.
    :param s: Input string
    :return: Tuple containing the list of permutations and the count
    """
    if len(s) == 1:
        return [s], 1
    
    permutations = []  
    total_count = 0    
    for i, char in enumerate(s):
        # Exclude the current character and find permutations of the remaining string
        remaining = s[:i] + s[i+1:]  # Excludes the current character at index `i`
        # Recursive call to find permutations of the smaller string
        sub_permutations, sub_count = find_permutations(remaining)
        # Add the current character to each permutation of the remaining string
        for perm in sub_permutations:
            permutations.append(char + perm)
        total_count += sub_count
    
    return permutations, total_count

input_string = "abcde"
result, count = find_permutations(input_string)
print("Permutations of '{}':".format(input_string), result)
print("Total number of permutations:", count)
