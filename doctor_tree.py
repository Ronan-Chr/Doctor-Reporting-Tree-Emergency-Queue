class DoctorNode:
    def __init__(self, name):
        self.name = name #who is the doctor
        self.left = None #left child
        self.right = None #right child

class DoctorTree:
    def __init__(self):
        self.root = None



# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Phan")
print(tree.root.name) # Output: Dr. Phan
print(tree.root.left) # Output: None
print(tree.root.right) # Output: None