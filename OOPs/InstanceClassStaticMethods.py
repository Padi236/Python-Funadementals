from msilib.schema import Class


class ClassTest():

    def __init__(self):
        pass

    #Instance methods are called by the class instance i.e. the class objects
    #Hence the instance methods needs object to call/invoke them    
    def instance_method(self):
        print(f"Calling instance_method for {self}")

    #classmethods takes argument cls(can be anything) and not the self
    #Hence are not called by the object or passed object as argument
    @classmethod
    def class_method(cls):
        print(f"Calling class_method of {cls}")

    #Doesn't have any parameter like cls or self
    #So they don't take any argument when you call them
    #So if you want a method/function inside a class that doesn't take/use class or the instance
    #decorate it with static method  
    @staticmethod
    def static_method():
        print("Called static_method")    


Test1 = ClassTest()
Test1.instance_method()
ClassTest.instance_method(Test1)

ClassTest.class_method()        #Python implicitly pass the Class name as the argument

ClassTest.static_method()       #Python doesn't pass any argument implicitly 

##################################################################################################################

#Instance method are used when you wanna produce an action that uses the data inside the object
#Also if you want to call the method to modify data inside the object

#Class methods are used often as factories

#Static method are used when you want to place that function inside the class 
#when you feel like it makes more sense there from code organisation point of view....

##################################################################################################################

#Factory example

class Books:
    Types = ("Hardcover", "paperback")      #Class variables; const

    def __init__(self, name, book_type, price):
        self.name = name
        self.book_type = book_type
        self.price = price

    #This is a representation of the book that allows us to with all the data included inside to recreate the book object
    #Use the __str__ method if you want to make it look nice for the user to read it
    def __repr__(self):
        return f"<Book {self.name} of type {self.book_type} is priced at RS.{self.price}>"

    #Create a method that will take in the name and price and will create the new book object of type hardcover
    #we are using Class inside a method defined inside the class
    #creating an object inside the class
    #since it is a class method it doesn't need an object
    @classmethod
    def hardcover(cls, name, price):
        return  cls(name, cls.Types[0], price+50)

    @classmethod
    def paperback(cls, name, price):
        return  cls(name, cls.Types[1], price)    

print(Books.Types)
book1 = Books("Harry Potter", "Hardcover", 1500)
print(book1.name)

book2 = Books.hardcover("Lord of the rings", 1200)
print(book2)

book3 = Books.paperback("Sherlock Holmes", 1200)
print(book3)




    

