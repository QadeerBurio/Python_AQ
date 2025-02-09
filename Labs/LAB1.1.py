# Prompt user for a string
string = input("Enter a string: ")

# Perform string operations
print(f"Concatenation: {string + ' concatenated'}")
print(f"Repetition: {string * 3}")  # Repeat string 3 times
print(f"Indexing (first character): {string[0] if len(string) > 0 else 'Empty string'}")
