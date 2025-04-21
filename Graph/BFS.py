from collections import deque
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def BFS(root):
    if root is None:
        return
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
root = TreeNode(8)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

BFS(root)
            
