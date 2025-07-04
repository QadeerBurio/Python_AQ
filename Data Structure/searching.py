def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found at index i
    return -1  # Not found

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Found at mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Not found


# ----------- Main Program ------------

# Input list from user
arr = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter the number to search: "))

# Linear Search
print("\n🔍 Linear Search:")
ls_result = linear_search(arr, target)
if ls_result != -1:
    print(f"✅ Found at index {ls_result}")
else:
    print("❌ Not found")

# Binary Search requires sorted array
sorted_arr = sorted(arr)
print("\n🔍 Binary Search (on sorted list):", sorted_arr)
bs_result = binary_search(sorted_arr, target)
if bs_result != -1:
    print(f"✅ Found at index {bs_result} (in sorted list)")
else:
    print("❌ Not found in sorted list")
