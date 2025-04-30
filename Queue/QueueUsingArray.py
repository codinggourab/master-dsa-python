def create():
    return []

def is_empty(queue):
    return len(queue) == 0

def enqueue(queue, data):
    queue.append(data)
    print("Enqueued item is:", data)

def dequeue(queue):
    if is_empty(queue):
        print("Queue is empty")
    else:
        deq_item = queue.pop(0)
        print("Dequeued item is:", deq_item)

def display(queue):
    if is_empty(queue):
        print("Queue is empty.")
    else:
        print("Queue elements:")
        for item in queue:
            print(item)


def menu():
    queue = create()
    while True:
        print("\n----- Queue Menu -----")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Check if Queue is Empty")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            data = input("Enter item to enqueue: ")
            enqueue(queue, data)
        elif choice == '2':
            dequeue(queue)
        elif choice == '3':
            display(queue)
        elif choice == '4':
            print("Queue is empty" if is_empty(queue) else "Queue is not empty")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


menu()
