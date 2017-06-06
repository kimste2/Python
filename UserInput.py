"""""
take user input and pass them as arguments to functions and print output  
"""


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1,num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        print("Error! Cannot divide by zero!")
        return -1 # used as an error condition
    else:
        return num1/num2


def exponent(num1, num2):
    return num1 ** num2

num_one = float(input("Please enter a number: "))
num_two = float(input("Please enter another number: "))

sum = addition(num_one, num_two)
difference = subtraction(num_one, num_two)
product = multiplication(num_one, num_two)
quotient = division(num_one, num_two)
power = exponent(num_one, num_two)

print("The sum of %.2lf and %.2lf is %.2lf " % (num_one, num_two, sum))
print("The difference of %.2lf and %.2lf is %.2lf " % (num_one, num_two, difference))
print("The product of %.2lf and %.2lf is %.2lf " % (num_one, num_two, product))
print("The quotient of %.2lf and %.2lf is %.2lf " % (num_one, num_two, quotient))
print("The base of %.2lf raise to the exponent of %.2lf is %.2lf " % (num_one, num_two, power))