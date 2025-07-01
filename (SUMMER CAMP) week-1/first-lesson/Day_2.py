def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

def say_hello_10_times():
    for i in range(10):
        print("Hello, World!")

say_hello_10_times()



def addition_function(num1, num2):
    return num1 + num2

def sub_function(num1, num2):
    return num1 - num2

def mul_function(num1, num2):
    return num1 * num2

def div_function(num1, num2):
    return num1 / num2

def mod_function(num1, num2):
    return num1 % num2

def power_function(num1, num2):
    return num1 ** num2

def floor_function(num1, num2):
    return num1 // num2

def sqrt_function(num1):
    return num1 ** 0.5

def cube_function(num1):
    return num1 ** 3




def do_my_operations(num1, num2, operator):
    if operator == "+":
        return addition_function(num1, num2)
    elif operator == "-":
        return sub_function(num1, num2)
    elif operator == "*":
        return mul_function(num1, num2)
    elif operator == "/":
        return div_function(num1, num2)
    elif operator == "%":
        return mod_function(num1, num2)
    elif operator == "**":
        return power_function(num1, num2)
    elif operator == "//":
        return floor_function(num1, num2)
    elif operator == "sqrt":
        return sqrt_function(num1)
    elif operator == "cube":
        return cube_function(num1)
    else:
        return "Invalid operator"

standard_input = int(input("Enter the first number: "))
standard_input2 = int(input("Enter the second number: "))
standard_input3 = input("Enter the operator: ")

print(do_my_operations(standard_input, standard_input2, standard_input3))










