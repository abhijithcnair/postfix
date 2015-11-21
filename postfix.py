def input_expression():
    input = raw_input("Enter a postfix expression")
    return input

def get_expression(input,operator,operand,i):
    if input in operator:
        operator= input
    else:
        operand = input
def push(operand,stack):
    stack.append(operand)
    return stack

def pop(stack):
    return stack.pop

def math_eval(operator,value1,value2,stack):
    if operator=='+':
        solution= value1 + value2
        
