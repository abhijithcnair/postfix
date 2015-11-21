def input_expression():
    input = raw_input("Enter a postfix expression")
    return input

def get_expression(input,operator,operand,i):
    if input in operator:
        operator= input
    else:
        operand = input
        
