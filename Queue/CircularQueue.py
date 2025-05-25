class Node:
    def __init__(self,MAX = 5):
        self.MAX = MAX
        self.q = [None] * MAX
        self.front = -1
        self.rear = -1
        
    def enqueue(self,data):
        
        if (self.rear + 1) % self.MAX == self.front:
            print("Queue is full")
        elif self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
            self.q[self.rear] = data
        else:
            self.rear = (self.rear+1) % self.MAX
            self.q[self.rear] = data
            
    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print("queue is empty")
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.MAX
            
    def display(self):
        if self.front == -1 and self.rear == -1:
            print("queue is empty")
        else:
            i = self.front
            print("Oueue is: ")
            while i != self.rear:
                print(self.q[i], end=" ")
                i = (i + 1) % self.MAX
            print(self.q[self.rear])
            
obj = Node()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(90)
obj.enqueue(16)
obj.enqueue(14)
obj.enqueue(30)
obj.display()
            
        
        