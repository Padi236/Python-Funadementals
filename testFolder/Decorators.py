#Python Decorator is a  function that takes another function adds some functionality to it and returns original function
#Variables are just identifiers bounds to the object

def inc(x):
    return x + 2

def operate(func,x):
    result = func(x)
    return result

print(operate(inc,3))    
##################################################################################################################
#a function can take another function as argument
#In python, we can also define a func inside a func

def print_message(msg):
    greeting = "Hello"

    def printer():
        print(greeting,msg)

    printer()

print_message("Hola Amigo!!!")
##################################################################################################################
#We can also return the function instead of returning only the value

def print_message(msg):
    greeting = "Hello"

    def printer():
        print(greeting,msg)

    return printer

func = print_message("Ankita there???")     #Here will be the function returned to
func()             #and then we call the func

#Note:
#The outer function <print_message> is done executing at line 36
#This should mean that all its local scope variables should be destroyed after its done executing
#However, when we call the func at Line no. 37, 
#we still have access to local scope variables (greeting and message) in inner function <printer>
#Such a function is called a closure
#A closure is an internal function which remembers the values and variables in its enclosing scope
#even if the outer function is done executing
#Python decorators makes extensive use of the closure
##################################################################################################################
#Ex: a decorator function that prints some info before and after executing another function

def printer():
    print("Hello World!!!")

#decorator function
def display_info (func):
    def inner():
        print("Executing", func.__name__ , "function" )
        func()
        print("Finished execution")     
    return inner

printer()    

#We can use the decorator function to run the same printer function

decorated_func = display_info(printer)
decorated_func()

#Here the decorated function act as a wrapper. It allows us to add functionality to the past function
#without changing the code of the original function
#In Python, we have much more elegant way of writing these line implicitly using @ symbol

##################################################################################################################
#decorator function
def display_info1 (func):
    def inner1():
        print("Executing", func.__name__ , "function" )
        func()
        print("Finished execution")     
    return inner1

@display_info1             
def printer1():
    print("Hello World!!!")

#Adding @symbol on top of the function definition means that 
#we are passing that function<printer> as an argument to the decorator function<decorated, dispay_info>
#and reassigning the function<printer> to the returned function<inner>

printer1()

##################################################################################################################

def smart_divide(func):
    def inner(a, b):
        print("Dividing", a ,"by", b)
        if b == 0:
            print("Can't divide by 0")
            return
        return func(a,b)
    return inner    

@smart_divide
def divide(a, b):
    return a / b

result1 = divide(15,3)
print(result1)
result2 = divide(5,0)
print(result2)    

##################################################################################################################
#Chaining decorators
#we can decorate a function multiple times with one or more decorators

#decorator func 1
def star(func):
    def inner(arg):
        print("*"*30)
        func(arg)
        print("*"*30)
    return inner

def percent(func):
    def inner(arg):
        print("%"*30)
        func(arg)
        print("%"*30)
    return inner    

@star                   #Star function wraps the percent function
@percent                #percent function wraps he printer function
def printer(msg):
    print(msg)

printer("Love you Ankita!!!!!")    


