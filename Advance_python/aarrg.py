import argparse

# Create an argument parser object with a description
parser = argparse.ArgumentParser(
    description="A comprehensive example of argparse with various features."
)

# 1. Positional Argument (Mandatory)
parser.add_argument(
    "filename",
    help="Name of the file to be processed (required positional argument)"
)

# 2. Optional Arguments
parser.add_argument(
    "--age",
    type=int,
    help="Your age (optional, expects an integer)"
)

parser.add_argument(
    "--city",
    default="Unknown",
    help="Your city (optional, defaults to 'Unknown')"
)

# 3. Boolean Flag (store_true)
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Enable verbose mode (optional flag, default is False)"
)

# 4. Choice Restriction
parser.add_argument(
    "--mode",
    choices=["auto", "manual", "test"],
    help="Choose a mode: auto, manual, or test"
)

# 5. Required Optional Argument
parser.add_argument(
    "--username",
    required=True,
    help="Your username (this argument is required)"
)

# 6. Multiple Values (nargs)
parser.add_argument(
    "--scores",
    nargs="+",
    type=int,
    help="Enter multiple scores separated by spaces"
)

# 7. Argument with limited values (range validation)
parser.add_argument(
    "--priority",
    type=int,
    choices=range(1, 6),
    help="Set priority (1-5)"
)

# 8. Grouping arguments (better help message organization)
auth_group = parser.add_argument_group("Authentication")
auth_group.add_argument("--user", help="Username for authentication")
auth_group.add_argument("--password", help="Password for authentication")

# 9. Mutually Exclusive Arguments (only one can be used)
exclusive_group = parser.add_mutually_exclusive_group()
exclusive_group.add_argument("--light", action="store_true", help="Enable light mode")
exclusive_group.add_argument("--dark", action="store_true", help="Enable dark mode")

# 10. Version Info
parser.add_argument(
    "--version",
    action="version",
    version="%(prog)s 1.0",
    help="Show the version of the script"
)

# Parse the command-line arguments
args = parser.parse_args()

# Access and process arguments
print(f"Processing file: {args.filename}")

if args.age:
    print(f"Your age: {args.age}")

print(f"City: {args.city}")

if args.verbose:
    print("Verbose mode is enabled.")

if args.mode:
    print(f"Selected mode: {args.mode}")

print(f"Username: {args.username}")

if args.scores:
    print(f"Scores provided: {args.scores}")

if args.priority:
    print(f"Priority level set to: {args.priority}")

if args.user and args.password:
    print("Authentication successful with provided credentials.")
elif args.user or args.password:
    print("Both username and password are required for authentication.")

if args.light:
    print("Light mode activated.")
elif args.dark:
    print("Dark mode activated.")
else:
    print("No display mode selected.")







# run1:Positional Argument (filename)
# Required without any flag.
# python aarrg.py myfile.txt

# run2: Optional Arguments (--age, --city)
# python aarrg.py myfile.txt --age 25 --city London
# Provided with flags, can have defaults.



# data.txt --age 22 --city NewYork --username AQ --scores 90 85 88 --priority 4 --verbose --dark