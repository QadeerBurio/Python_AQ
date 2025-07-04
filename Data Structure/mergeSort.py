def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Step 1: Split the array
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Step 2: Merge sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Step 3: Compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Step 4: Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# -------- Main Code ----------
arr = [12, 4, 7, 9, 2, 5]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:  ", sorted_arr)
