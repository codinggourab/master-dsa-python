MAX = 5
arr = [0] * MAX
front = 0
rear = -1
itemcount = 0

def isEmpty():
    return itemcount == 0

def peek():
    return arr[front]

def isFull():
    return rear == MAX-1

def size():
    return itemcount

def insert(data):
    global rear, itemcount
    if not isFull():
        rear += 1
        arr[rear] = data
        itemcount += 1
      
def remove():
    data = arr[front+1]
    if front == MAX:
        front = 0
    itemcount-1
    return data

insert(5)
insert(9)
insert(6)
insert(1)
insert(4)
insert(2)

for i in range(MAX):
    print(arr[i],end=" ")
print()
        