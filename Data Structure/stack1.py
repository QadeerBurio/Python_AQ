class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"✅ Pushed {item} to the stack.")

    def pop(self):
        if self.is_empty():
            print("❌ Stack is empty! Cannot pop.")
            return None
        item = self.stack.pop()
        print(f"🗑️ Popped item: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("❌ Stack is empty!")
            return None
        print(f"🔍 Top of stack: {self.stack[-1]}")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        print(f"📦 Stack size: {len(self.stack)}")
        return len(self.stack)

    def display(self):
        if self.is_empty():
            print("📭 Stack is empty.")
        else:
            print("📚 Stack (Top to Bottom):")
            for item in reversed(self.stack):
                print(item)

# ===== Menu-Based Program =====
def main():
    s = Stack()

    while True:
        print("\n--- Stack Operations ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Is Empty?")
        print("5. Size")
        print("6. Display Stack")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            val = input("Enter value to push: ")
            s.push(val)
        elif choice == "2":
            s.pop()
        elif choice == "3":
            s.peek()
        elif choice == "4":
            if s.is_empty():
                print("✅ Yes, the stack is empty.")
            else:
                print("❌ No, the stack is not empty.")
        elif choice == "5":
            s.size()
        elif choice == "6":
            s.display()
        elif choice == "7":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1-7.")

if __name__ == "__main__":
    main()
