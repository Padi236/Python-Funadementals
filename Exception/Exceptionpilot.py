#Exception handling is the process of responding to exception in a custom way during the execution of program
#Errors are often used to flow control

from  OOPs import Calculator

try:
    
    print ("Welcome to the average grade program")

    Students = [
                {"name": "Padi", "Age": 30, "grades" : [ 88, 72, 93, 81, 91]},
                {"name": "Anki", "Age": 36, "grades" : [ ]},        #88, 65, 93, 90, 91
                {"name": "Suchi", "Age": 30, "grades" : [89, 80, 93, 85, 75]}        #89, 80, 93, 85, 75
    ]
    
    for student in Students:
        name = student["name"]
        #age = student["age"]
        grades = student["grades"]
        average = Calculator.divide(sum(grades), len(grades))
        print(f"Average grade marks of {name} is {average}")
           
#Except clause/block is executed if any exceptions/error is raised
#You can have multiple except clauses, wherein you can catch those exceptiondiffernetly and handle them differently.   
except ZeroDivisionError as e:
    #print(e)       #prints the default message associated with the exception defined in the concerned function(here, divide) 
    print(f"ERROR: No grades defined for {name}")

except IndexError:
    print("Invalid index. Stay in your limit")    

#This clause/block is executed only if the try block executed succesfully
#The significance of this block is to catch specific form of errors and you don't want all your code in one block
else:               
    print("All students averages calculated successfully")
    #print(f"The average grade is: {avg}")

#finally block/clause is executed regardless of any exceptions occur or not
finally:
    print("We are in finally block")    
