#To accept/collect a set of arguments in one/single parameter use (*)asterisk before the variable
#The values are stored in args variable in the form of tuple of arguments

def multiply(*args):
    #print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total    

print(multiply(1, 3, 5))

#This goes the other way around as well
#Note that here the asterisk(*) is used to destructure the argument into number of parameters
#Though the number of arguments in original list/tuple/Set should be same as the number of parameters

def addition(x, y, z):
    return x + y + z

marks = [1, 3, 5]
print(addition(*marks))

#Lets try with named arguments
print(addition(x = 1, y = 3, z = 5))

#Consider a dictionary 
grades = {"x" : 3, "y" : 5, "z" : 7}
print(addition(grades["x"], grades["y"], grades["z"]))      #but this looks ugly

#Alternativly, 
print(addition(x = grades["x"], y = grades["y"], z = grades["z"]))

#Observe that here the named argument(parameter names) and the dictionary keys are same, that is, 'x' and 'y'
#So in such a situation we can simplif the code as
print(addition(**grades))

#It tells the python that you've got the dictionary with 2 keys
#So I'm gonna pass each key as named argument and the value be the one that's associated with the key


#Consider a function apply that collects number of aguments and one required named argument
def apply(*args, operator):
    if operator == "+":
        return sum(args)
    elif operator == "*":
        return multiply(*args)  #This will return only as tuple because we are not passing different arguments but a
                                #tuple of arguments, hence we need to pass (**) to destructure/umpack the tuple before passing
    else:
        print("Invalid operator") 

print(apply(1, 3, 5, 7, operator = "*"))

