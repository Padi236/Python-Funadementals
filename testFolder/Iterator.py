#an object which has __iter__ method is iterable

Friendlist = ["Suchi", "Momo", "Vai", "Ankita", "Deven"]
print(dir(Friendlist))

print(Friendlist.__iter__())

#Iterator in python is simply an object that can return data one at a time while iterating over it.
##For an object to be iterator ot must implement 2 methods: iter, next

itr = Friendlist.__iter__()     #equivalent to iter(Friendlist)

#print(itr.__sizeof__())

#item1 = itr.__next__()          #equivalent to next(itr)
#print(item1)

#item2 = next(itr)
#print(item2)

#item3 = next(itr)
#print(item3)

item4 = next(itr)
print(item4)

##Trivia: For loops internally uses while loops to iterate through sequences

while(True):
    try:
        element = next(itr)
        print(element)

    except StopIteration:
        print("You've reached the end of iteration")
        break

##################################################################################################################
# Creating custom iterators
class Even:
    def __init__(self,max):
        self.n = 2
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration


evenObject = Even(10)

print(next(evenObject))
print(next(evenObject))
print(next(evenObject))

##################################################################################################################

#Significance of iterator
#Iterator are powerful tools when dealing with large stream of data              
#If you use regular list  to store these values our computer will run out of memory quickly
#With iterator,however, we can save resources as they return only one element at a time.
#So in theory, we can deal with infinite data with finite memory   
#Generally, in python, iterators are implemented using generators that make it much easier to use



