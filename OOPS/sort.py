array = [4, 5, 6, 7, 8, 9, 9, 6,0]

def find_smallest_and_largest(array):
   
    smallest = array[0]
    largest = array[0]
    
    for num in array:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    
    return smallest, largest


smallest, largest = find_smallest_and_largest(array)
print("Smallest element:", smallest)
print("Largest element:", largest)

array2 = [4, 5, 6, 7, 8, 9, 5, 4]
def sort_array(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
sorted_array = sort_array(array2)
print(sorted_array)
