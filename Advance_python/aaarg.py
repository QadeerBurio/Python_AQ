import argparse

parser = argparse.ArgumentParser(description="A complex command-line tool.")

# Positional argument
parser.add_argument("filename", help="File to process")

# Optional arguments
parser.add_argument("-n", "--number", type=int, required=True, help="Provide a number")
parser.add_argument("-l", "--list", nargs="+", help="Provide a list of items")
parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

args = parser.parse_args()

print(f"Processing file: {args.filename}")
print(f"Number provided: {args.number}")
if args.list:
    print(f"List items: {args.list}")
if args.verbose:
    print("Verbose mode enabled.")




    
# Feature	Description	Example Usage
# Positional Args	Required arguments	python script.py file.txt
# Optional Args	With default values and optional parameters	--age 25, --name AQ
# Flags	Boolean flags using store_true	--verbose
# Data Types	Specify type (int, float, etc.)	--count 5
# Choices	Restrict values to specific options	--mode auto
# Multiple Values	Accept lists of inputs using nargs	--scores 10 20 30
# Required Args	Make optional args mandatory	--username AQ
# Help Messages	Auto-generated help	--help