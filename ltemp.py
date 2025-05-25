from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def BFS(root):
    if root is None:
        return
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.data,end=" ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
root = Node(8)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

BFS(root)
