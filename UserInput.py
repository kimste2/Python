# takes 2 numbers and preforms basic operations on them
def addition(num1, num2):
    return num1 + num2

int_one = float(input("Please enter a number: "))
int_two = float(input("Please enter another number: "))

sum = addition(int_one, int_two)

print("The sum of %.2lf and %.2lf is %.2lf " % (int_one, int_two, sum))
