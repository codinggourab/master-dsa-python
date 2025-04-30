class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head=None
    def create(self,data):
        q = Node(data)
        
        if self.head == None:
            self.head = q
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = q
            
    def findMiddle(self):
        slow = self.head
        fast = self.head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        if slow:
            print("Middle element is: ",slow.data)

            
    def reverse_ll(self):
        temp  = self.head
        prev = None
        
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        self.head = prev
            
            
    def display(self):
        if self.head is None:
            print("Lisyt is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,end="->")
                temp = temp.next
            print("None")
            
            
obj = Linkedlist()
obj.create(10)    
obj.create(60)    
obj.create(40)    
obj.create(80)    
obj.create(20)    

obj.display()

obj.findMiddle()

obj.reverse_ll()
obj.display()
  
  