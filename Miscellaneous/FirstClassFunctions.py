#it mean that functions are just variables. You can pass them as arguments in any function or use them just like variables
from ast import Lambda
import operator


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be zero")
    return dividend / divisor     

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator = divide) 
#This will work as long as the number of arguments match with that of divide function
#In above statement divide function is not called as parenthesis() is not added after the function name
#We are passing the function name as only the value just like any other variable
#divide though being a function is passed to other function as argument
print(result)

##################################################################################################################

#Example 2

#type 3: with built_in operator: Comment type1 statement while using type 1 and 2
from operator import itemgetter

def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element

    raise RuntimeError(f"{expected} could not be found in the sequence")        

Friends = [
    {"name" : "Padi", "age" : 30},
    {"name" : "Anki", "age" : 26},
    {"name" : "Momo", "age" : 27}

]

def get_friend_name(friends):
    return friends["name"]

#type 1: withFirst class function
print(search(Friends, "Anki", get_friend_name))    
#type 2: with Lambda function
print(search(Friends, "Anki", lambda Friend :Friend["name"]))
#type3
print(search(Friends, "Anki", itemgetter("name")))  #funtion that creates a function and lets you use it afterwards

print(dir(itemgetter))



