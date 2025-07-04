# Exercise: Python Variables


# 1. Create a variable called break and assign it a value 5.
#  See what happens and find out the reason behind the behavior that you see.

# break=5          # SyntaxError: invalid syntax

# In Python, break is also a reserved keyword. Attempting to assign a value to break will result in a syntax error.



# 2. Create two variables. One to store your birth year and another one to store current year.
#  Now calculate your age using these two variables


birth_year=1982
current_year=2019
age=current_year-birth_year
age

# 3. Store your first, middle and last name in three different variables and then print your full name using these variables

first="Dhaval"
middle="Rambhai"
last="Patel"
print("My full name is: " + first + " " + middle + " " + last)

# 4. Answer which of these are invalid variable names:
#  _nation 1record record1 record_one record-one record^one continue

# AND: 1record, record-one, record^one, continue