class queueUSingStack:
    def __init__(self):
        self.stack1= []
        self.stack2= []
        
    def enqueue(self,data):
        self.stack1.append(data)
    def dequeu(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
                
        if not self.stack2:
            return "Queue is empty"
        return self.stack2.pop()
    def display(self):
        temp = self.stack2[::-1] + self.stack1
        if not temp:
            print("Queue is empty")
        else:
            print("Front ->", ' -> '.join(map(str, temp)))
            
q = queueUSingStack()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()        # Front -> 10 -> 20 -> 30

print("Dequeued:", q.dequeu())  # 10
q.display()        # Front -> 20 -> 30

q.enqueue(40)
q.display()        # Front -> 20 -> 30 -> 40
