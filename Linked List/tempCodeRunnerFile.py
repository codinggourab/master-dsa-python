class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class InsertStart:
    def __init__(self):
        self.head = None
    def addinbw(self,data,key):
        q = Node(data)
        temp = self.head
        while temp:
            if temp.data == key:
                q.next = temp.next
                q.prev = temp
                if temp.next is not None:
                    temp.next.prev = q
                else:
                    self.tail = q
                temp.next = q
                return
            temp = temp.next
