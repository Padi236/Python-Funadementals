#Everything in python is object and we can check this using type() function
#It displays the class of the object under consideration
list1 = [1, 3, 5, 7]
print(type(list1))

tuple1 = (1, 3, 5, 7)
print(type(tuple1))

set1 = {"Padi", 236, "Ankita", 49}
print(type(set1))

str1= "Ankita is the best"
print(type(str1))

dict1 = {"name" : "Padi", "age" : 30, "dept": "learning"}
print(type(dict1))

n1 = 49
print(type(n1))

f1 = 23.49
print(type(f1))

def MyFunc():
    pass
print(type(MyFunc))

Flag = True
print(type(Flag))

#Use dir() function, to list out all the attributes and methods of the object
 
print(dir(list1))
print(list1.__add__(list(tuple1)))  #list1 is not affected.
print(list1)
list1.reverse()
print(list1)
#list1.clear()
#print(list1)
print(list1.pop())
print(list1)
list1.sort()
print(list1)
list1.insert(0, 23)
print(list1)
list1.remove(5)
print(list1)

## id() return the id of an object .It is unique ID.
#Consider a list of numbers

numbers1 = [1, 2, 3, 4]
print(numbers1)
print(id(numbers1))

#Pyhton does memory optimisation by referring the different variable to same object
#For example
numbers2 = numbers1     #Here the number2 and number1 refers to same object
print(numbers2)         #Therefore both will have same id and content
print(id(numbers2))

#So if we append an element in numbers1 it will be reflected in numbers2 as well
#Even you haven't made any changes to numbers2
numbers1.append(23)
print(f"numbers1 is : {numbers1} and numbers2 is : {numbers2}")

#To counter this we use copy methodof list
numbers3 = numbers1.copy()
numbers1.append(49)
print(f" num1 is {numbers1}")
print(f" num2 is {numbers2}")
print(f" num3 is {numbers3}")
print(f"num1 id: {id(numbers1)}")
print(f"num2 id: {id(numbers2)}")
print(f"num3 id: {id(numbers3)}")
