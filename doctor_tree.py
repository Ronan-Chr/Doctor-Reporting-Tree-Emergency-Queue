class DoctorNode:
    def __init__(self, name):
        self.name = name #who is the doctor
        self.left = None #left child
        self.right = None #right child

class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, employee_name, side, current_node=None):
        # Empty tree
        if self.root is None:
            print("Doctor tree is empty. Please set the root doctor first.")
            return False

        # Start from root if not part of a recursive call
        if current_node is None:
            current_node = self.root

        # find a doctor node with the name of the parent_name
        if current_node.name == parent_name:
            if side == "left" and current_node.left is None:
                current_node.left = DoctorNode(employee_name)
                print(f"✅ {employee_name} added to the LEFT of {parent_name}")
                return True
            elif side == "right" and current_node.right is None:
                current_node.right = DoctorNode(employee_name)
                print(f"✅ {employee_name} added to the RIGHT of {parent_name}")
                return True
            else:
                print(f"❌ {parent_name} already has a {side} report.")
                return False

        if current_node.left:
            if self.insert(parent_name, employee_name, side, current_node.left):
                return True

        if current_node.right:
            if self.insert(parent_name, employee_name, side, current_node.right):
                return True

        return False  # parent_name not found in the tree

    #Define preorder traversal method
    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    #Define inorder traversal method
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    #Define postorder traversal method
    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Phan")
print(tree.root.name) # Output: Dr. Phan
print(tree.root.left) # Output: None
print(tree.root.right) # Output: None

# Step 3 tests
tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")

tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Morgan", "right")

print(tree.root.left.name)        # Dr. Phan
print(tree.root.left.right.name)  # Dr. Morgan
print(tree.preorder(tree.root))   # ['Dr. Croft', 'Dr. Phan', 'Dr. Morgan']
print(tree.inorder(tree.root))    # ['Dr. Phan', 'Dr. Morgan', 'Dr. Croft']
print(tree.postorder(tree.root))  # ['Dr.Morgan', 'Dr. Phan ', 'Dr. Croft']
