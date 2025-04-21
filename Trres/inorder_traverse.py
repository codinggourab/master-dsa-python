class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data,end=" ")
    inorder(node.right)
    
    
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(8)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(9)
root.right.right.right = Node(10)

print("Inorder traversal is: ")
inorder(root)
        