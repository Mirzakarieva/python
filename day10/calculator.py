#Calculator


#Add
def add(a, b):
    return a+b

#Subtract
def subtract(a, b):
    return a-b

#Multiply
def multiply(a, b):
    return a*b

#Divide
def divide(a, b):
    return a/b


arithmetical_operations={
    "+": add ,
    "-": subtract ,
    "*": multiply ,
    "/": divide
}
def calculator():
        
    num1 =  float(input("What's the first number?: "))
    continued = True
    while continued == True:
        for operation in arithmetical_operations:
            print(operation)

        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input ("What's the second number?: "))

        calculate = arithmetical_operations[operation_symbol]
        answer = calculate(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        con = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation.: ")
        if con == "y":
            num1 = answer
        else:
            calculator()


calculator()


# operation_symbol = input ("Pick another operation: ")
# num3 = int (input ("What's the next number?: "))
# calculation_function = arithmetical_operations [operation_symbol]
# second_answer = calculation_function (calculation_function (num1, num2), num3)
# print (f"{first_answer} {operation_symbol} {num3} = {second_answer}")
