class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"✅ Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("❌ Queue is empty! Cannot dequeue.")
            return None
        item = self.queue.pop(0)
        print(f"🗑️ Dequeued: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("❌ Queue is empty!")
            return None
        print(f"👀 Front of Queue: {self.queue[0]}")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        print(f"📦 Queue size: {len(self.queue)}")
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("📭 Queue is empty.")
        else:
            print("📚 Queue (Front → Rear):", self.queue)
def main():
    q = Queue()
    while True:
        print("\n--- Queue Operations ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Is Empty?")
        print("5. Size")
        print("6. Display Queue")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            val = input("Enter value to enqueue: ")
            q.enqueue(val)
        elif choice == "2":
            q.dequeue()
        elif choice == "3":
            q.peek()
        elif choice == "4":
            print("✅ Yes" if q.is_empty() else "❌ No")
        elif choice == "5":
            q.size()
        elif choice == "6":
            q.display()
        elif choice == "7":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    main()
