# Prompt user for a list of integers
numbers = list(map(int, input("Enter a list of integers separated by space: ").split()))

# Append an element
numbers.append(100)
print(f"After appending 100: {numbers}")

# Insert an element at index 1
numbers.insert(1, 50)
print(f"After inserting 50 at index 1: {numbers}")

# Remove an element (if exists)
if numbers:
    numbers.remove(numbers[0])
print(f"After removing the first element: {numbers}")
