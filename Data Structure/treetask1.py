class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, mode="both", level=0):
        if mode == "name":
            data = self.name
        elif mode == "designation":
            data = self.designation
        else:  # both
            data = f"{self.name} ({self.designation})"

        print("  " * level + "📁 " + data)
        for child in self.children:
            child.print_tree(mode, level + 1)
def build_management_tree():
    # CEO
    ceo = TreeNode("Naveed", "CEO")

    # CTO hierarchy
    cto = TreeNode("Iqbal", "CTO")
    infra_head = TreeNode("Ali", "Infrastructure Head")
    infra_head.add_child(TreeNode("Asim", "Cloud Manager"))
    infra_head.add_child(TreeNode("Nida", "App Manager"))

    app_head = TreeNode("Hira", "Application Head")
    cto.add_child(infra_head)
    cto.add_child(app_head)

    # HR hierarchy
    hr_head = TreeNode("Sarah", "HR Head")
    hr_head.add_child(TreeNode("Ahsan", "Recruiter"))

    # Add to CEO
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()

    print("\n🔹 Name Tree:")
    root_node.print_tree("name")

    print("\n🔹 Designation Tree:")
    root_node.print_tree("designation")

    print("\n🔹 Name + Designation Tree:")
    root_node.print_tree("both")






# COde 2
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(3)