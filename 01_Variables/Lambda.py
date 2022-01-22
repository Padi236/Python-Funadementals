#Lambda fun is a special func which doesnt have a name and is only used to returns values
#Lambda func are exclusively used to operate on inputs and return outputs

# Consider a simple add func

def add_num(x, y):
    return x + y

print(add_num(23,4))  

#Lets convert this to lambda function
#If you don't want to give it a name, then you would have to use it in the same line where you define it.

print((lambda a, b : a + b)(23,9))

#There are four parts to a lambda function
#1. the lambda keyword
#2. your parameter list
#3. colon
#4. return value without the return keyword

#if you want your lambda functions to have a name, assign it to a variable
add_func = lambda a, b : a + b

print(add_func(4,9))

##Significance of lambda functions
##Consider a double function whuch doubles the input value and return it.
def double(x):
    return x * 2

sequence = [1, 3, 5, 7, 9]

#To double the sequence
#1. List comprehension

#List comprehension method 1
double_sequence = [ num * 2 for num in sequence ]
print(f"This is double sequence with list comprehension : {double_sequence}")

#List comprehension method 2
##This is preferable, specially in case of complex math function
##Allows to potentially perfrom larger or more complicated mathematical expression
##without making list comprehension complicatedi i.e. readability
double_sequence_with_func = [ double(number) for number in sequence]
print(f"This is double sequence with function in list comprehension : {double_sequence_with_func}")

#3 With Lambda function
#Not easily readable when there is larger function
double_sequence_with_only_lambda = [ (lambda p : p *2)(x) for x in sequence]
print(f"This is double sequence with lambda in list comprehension : {double_sequence_with_only_lambda}")

#3. Lambda in conjunction with Map function
#Lambdas are meant to be short functions, often used without giving them a name, for example in conjunction with
#built in function map
#Map : It goes over each value in the sequence such as a List, tuple, Set and so on and 
#it applies the defined function(Here double) on each element and then return the final sequence as Map object
#So to print the sequence you need to typecast it into list first.
##Mostly List comprehension is used in pyrhon. But some programming languages dont use list comprehension
##Then we have to use Ma function 
double_sequence_with_map = list(map(double, sequence))
print(f"This is double sequence with map function and lambda :{double_sequence_with_map}")

#Note: List comprehension is faster than lambda
