def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)


str1 = "listen"
str2 = "silent"


# print(sorted(str1))
# print(sorted(str2))


print(f"Are '{str1}' and '{str2}' anagrams? {are_anagrams(str1, str2)}")
