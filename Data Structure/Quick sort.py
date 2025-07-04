def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Already sorted

    pivot = arr[0]  # Choose pivot
    left = [x for x in arr[1:] if x < pivot]       # Smaller values
    right = [x for x in arr[1:] if x >= pivot]     # Larger or equal values

    # Recursively sort left and right
    return quick_sort(left) + [pivot] + quick_sort(right)

# ---------- Main Program ----------
arr = [33, 10, 55, 26, 64, 18]
print("Original List:", arr)

sorted_arr = quick_sort(arr)
print("Sorted List:  ", sorted_arr)
