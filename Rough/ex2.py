# import time
#
# # Optional: If you want to display the current time
# current_time = time.strftime('%H:%M:%S')
# print("Current Time:", current_time)
#
# # Get the hour from user input
# # hour = int(input("Enter The Hour (0-23): "))
# # print("Hour entered:", hour)
#
# # Determine the greeting based on the hour
# if 0 <= hour < 12:
#     print("Good Morning Sir!")
# elif 12 <= hour < 17:
#     print("Good Afternoon Sir!")
# elif 17 <= hour < 24:
#     print("Good Evening Sir!")
# else:
#     print("Invalid hour entered.")  # Handle cases where the input is not in the valid range



    # # formated Time
    # import time
    #
    # formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print("Formatted Time:", formatted_time)


# Code 3
# import time
#
# # Get the current hour
# current_time = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
#
# # Display the current time and hour
# print("Current Time:", current_time)
# print("Hour detected:", hour)
#
# # Determine the greeting based on the hour
# if 0 <= hour < 12:
#     print("Good Morning Sir!")
# elif 12 <= hour < 17:
#     print("Good Afternoon Sir!")
# elif 17 <= hour < 24:
#     print("Good Evening Sir!")
# else:
#     print("Invalid hour detected.")  # This line is just a safeguard; it won't normally be reached.



# Code 4

# import time
# t = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
# # hour = int(input("Enter hour: "))
# # print(hour)
#
# if(hour>=0 and hour<12):
#   print("Good Morning Sir!")
# elif(hour>=12 and hour<17):
#   print("Good Afternoon Sir!")
# elif(hour>=17 and hour<0):
#   print("Good Night Sir!")