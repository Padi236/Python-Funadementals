
#Collection: List, Tuple, Set, Dictionaries
#For Tuple Brackets are not necessary unless you want to specify it explicitly 
#or when python might be confused if you want to create a tuple or are these part of some other collection
from typing import ItemsView


x = 5, 11
print(x)

#but in case of list of tuples you need to specify brackets otherwise you will end up creating only list
List_Of_Tuples = [(2,4,6),(1,3,5)]

#Regarding destructing variables, this tuple here can be destructured/decomposed/split-out/unpacking into seperate variables
#Python is smart enough to assign values to these variable respectively. 
#Its a just a shorthand instead of assignong two variables seperately

#Python is smart enough to know that t here is a tuple and you are asking me to assign this tuple to these 
#variables, what Im gonna do is split it out into its component.

#Utility
x, y = 5, 11
print(x)
print(y)

#Consider a dictionary of students
Students_grades = {"Padi" : 91, "Tadi" : 88, "AnKi" : 95}

#Displayes the Dictionary items as lis of tuples
#This is because the The items() method returns a view object. 
#The view object contains the key-value pairs of the dictionary, as tuples in a list.
print(list(Students_grades.items()))

#We can iterate over this list of tuples 
for student_grade in list(Students_grades.items()):
    print(student_grade)

####
# Consider a list of tuple having people info

People = [("Ankita",26,"Developer"), ("Padi", 30, "Tester"), ("Sanaya", 34, "Actor")]

#Method1: iterate over tuple in normal way. Not a easily readable format.
for eachPeople in People:
    print(f"{eachPeople[0]} is {eachPeople[1]} years old and is a {eachPeople[2]}")     

#Method2: Desconstruct and then iterate. Much easy readable format.
for name,age,profession in People:
    print(f"{name} is {age} years old and is a {profession}") ## This way code is readable

#Ignoring variable with underscore( _ )
#If _ is used as an variable on its own that is because you dont care about this variable
#this variable is meant to be ignored

Stud = ("Padi", 30, "Tester")
name, _, Job = Stud
print(name, _, Job)

#Spliting a list into two
num = [1, 2, 3, 4, 5]
sir, *mam = num
print(sir)
print(mam)

*head1, tail1 = num
print(head1)
print(tail1)
print(*head1)




