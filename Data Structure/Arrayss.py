# Using a list as an array
numbers = [10, 20, 30, 40]

print("Original array:", numbers)

# Accessing elements by index
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Adding a new element at the end
numbers.append(50)
print("After appending 50:", numbers)

# Changing value at index 1
numbers[1] = 25
print("After changing index 1 to 25:", numbers)

# Looping through array
print("All elements:")
for num in numbers:
    print(num)
