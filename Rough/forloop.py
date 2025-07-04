# store monthly expenses in a list and find out total expenses for all month's

# exp=[2300,2100,2700,2900,3100,1100,]
# # total=exp[0]+exp[1]+exp[2]+exp[3]+exp[4]+exp[5]
#
# total=0
# for item in exp:
#     total=total+item
# print("Total Expenses is : ",total)


# 2nd Code

# colors = ["red", "green", "blue"]
# shapes = ["circle", "square", "triangle"]
#
# for color in colors:
#     for shape in shapes:
#         print(f"{color} {shape}")

#3rd Code
# for i in range(1, 11):
#     print(i)

# While loop
# i = 1
# while i <= 5:
#     print(i)
#     i += 1


# 4th code
# exp=[2300,2100,2700,2900,3100,1100,]
# total=0
# for i in range(len(exp)):
#     print("Month:",(i+1),"Expenses:",exp[i])
#     total=total+exp[i]
#     print("Total Expenses is : ",total)

# 5th Code

# key_locations="chair"
# locations=["Garage","living room","chair","closet"]
# for i in locations:
#     if i==key_locations:
#         print("key is found in:",i)
#         break
#     else:
#         print("key is not found in :",i)

# 6th Code: print square of numbers between 1_5 except even

# for i in range(1,6):
#     if i%2==0:
#         continue
#     print(i*i)


# While loop

# i=int(input("Enter Number:"))
#
# while i<38:
#     i=int(input("Enter Number:"))
#     print(i)
# else:
#     print("I am inside else")
#
#
# print("Done with the loop")


# Break statement

# for i in range(12):
#     print(" 5X:",i+1,"=",5*(i+1))

# # Continue Statement
#
# for i in range(12):
#     if i == 11:
#         print("Skip the iteration")
#         continue
#     print("5X:", i, "=", 5 * i)


# f strings

# letter="my name is {1} and i am from {0}"
# name="Harry"
# country="Pak"
# # print(letter.format(country,name))
# print(f"My name is {name} and i a from {country}")
#
# txt="for only {price:.2f} dollars!"
# print(txt.format(price=49.92999))


# Enumerate function use index with forloop

# code 1:
# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits, start=1):
#     print(f"Index {index}: {fruit}")

# code 2:

a=[3,5,7,8,9,4,2,3,6]

for index, a in enumerate(a,start=1):
    print(index,a)
    if index==3:
        print(index,"AQ")
    elif index==6:
        print(index,"Sami")