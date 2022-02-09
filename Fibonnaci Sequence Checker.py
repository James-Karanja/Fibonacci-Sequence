import math

num = int(input ("\nEnter any number to be checked whether it is in the Fibonnacci Sequence or Not: \n"))

def fibonacciChecker():
    k = int(5*num*num+4)
    s = int(5*num*num-4)
    square1 = math.sqrt(k)
    square2 = math.sqrt(s)
    print("\n")
    if (square1 - int(square1) == 0 or square2-int(square2) == 0):
        print(num,"is a Fibonacci number\n")
    else:
        print(num,"is not a Fibonacci number\n")

fibonacciChecker()