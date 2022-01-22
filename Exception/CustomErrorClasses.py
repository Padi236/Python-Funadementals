#To use the custome error class YOU HAVE to inherit from the most relevant built-in error class
#like ValueError, RuntimeError, TypeError
#and then you can name it as you would like

class TooManyPagesReadError(ValueError):
    pass

class Book():
    def __init__(self, name: str, pages_count: int):
        self.name = name
        self.pages_count = pages_count
        self.pages_read = 0

    def __repr__(self):
        return(
            f"<Book: {self.name} read{self.pages_read} out of {self.pages_count}>"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.pages_count:
            raise TooManyPagesReadError(
                f"You are trying to read {self.pages_read + pages}, But the book is of {self.pages_count} pages"
                )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} out of {self.pages_count}")

book1 = Book("Harry Potter", 100)
try:
    book1.read(80)
    book1.read(50)      #This is absurd since you can't read more than total page count
                    #Hence we need to raise a custom exception here
except TooManyPagesReadError as t:
    print(t)

    






