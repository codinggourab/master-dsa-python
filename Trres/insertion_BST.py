class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
def insert(root,key):
    if root == None:
        return Node(key)
    if root.data == key:
        return root.data
    
    if root.data < key:
        root.right = insert(root.right,key)
    else:
        root.left = insert(root.left,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
        
r = Node(15)
r = insert(r, 10)
r = insert(r, 18)
r = insert(r, 4)
r = insert(r, 11)
r = insert(r, 16)
r = insert(r, 20)
r = insert(r, 13)

# Print inorder traversal of the BST
inorder(r)