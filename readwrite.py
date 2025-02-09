
# # Read
# file = open('write.txt', 'r')
# content = file.read()
# print(content)
# file.close()


# read line by line:

# file = open('write.txt', 'r')
# for line in file:
#     print(line.strip())  # strip() removes the newline character
# file.close()

# # Word count write, read another file:
# file = open('write.txt', 'r')
# files=open('writes.txt','w')
# for line in file:
#     token=line.split(" ")
#     files.write("wordcount: "+str(len(token))+" "+line)
#     # print(len(token),token)  # strip() removes the newline character
#
# file.close()
# files.close()


# read lines into list:

# file = open('data.json', 'r')
# lines = file.readlines()
# print(lines)
# file.close()


#  Write in the file if you create new file you write only name:
# To write data to a file, open it in write ('w'), append ('a'), or read/write ('r+') mode.


# file = open('write.txt', 'w')
# file.write('Hello, World!\n')
# file.write('This is a new line.')
# file.close()

#  Append in file if you write new text in already file created:

# file = open('filename.txt', 'a')
# file.write('\nThis line is added to the file.')
# file.close()

# Reading--> using with statement without closing close():
# with open('filename.txt', 'r') as file:
#     content = file.read()
#     print(content.strip())


# # Writing--> using with statement without closing close():

# with open('filenamee.txt', 'w') as file:
#     file.write('Hello, World!\n')
#     file.write('This is a new line.')


# # Appending--> using with statement without closing close():

# with open('filenamee.txt', 'a') as file:
#     file.write('\nThis line is added to the file.')

# with open('images (3).jpeg', 'wb') as file:
#     file.write(data)  # where 'data' is the binary data you want to write

# with open('images (3).jpeg', 'rb') as file:
#     data = file.read()
#     print(data)






# # File I/O with code:


# Reading
# file=open('data.txt', 'r')
# content=file.read()
# print(content)
# file.close()

# # Writing
# file=open('DataV.txt','w')
# file.write("Data Is Visible!")



#
# # Using a context manager to open the file
# with open("DataV.txt", 'r') as f:
#     for line in f:
#         print(line)  # Directly print each line






# # Open the file in read mode
# f = open('DataV.txt', 'r')
#
# i = 0  # Initialize a counter for the students
#
# while True:
#     i += 1  # Increment the student count
#     line = f.readline()  # Read the next line from the file
#
#     if not line:
#         break  # Exit the loop if the end of the file is reached
#
#     # Remove any extra whitespace (like newline characters) and split by comma
#     parts = line.strip().split(",")
#
#     # Check if there are exactly three parts in the line
#     if len(parts) != 3:
#         print(f"Error: Line {i} does not contain exactly three values: {line}")
#         continue  # Skip to the next iteration if line format is incorrect
#
#     try:
#         # Convert each part to an integer
#         m1 = int(parts[0])
#         m2 = int(parts[1])
#         m3 = int(parts[2])
#     except ValueError:
#         print(f"Error: Non-integer value found in line {i}: {line}")
#         continue  # Skip to the next iteration if conversion fails
#
#     # Print the multiplied marks for each subject
#     print(f"Marks of student {i} in Maths is: {m1 * 2}")
#     print(f"Marks of student {i} in English is: {m2 * 2}")
#     print(f"Marks of student {i} in SST is: {m3 * 2}")
#
#     # Print the original line (optional)
#     print(line.strip())
#
# # Close the file after reading
# f.close()



# Seek(), tell() functions in r/w :

# with open('DataV.txt','r') as f:
#     print(type(f))
#
#     f.seek(10)
#
#     print(type(f.tell()))
#     print(f.tell())
#     data=f.read(5)
#     print(data)






file = open('my.txt', 'r+')

# Read the first 5 characters
print(file.read(5))  # Output: (First 5 characters of the file)

# Show current position
print(file.tell())  # Output: 5

# Move back to the beginning
file.seek(0)

# Read the next 5 characters
print(file.read(10))  # Output: (First 5 characters of the file again)

# Move pointer to end of the file
file.seek(0, 2)
print(file.tell())  # Output: (Size of the file in bytes)

file.close()

