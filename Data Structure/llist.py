# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Go to the last node
                current = current.next
            current.next = new_node

    # Insert at specific index
    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:  # Insert at head
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        if current is None:
            print("Index out of bounds")
            return
        new_node.next = current.next
        current.next = new_node

    # Delete node by value
    def delete(self, value):
        current = self.head
        if not current:
            print("List is empty")
            return
        if current.data == value:
            self.head = current.next
            return
        while current.next and current.next.data != value:
            current = current.next
        if current.next is None:
            print(f"Value {value} not found.")
            return
        current.next = current.next.next

    # Count number of nodes
    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Display all nodes
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()

print("Count:", ll.count())

ll.insert(1, 15)  # Insert 15 at index 1
ll.display()

ll.delete(20)     # Delete value 20
ll.display()

print("Final count:", ll.count())
