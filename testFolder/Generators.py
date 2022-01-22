#Generators are elegant wy to create custom itrators in python that makes it really easy to work with iterators
#For an object to be an iterator it should implement iter method which would return the iterator object
#and the next method which will return the next value in the stream
#and possibly raise StpIteration exeption when there is no value to returned

#As you can see this is a bit of lengthy process
#To counter these we will make use of Generator

#Generator is simply a functon with slight modification inside it so that we can implement iterators
#To make normal function into a generator, we need to implement one or more yield keywords
#In this, we will use the yield keyword to get the next item of the iterator

#The diff between return and yield statement is that the return statement terminates the function completely
#whereas the yield statement pauses the function, saving all its state, for next successive calls. 

def even_generator():
    n = 0
    n += 2
    yield n
    
    n += 2
    yield n
    
    n += 2
    yield n
    
    n += 2
    yield n


numbers = even_generator()
print(next(numbers))        #gives value of first yield
print(next(numbers))
print(next(numbers))


#Implementing a loop for the generator to return numbers till a limit

def even_generator_limit(limit):
    n = 2

    while(n <= limit):
        
        yield n
        n += 2

num = even_generator_limit(6)
print(next(num))            #2
print(next(num))            #4
print(next(num))            #6
#print(next(num))            #raised StopIteration, after the limit is reached

#When Compared with custom iterator, it can be noticed that
#we don't have to explicitly define the iter method, next method or raise the stopIteration exception
#They are handled implicitly by the Generators making our code easy to write and understand

##################################################################################################################

#Task: Fibonacci series

def generator_fibonacci():
    
    n1 = 0
    n2 = 1

    while(True):

        yield n1
        n1 ,n2 = n2, n1+n2

sequence = generator_fibonacci()

print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))

#If we would have used a for loop and a list to store this infinite sequence we would have run out of memory
#However with generators, we can keep accessing these terms as long as we want
#it is because we are dealing with only one item at a time


