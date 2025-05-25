class Node:
    def __init__(self, data,count,max_s):
        self.data = data
        self.next = None
        self.count = 0

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    def is_full(): 
        return self.count >= self.max_size

    def push(self, item,):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        print(f"Pushed item: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
        else:
            popped_item = self.top.data
            self.top = self.top.next
            print(f"Popped item: {popped_item}")

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):")
            current = self.top
            while current:
                print(current.data)
                current = current.next
            print(self.top)

# Menu-driven program
def main():
    stack = Stack()

    while True:
        print("\nMENU")
        print("1. Push an element into the stack")
        print("2. Pop an element from the stack")
        print("3. Display the stack elements")
        print("4. Exit from program")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to push: ")
            stack.push(item)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.display()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the program
main()
