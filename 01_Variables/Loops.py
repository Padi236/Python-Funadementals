number = 23
#user_input = input("Do you want to play?  (Y/n) ").lower()

#While loop
while True:               ##user_input != "n":

    user_input = input("Do you want to play?  (Y/n) ").lower()

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    #Diff = abs(number - user_number)
    if user_number == number:
        print("You guessed it right")        
    else :
        print(f"Sorry, You were off by {abs(number - user_number)}")

#For each element in loop
list1 = [1,2,3,4,5,6,7,8,9,10]
evenList = []
for num in list1:       #for num in range(4)
    #exercise to create a list of only even numbers from a given list
    if num % 2 == 0:
        evenList.append(num)

    print(f"{num} is the integer.")
    
print(evenList)    

#For loop  
Grades = [70,80,85,75,66]
Total_Subjects = len(Grades)
Total_marks = 0

for eachGrade in Grades:
    Total_marks = Total_marks + eachGrade

#Total_marks can also be evaluated by Total_marks = sum(Grades)
Avg = Total_marks/Total_Subjects
print(Avg)



    
