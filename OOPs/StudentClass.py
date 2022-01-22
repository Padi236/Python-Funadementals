#Consider a dictionary of student information
Student_info = { "name" : "Padi", "age" : 30, "team" : "Learning", "Grades" : (88,72,91,81,93)}

class Student:
    def __init__(self, name, grades):       #Constructor called immidiately an object is created
        self.name = name
        self.grades = grades

    def chk_pass_fail(self):
        for marks in self.grades:
            if marks < 40:
                return f"{self.name} has failed"
        return f"{self.name} is passed"                

    def AverageGrade(self):
        avg = sum(self.grades) / len(self.grades)
        return avg

    def showStudent(self):
        print(f"Student name: {self.name}")
        print(f"{self.name}'s grades: {self.grades}")
        print(f"{self.name}'s average grades: {self.AverageGrade()}")
        print(f"{self.chk_pass_fail()}")

    #str method is called when you want to turn your object into a string 
    #such as while printing it out or str(Obj reference)
    def __str__(self):      
        return f"Hello, {self.name}, your grades being {self.grades}  "

    #repr method is used to print out an unambiguous repesentation of an object so that you can recreate that object
    #The <> are just for looks for programmers to read the string inside those angular brackets
    #This method is used mostly while using python debugger
    def __repr__(self) -> str:
        return f"<{self.name} has {self.grades}. Also {self.chk_pass_fail}>" 
        
 
    def AvgGradesAll (listOfObjects):
        pass

student1 = Student("Padi", (85, 82, 93, 39, 72))
student2 = Student("Ankita", (85, 95, 75, 90))

print(student2)

student2.showStudent()
#Calculate average grades of all students

