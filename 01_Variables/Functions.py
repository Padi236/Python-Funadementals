
def add_Stud():     #Function Definition
    stud = input("Enter student's name: ")
    Student_info.append(stud)

Student_info = ["Padi", "Anki", "Sanaya"]       #Global variable
add_Stud()
print(Student_info)

##Function parameters, Passing the arguments
#1. Positional arguments
def say_hello(name, surname):       #function parameters
    print(f"hello, {name} {surname}")

say_hello("Anki", "Padi")           #function arguments

#2. Keyword/named arguments
def say_Howdy(name,surname):
    print(f"Howdy, {name} {surname}")

say_Howdy(surname="Padi", name="Anki")    

#No spaces around equal sign between keyword and argument
#You can simulatneous have position argument and keyword argument, but positional argument goes first 
#like("Padi", name="Anki") --- This will work
#like(surname="Padi", "Anki") --- This won't work
#Same rule is applied to Function definition

###Default parameter
def Discounted_Price(MRP,disc=5):         #MRP is required parameter, Default parameter is overriden if passed
    Net_amount = MRP*(1 - (disc/100))
    print(f"The final price is {Net_amount}")

Discounted_Price(MRP=200, disc=20)    

#DO NOT USE GLOBAL VARIABLE AS DEFAULT PARAMETER