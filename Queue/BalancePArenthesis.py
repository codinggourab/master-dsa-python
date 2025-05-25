def check_parentheses_balance(expression):
    
    stack = []

    
    parentheses_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    # Set of all opening parentheses
    opening_parentheses = set(parentheses_map.keys())

    # Set of all closing parentheses
    closing_parentheses = set(parentheses_map.values())

    # Iterate through each character in the expression
    for char in expression:
        # If it's an opening parenthesis, push it onto the stack
        if char in opening_parentheses:
            stack.append(char)
        # If it's a closing parenthesis
        elif char in closing_parentheses:
            # If the stack is empty, it means there's a closing parenthesis
            # without a corresponding opening one (unbalanced)
            if not stack:
                return False
            # Pop the top element from the stack
            top_char = stack.pop()
            # Check if the popped opening parenthesis matches the current closing parenthesis
            if parentheses_map[top_char] != char:
                return False # Mismatch found

    # After iterating through the entire expression, if the stack is empty,
    # all opening parentheses have been matched with their corresponding closing ones.
    # Otherwise, there are unmatched opening parentheses.
    return not stack

# --- Example Usage ---
print("--- Parenthesis Balance Checker ---")

# Test cases
expressions = [
    "({[]})",        # Balanced
    "([{}])",        # Balanced
    "({[})",         # Unbalanced - mismatched
    "((()))",        # Balanced
    "(()",           # Unbalanced - missing closing
    ")(",            # Unbalanced - leading closing
    "abc",           # No parentheses, considered balanced
    "",              # Empty string, considered balanced
    "[{()}]",        # Balanced
    "[{)]"           # Unbalanced - mismatched
]

for expr in expressions:
    result = check_parentheses_balance(expr)
    print(f"Expression: '{expr}' -> Balanced: {result}")