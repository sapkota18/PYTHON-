list = [18, 45, 7]
print(list)
list.append("hell")  # Adding elements in list
print("List After Adding", list)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # Mearging list2 with list1
print("List after Mearging", list1)


list3 = [100, 200, 300]
list3.remove(200)  # Removing List item 200
print("List After Removing Element", list3)

list4 = [1, 2, 3]
list4.insert(1, 5)  # Inserting Element In list after 1
print("After Insertion", list4)

x = list4.pop(2)
print("Popped Element:", x)  # Poping Element
print("After Poping element", list4)


list4.reverse()  # Reversing List
print("After Reverse:", list4)


list5 = [10, 1, 6, 8, 4, 9, 8, 9, 9]
print("Before Sorting: ", list5)
list5.sort()  # Sorting List
print("After Sortinng: ", list5)
count = list5.count(9)  # Counting List item 9
print("Count of 9 is:", count)
list5.clear()
print("After clearing list",list5)
