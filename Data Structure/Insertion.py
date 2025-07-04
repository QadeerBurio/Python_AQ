def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current value to insert
        j = i - 1
        # Move elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert key at correct position
        arr[j + 1] = key
arr = [8, 4, 1, 5, 9, 2]
print("Original:", arr)

insertion_sort(arr)
print("Sorted:  ", arr)
