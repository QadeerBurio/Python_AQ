# Code 1
expenses = [2200, 2350, 2600, 2130, 2190]

# 1. Feb extra
print("1. Extra spent in Feb over Jan:", expenses[1] - expenses[0])

# 2. Total expense in Q1
print("2. Total expense in first quarter:", sum(expenses[0:3]))

# 3. Check for exact $2000
print("3. Did I spend exactly $2000 in any month?", 2000 in expenses)

# 4. Add June
expenses.append(1980)
print("4. Expense list after adding June:", expenses)

# 5. Refund in April
expenses[3] = expenses[3] - 200
print("5. Expense list after $200 refund in April:", expenses)


# Code 2
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print("1. Length of list:", len(heros))

heros.append('black panther')
print("2. After appending:", heros)

heros.remove('black panther')
heros.insert(heros.index('hulk') + 1, 'black panther')
print("3. After inserting after hulk:", heros)

heros[1:3] = ['doctor strange']
print("4. After replacing thor & hulk with doctor strange:", heros)

heros.sort()
print("5. Sorted list:", heros)

# code3
# Take max number input from the user
max_num = int(input("Enter the maximum number: "))

# Generate list of odd numbers using list comprehension
odd_numbers = [num for num in range(1, max_num + 1) if num % 2 != 0]

# Print the result
print("Odd numbers from 1 to", max_num, "are:", odd_numbers)
