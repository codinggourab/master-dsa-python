def Create_Stack():
    stack = []
    return stack

def is_empty(stack):
    return len(stack) == 0

def push(stack,item):
    stack.append(item)
    print("Pushed item is: ",item)
    
def pop(stack):
    if is_empty(stack):
        print("Stack is empty. Cannot pop.")
    else:
        pop_item = stack.pop()
        print(f"Popped item: {pop_item}")

def display(stack):
    if is_empty(stack):
        print("Stack is empty.")
    else:
        print("Stack elements (top to bottom):")
        for item in reversed(stack):
            print(item)
    
    
def main():
    stack = Create_Stack()
    
    while True:
        print("\nMENU")
        print("1. Push an element into the stack")
        print("2. Pop an element from the stack")
        print("3. Display the stack elements")
        print("4. Exit from program")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to push: ")
            push(stack, item)
        elif choice == '2':
            pop(stack)
        elif choice == '3':
            display(stack)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the menu
main()
    