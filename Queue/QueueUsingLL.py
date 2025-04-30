class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print("Enqueued item is:", data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            deq_item = self.front.data
            self.front = self.front.next
            if self.front is None:  # Queue became empty
                self.rear = None
            print("Dequeued item is:", deq_item)

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            current = self.front
            print("Queue elements:")
            while current:
                print(current.data)
                current = current.next

# Menu-driven part
def menu():
    queue = LinkedQueue()
    while True:
        print("\n----- Queue Menu (Linked List) -----")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Check if Queue is Empty")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            data = input("Enter item to enqueue: ")
            queue.enqueue(data)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.display()
        elif choice == '4':
            print("Queue is empty" if queue.is_empty() else "Queue is not empty")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
