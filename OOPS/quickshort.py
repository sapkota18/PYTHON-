def quick_sort(arr):
    """
    Implements the Quick Sort algorithm.
    :param arr: List of elements to be sorted
    :return: Sorted list
    """
    if len(arr)<=1:
        return arr
    
    pivot=arr[-1]
    
    less_than_pivot=[x for x in arr[:-1] if x<=pivot]
    greater_than_pivot=[x for x in arr[:-1] if x>pivot]
    return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)


arr = [3, 6, 8,16,0, 10, 1, 2, 1,-3]
sorted_arr = quick_sort(arr)
print("Original array:", arr)
print("Sorted array:", sorted_arr)

    