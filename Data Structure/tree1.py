class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        print("  " * level + f"📁 {self.data}")
        for child in self.children:
            child.print_tree(level + 1)

# Example Usage
if __name__ == "__main__":
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("MacBook"))

    phone = TreeNode("Phone")
    phone.add_child(TreeNode("iPhone"))
    phone.add_child(TreeNode("Samsung"))
    phone.add_child(TreeNode("OnePlus"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)

    root.print_tree()
