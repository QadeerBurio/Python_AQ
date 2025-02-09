import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple calculator to perform operations on two numbers.")

    parser.add_argument("number1", type=float, help="First number")
    parser.add_argument("number2", type=float, help="Second number")
    parser.add_argument("operation", type=str, choices=["add", "subtract", "multiply"],
                        help="Operation to perform (add, subtract, multiply)")

    args = parser.parse_args()

    if args.operation == "add":
        result = args.number1 + args.number2
    elif args.operation == "subtract":
        result = args.number1 - args.number2
    elif args.operation == "multiply":
        result = args.number1 * args.number2
    else:
        result = "Invalid operation"

    print(f"Result: {result}")
