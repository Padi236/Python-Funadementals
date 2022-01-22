#A moodule is a file that contains python code that we can use in our program

print(__file__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(dividiend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be zero")      #message attached to the error
        
    return dividiend / divisor

print("Calculator.py: ", __name__ )           