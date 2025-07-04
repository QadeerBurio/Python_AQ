class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(root, key):
            if root is None:
                return Node(key)
            if key < root.key:
                root.left = _insert(root.left, key)
            elif key > root.key:
                root.right = _insert(root.right, key)
            return root
        self.root = _insert(self.root, key)

    def inorder(self):
        def _inorder(root):
            if root:
                _inorder(root.left)
                print(root.key, end=' ')
                _inorder(root.right)
        _inorder(self.root)

    def preorder(self):
        def _preorder(root):
            if root:
                print(root.key, end=' ')
                _preorder(root.left)
                _preorder(root.right)
        _preorder(self.root)

    def postorder(self):
        def _postorder(root):
            if root:
                _postorder(root.left)
                _postorder(root.right)
                print(root.key, end=' ')
        _postorder(self.root)

    def search(self, key):
        def _search(root, key):
            if root is None or root.key == key:
                return root
            if key < root.key:
                return _search(root.left, key)
            return _search(root.right, key)
        return _search(self.root, key)

    def delete(self, key):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(root, key):
            if not root:
                return root
            if key < root.key:
                root.left = _delete(root.left, key)
            elif key > root.key:
                root.right = _delete(root.right, key)
            else:
                # Node with one or no child
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                # Node with two children
                temp = _min_value_node(root.right)
                root.key = temp.key
                root.right = _delete(root.right, temp.key)
            return root

        self.root = _delete(self.root, key)

# -------------------------
# Example usage

bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

print("📘 Inorder Traversal (Sorted):")
bst.inorder()  # 20 30 40 50 60 70 80

print("\n📗 Preorder Traversal:")
bst.preorder()  # 50 30 20 40 70 60 80

print("\n📙 Postorder Traversal:")
bst.postorder()  # 20 40 30 60 80 70 50

print("\n🔍 Search 60:", bst.search(60) is not None)  # True
print("🔍 Search 90:", bst.search(90) is not None)  # False

bst.delete(50)
print("\n🗑️ After deleting 50:")

print("Inorder:")
bst.inorder()  # Should not contain 50

print("\nPreorder:")
bst.preorder()

print("\nPostorder:")
bst.postorder()
