#Create a list of student dictionary where each student has key of name school and grades

Students_list = [{"name" : "Padi", "school": "Air Force School", "Grades" : (70, 80, 90)},
    {"name" : "Ankita", "school": "Chate School", "Grades" : (80, 80, 90)},
    {"name" : "Suchi", "school": "Kendriya Vidyalaya", "Grades" : (60, 70, 80)},
    {"name" : "Momo", "school": "Zilla Parishad", "Grades" : (80, 90, 95, 75)}]


def avg_grades(data):
    grades = data["Grades"]
    grade_avg = sum(grades)/len(grades)
    return grade_avg

#print(avg_grades(Students_list))    #For a single Student dictionary

#Students_Avg_gradess = [avg_grades(Students_list) for Student in Students]
#Avg_grades_class = sum(Students_Avg_gradess)/len(Students_Avg_gradess)
#print(Avg_grades_class)

def avg_grades_all_students(studentdata):
    total = 0
    count = 0

    for eachStudent in Students_list:
        total = total + sum(eachStudent["Grades"])      #total += sum(eachStudent["Grades"])
        count = count + len(eachStudent["Grades"])

    print(f"Total sum of grades is {total} and the total number of grades are {count}")
    return total/count
    
print(f"Total average grade of class is {avg_grades_all_students(Students_list)}")
  





