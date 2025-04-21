
class Graph:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def DFS(node):
    if node is None:
        return
    print(node.value,end=" ")
    DFS(node.left)
    DFS(node.right)


# 🏗 Building a bigger Graph:
#            1
#         /     \
#       2         3
#     /   \      /  \
#    4     5    6    7
#   / \   /
#  8   9 10
            
root = Graph(1)
root.left = Graph(2)
root.right = Graph(3)

root.left.left = Graph(4)
root.left.right = Graph(5)

root.right.left = Graph(6)
root.right.right = Graph(7)

root.left.left.left = Graph(8)
root.left.left.right = Graph(9)
root.left.right.left = Graph(10)

DFS(root)
            
