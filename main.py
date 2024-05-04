from art import logo
endcode = True
print(logo)

#Functions
def add(n1, n2):
    output = n1 + n2
    return output

def substract(n1, n2):
    output = n1 - n2
    return output

def multiply(n1, n2):
    output = n1 * n2
    return output

def divide(n1, n2):
    output = n1 / n2
    return output

operations = {
    "+": add, 
    "-": substract, 
    "*": multiply, 
    "/": divide
}

num1 = int(input("What's the first number? : "))
num2 = int(input("What's the second number? : "))

for operators in operations:
    print(f"\n{operators}")

operator = input("Which operation do you wanna choose? : ")    

final_function = operations[operator]
answer = final_function(num1, num2)
print(f"{num1} {operator} {num2} = {answer}")
