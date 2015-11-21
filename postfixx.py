
def get_input():
    return raw_input("enter the postfix string")

def push(operand,stack):
  # if value in operand:
	stack.append(int(operand))
        return stack
def pop(stack):
    stack.pop
    return stack
def evaluate(value1,value2,operator,stack):
    if operator =='+':
        solution=value2+value1
    elif operator =='-':
        solution= value2-value1
    elif operator=='*':
        solution = value2*value1
    elif operator == '/':
        solution = value2/value1
    return solution

def main():
    stack=[]
    evalu = get_input()
    #while(i):
   # new_list = list(evalu)
    operand= "0123456789"
    operators=['+','-','/','*']

    for value in evalu:
        if value in operand:
            push(value,stack)
        elif value in operators:
            
            value2= stack.pop()
            value1= stack.pop()
            operator = value
            
          
            result = evaluate(value1,value2,operator,stack)
            push(result,stack)
            print stack[0]
           # print result

if __name__ == '__main__':
    main()
    

            
