def describe_number(x):
    match x:
        case 0:
            return "Zero"
        case 1 | 2 | 3:
            return "Small number"
        case _ if x < 0:
            return "Negative number"
        case _:
            return "Some other number"

print(describe_number(int(input("Enter Your Number:"))))  # Output: Small number
# print(describe_number(-5))  # Output: Negative number
