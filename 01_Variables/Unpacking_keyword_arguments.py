#The double asterisk(**) works in following way
#1. Can be used in a function to collect named arguments into a dictionary
#2. Can be used in a function call to unpack a dictionary into keyword aguments


#(**) collects keyword arguments and put it into a dictionary
def named(**kwargs):
    print(kwargs)

named(name = "Padi", age = 30)    #this will print the dictionary with **kwargs parameter

#Vice versa, we can unpack a dictionary into named arguments
def named_update(name, age):
    print(name, age)

My_info = { "name" : "Padi", "age" :25}
named_update(**My_info)
#named(**My_info) 


#Packing, Unpacking, Repacking dictionary
def named_func(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named_func(**kwargs)
    for args,value in kwargs.items():
        print(f"{args} : {value}")


print_nicely(name = "Padi", age = 30)

#First the named arguments will be collected into kwargs dictionary from the function call at line no 31
#Then we're gonna call the named_func bu w are going to unpack that dictionary into named arguments so we are gonna pass as it is


#*args = Position arguments
#**kwargs = Named arguments

#We can use both *args and **kwargs together
def MyFunc(*args, **kwargs):
    print(args)
    print(kwargs)

MyFunc(1, 3, 5, name = "Ankita", age = 26) #Preserve the order: First position then named arguments


