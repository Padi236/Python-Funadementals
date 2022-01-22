#Composition is a counterpart to inheritance so you build out classes that use other classes.
#Composition allows your classes to be simpler and reduces the complexity of your code overall,
#Inheritance is 'is -a' relationship. For e.g. Printer is a device. And not, Printer has a device
#Composition is 'has -a' relationship. For e.g. A Bookshelf has many books. And not, Bookshelf is a book

#class Book(Bookshelf): This is bad approach, 'cos A bookshelf can contain books, but one isn't the other        
#So the conceptual reason is a book is not a bookshelf.
#The technical reason is there is no reason to inherit if you're not gonna use that inheritance anywhere

#So this is where composition comes in. Composition is for when you wanna say something like, a bookshelf has many books.
#A bookshelf is composed of a bunch of things and books. So instead of defining our bookshelf and our book like this,
#we're going to define it slightly differently.

class Bookshelf():
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return "Bookshelf with {} books".format(len(self.books))

class Book():      
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} book is in bookshelf"

book1 = Book("Harry Potter")
#print(book1)

book2 = Book("Lord of the rings")
#print(book2)

bookshelf2 = Bookshelf(book1, book2)
print(bookshelf2)

#This is composition and this is very common, much more common than inheritance.
#It is when you have a class that contains a bunch of other classes or a class that has as many of that.
#And the here we've got our bookshelf that has many books.
#And when you use it, when you create it, you can pass to it a bunch of your other book objects.
#So to recap. Inheritance means that a book is a bookshelf, composition means that a bookshelf has many books.
