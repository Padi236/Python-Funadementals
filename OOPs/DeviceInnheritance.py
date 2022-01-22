class Device():
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self) -> str:
        if self.connected:
            return f"{self.name!r} connected by ({self.connected_by})" 
        return f"{self.name} is disconnected"
    
    def disconnect(self):
        self.connected = False
        print(f"{self.name} is disconnected now")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remainingpages = capacity

    def __str__(self):
        return f"{super().__str__()}, (remaining pages:{self.capacity})" 

    def print(self, pages):
        if not self.connected:              #self.connected == False:
            return "You are not connected"
        print(f"Printing {pages} pages")
        self.capacity -= pages


device1 = Device("Keyboard", "USB")
print(device1)            

printer1 = Printer("HP Inkjet", "microUSB", 350)
print(printer1)

printer1.print(25)
print(printer1)

printer1.disconnect()

printer1.print(25)
print(printer1) 

#Here we have used inheritance to build out our __init__ and __str__ method using parent class super() methods
#In addition, printer can access the disconnect method defined in parent class.
#When you call the Printer.disconnect() method....
#Python will first look for disconnect method in derived class(Printer)
#If not found, it will then look for it in parent class(Device)
#The device class actually inherits from another class, which is the default inheritance, and that is Python's Object class 
#So if you call a method, which is not in the derived class or the parent class, python will then go to Object class to see if it is there
#If still not found, error will be raised
#So those are 3 level of calling we'll see while calling any method