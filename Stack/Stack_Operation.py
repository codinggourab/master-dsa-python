#stack implementation using Array
# def Create_Stack():
#     stack = []
#     return stack

# def is_empty(stack):
#     return len(stack) == 0

# def push(stack,item):
#     stack.append(item)
#     print("Pushed item is: ",item)
    
# def pop(stack):
#     if is_empty(stack):
#         print("Stack is empty. Cannot pop.")
#     else:
#         pop_item = stack.pop()
#         print(f"Popped item: {pop_item}")

# def display(stack):
#     if is_empty(stack):
#         print("Stack is empty.")
#     else:
#         print("Stack elements (top to bottom):")
#         for item in reversed(stack):
#             print(item)
    
class Stack:
    def __init__(self,cap):
        self.cap = cap
        self.top = -1
        self.s = [0] * cap
        
    def  push(self,data):
        if self.top == self.cap - 1:
            print("Stack is overflow")
            return False
        else:
            self.top += 1
            self.s[self.top] = data
            return True
        

    def pop(self):
        if self.top < 0:
            print("stack is underflow")
        else:
            popped = self.s[self.top]
            self.top -= 1
            return popped
    def peek(self):
        if self.top < 0:
            print("stack is underflow")
        return self.s[self.top]

    def is_empty(self):
        return self.top < 0

    def display(self):
        if self.top < 0:
            print("stack is underflow")
        else:
            for i in range(self.top,-1,-1):
                print(self.s[i])
    

def main():
    
    s =  Stack(10)
    while True:
        print("\nMENU")
        print("1. Push an element into the stack")
        print("2. Pop an element from the stack")
        print("3. Display the stack elements")
        print("4. Exit from program")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to push: ")
            s.push(item)
        elif choice == '2':
            s.pop()
        elif choice == '3':
            s.display()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the menu
main()
    