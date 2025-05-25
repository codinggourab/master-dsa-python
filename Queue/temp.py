class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def isEmpty(self):
        return self.front is None
    def enqueue(self,data):
        newNode = Node(data)
        if self.front is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        print("Queed item is: ",data)
        
    def deque(self):
        if self.front is None:
            print("Queue is empty")
        else:
            deq = self.front.data
            self.front = self.rear.next
            if self.front is None:
                self.rear = None
            print("Deque item is : ",deq)
            
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            current = self.front
            while current:
                print(current.data, end=" ")
                current = current.next


obj = QueueLL()

obj.enqueue(20)
obj.enqueue(90)
obj.enqueue(30)
obj.enqueue(50)
obj.enqueue(10)
obj.display()  