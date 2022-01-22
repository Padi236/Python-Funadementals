#Decorators allow us to very easily modify function

#import functools as a ounter measure
import functools

user = {"name" : "Padi", "access_level" : "admin"}

#def get_admin_password():
#    return "1234"

#print(get_admin_password())         #Admin password is accessible before securing it

#Following code allows the secure the above function(get_admin_password()) from admin_level == guest
#Otherwise we would have to handle it with if else statements everywhere

def make_secure(func):
    @functools.wraps(func)      #counter measure: suggesting secure_function that it is wrapper for func
                                #preserving the names and documentation of the get_admin_password()
    def secure_function():
        if user["access_level"] == "admin":
            return  func()
        else:
            print(f"No admin permissions for {user['name']}")    
    return secure_function
     
#get_admin_password = make_secure(get_admin_password)
#The above commented line can have disadvantage that if the get_admin_password function is placed above or below
#To counter that we have pie(@) symbol which equivalent to above statement of function assignment 

#If you put @make_secure on top of function definition, that will prevent the function from being created as it is
#And instead it will create it and pass it through decorator, in one go
@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password())         #Admin password is not accessible after securing it             

#One proble with decorator or function assignment is that 
#when you replace the function get_admin_password() by secure_function(), the name of the function changes
#get_admin_password() still exists as a name inside python but it is no longer registered as a function internally
#Now the secure_function is registered as a function internally
#There are some libraries that will actually use that internal name.
#for example
print(get_admin_password.__name__)      #prints into secure_function so the name of the function changed

#In addition if there is any documentation attached to the get_admin_password() will also be lost
#once the function is replaced since secure_function() has no documentation

#Counter measure: use another decorator 

##################################################################################################################

def parent(num):
    #print("This is parent calling")
    def first_child():
        return "Hi This is first child"

    def second_child():
        return "Hi This is second child"

    if num == 1:
        return first_child
    #Note that you are returning first_child without the parentheses. 
    #Recall that this means that you are returning a reference to the function first_child.
    #In contrast first_child() with parentheses refers to the result of evaluating the function

    else:
        return second_child
    
#You can now use first and second as if they are regular functions, 
#even though the functions they point to can’t be accessed directly
#In this example, you did not add parentheses to the inner functions—first_child—upon returning. 
#That way, you got a reference to each function that you could call in the future
first = parent(1)
print(first())      

##################################################################################################################

#Decorator functions with parameters

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_whee(name):
    print(f"Whee! {name}")

say_whee("Ankita")        

##################################################################################################################

#Decorator functions with parameters

end_user = {"name" : "Ankita", "access_level" : "superuser"}

def make_secure(func):
    @functools.wraps(func)

    def secure_function(*args, **kwargs):
        if end_user["access_level"] == "superuser":
            return  func(*args, **kwargs)
        else:
            print(f"No admin permissions for {end_user['name']}")    
    return secure_function
     

@make_secure
def get_superuser_password(accessor):
    if accessor == "superuser":
        return "1234"
    elif accessor == "admin" :
        return  "Still not a superuser doofus"
    else:
        return "Get out of here"       

print(get_superuser_password("superuser"))

##################################################################################################################

#Decorators with parameters

userList = {"name" : "Suchita", "access_level" : "superuser"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)

        def secure_function(*args, **kwargs):
            if userList["access_level"] == access_level:
                return  func(*args, **kwargs)
            else:
                print(f"No {access_level} permissions for {userList['name']}")    
        return secure_function
    return decorator    
     

@make_secure("admin")
def get_admin1_password(accessor):
    return "admin:1234"

@make_secure("user")
def get_user_password(accessor):
    return "user:user_password"

@make_secure("superuser")
def get_superuser1_password(accessor):
    return "superuser:su_password"        
    

print(get_admin1_password("guest"))
print(get_user_password("guest"))
print(get_superuser1_password("guest"))

     