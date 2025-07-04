import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4])  # 'i' = type code for integer

print("Original array:", arr)

# Access elements
print("Element at index 2:", arr[2])

# Append a new item
arr.append(5)
print("After appending 5:", arr)

# Insert at index 1
arr.insert(1, 10)
print("After inserting 10 at index 1:", arr)

# Remove an item
arr.remove(3)
print("After removing 3:", arr)

# Loop through the array
print("Final array elements:")
for val in arr:
    print(val)
