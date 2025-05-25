class dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def RearEnqueue(self,item):
        self.items.append(item)

    def FrontEnqueue(self,item):
        self.items.insert(0,item)

    def RemoveFront(self):
        return self.items.pop(0)
    
    def RemoveRear(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
d = dequeue()

print(d.isEmpty())
d.RearEnqueue(8)
d.RearEnqueue(5)
d.FrontEnqueue(7)
d.FrontEnqueue(10)
print(d.size())
print(d.isEmpty())
d.RearEnqueue(11)
print(d.RemoveFront())
print(d.RemoveFront())
d.FrontEnqueue(55)
d.RearEnqueue(45)
print(d.items)
