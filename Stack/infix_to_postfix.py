def prec(c):
    if c == '^':
        return 3
    elif c in ('*', '/'):
        return 2
    elif c in ('+', '-'):
        return 1
    else:
        return -1
    

def infix_postfix(e):
    st = []
    res = ''
    
    for c in e:
        if c.isalnum():
            res += c
        elif c == '(':
            st.append('(')
        elif c == ')':
            while st and st[-1] != '(':
                res += st.pop()
            st.pop()
        else:
            while st and prec(c) <= prec(st[-1]):
                res += st.pop()
            st.append(c)
    while st:
        res += st.pop()
        
    return res
exp = 'A*(B+C-D)'  
print(f"Infix expression is: {exp}")
print(f"Postfix expression is: {infix_postfix(exp)}")

infix_postfix(exp)
                
        