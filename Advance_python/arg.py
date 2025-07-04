import argparse

# Create an argument parser object
parser = argparse.ArgumentParser(description="A simple argument parsing example.")

# Add arguments
parser.add_argument("name", help="Your name")  # Positional argument
parser.add_argument("--age", type=int, help="Your age")  # Optional argument
parser.add_argument("--city", default="Unknown", help="Your city")  # Default value

# Parse the arguments
args = parser.parse_args()

# Access the parsed arguments
print(f"Hello, {args.name}!")
if args.age:
    print(f"You are {args.age} years old.")
print(f"You're from {args.city}.")
