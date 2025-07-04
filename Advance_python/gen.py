def generate_numbers(n):
    for i in range(n):
        yield i

# Using the generator
gen = generate_numbers(5)
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1

for num in gen:
    print(num)  # Output: 0, 1, 2, 3, 4



def fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

# Using the generator
for num in fibonacci(10):
    print(num, end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34
