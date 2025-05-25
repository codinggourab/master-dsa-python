def is_operator(char):
    return char in "+-*/^"

def precedence(operator):
    if operator in "+-":
        return 1
    elif operator in "*/":
        return 2
    elif operator == "^":
        return 3
    return 0

def infix_to_prefix(infix_expression):
    stack = []
    prefix_expression = ""
    
    reversed_infix = infix_expression[::-1]

    for char in reversed_infix:
        if char.isalnum():
            prefix_expression += char
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix_expression += stack.pop()
            stack.pop()
        elif is_operator(char):
            while stack and stack[-1] != ')' and precedence(char) < precedence(stack[-1]):
                prefix_expression += stack.pop()
            stack.append(char)

    while stack:
        prefix_expression += stack.pop()

    return prefix_expression[::-1]

infix_expression = "A + (B ^ (C + D - E) / F) + G / H"
prefix_expression = infix_to_prefix(infix_expression)
print(f"Infix Expression: {infix_expression}")
print(f"Prefix Expression: {prefix_expression}")