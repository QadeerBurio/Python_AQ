class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Create list from Python list
    def insert_values(self, data_list):
        self.head = None  # Clear existing list
        for data in data_list:
            self.append(data)

    # Append at end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Print all elements
    def print(self):
        current = self.head
        llstr = ""
        while current:
            llstr += str(current.data) + " → "
            current = current.next
        print(llstr + "None")

    # Insert after a specific value
    def insert_after_value(self, data_after, data_to_insert):
        current = self.head
        while current:
            if current.data == data_after:
                new_node = Node(data_to_insert)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Value {data_after} not found in the list.")

    # Remove node by value
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print(f"Value {data} not found in the list.")

# ====== Testing the code with your instructions ======
ll = LinkedList()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print()

ll.insert_after_value("mango", "apple")  # insert apple after mango
ll.print()

ll.remove_by_value("orange")  # remove orange
ll.print()

ll.remove_by_value("figs")  # not in list
ll.print()

ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()  # Should print: None
