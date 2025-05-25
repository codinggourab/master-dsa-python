class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class CircularLL:
    def __init__(self):
        self.head = None
        
    def create(self,data):
        q = Node(data)
        if self.head == None:
            self.head = q 
            q.next = self.head   
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = q
            q.next = self.head
                
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
            if curr == self.head:
                break
        print("none")
        
clist = CircularLL()
clist.create(10)
clist.create(30)
clist.create(70)
clist.create(80)
clist.create(40)

clist.display()