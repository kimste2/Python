"""
Fizz Buzz: 
"Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”
"""
for x in range(1, 100):
    if x % 5 == 0 and x % 3 == 0:
        print("%d FuzzBuzz\n" % x)
    elif x % 5 == 0:
        print("%d Buzz\n" % x)
    elif x % 3 == 0:
        print("%d Fizz\n" % x)
