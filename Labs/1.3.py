import math

# Prompt user for a number
num = float(input("Enter a number: "))

# Perform mathematical operations
print(f"Square Root: {math.sqrt(num)}")
print(f"Power (raised to 3): {math.pow(num, 3)}")
print(f"Sine: {math.sin(math.radians(num))}")  # Convert degrees to radians
print(f"Cosine: {math.cos(math.radians(num))}")
print(f"Logarithm (base 10): {math.log10(num) if num > 0 else 'Undefined for non-positive numbers'}")
