char = input("Enter a character: ").lower()

if char in "aeiou":
    print(f"{char} is a vowel.")
elif char.isalpha():
    print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a letter.")
