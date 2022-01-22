#Elements are in Key-Value pairs
Friends = {"Padi" : 91, "Anki" : 95, "Suchi" : 94}
print(Friends.keys())
print(Friends.values())

#Add Element to dictionary
Friends["Vai"] = 93
print(Friends)

#List of dictionaries
Friends = [
            {"name": "Anki", "Age": "26", "Status" : "M"},
            {"name": "Suchi", "Age": "27", "Status" : "M"},
            {"name": "Momo", "Age": "26", "Status" : "M"},
          ]

print(Friends[1]["name"])

#Iteration over dictionary
#Method1
Students_grades = {"Padi" : 91, "Tadi" : 88, "AnKi" : 95}

for student in Students_grades:
    print(f"{student} attendence is {Students_grades[student]}")

#Method2
for studs, availaibilty in Students_grades.items():
    print(f"{studs} attendenCe is {availaibilty}")

#To access a particular value based on key only if it is available
if "Vai" in Students_grades:
    print(f"Padi attendence is {Students_grades['Padi']}" )
else:
    print("This student is not in this class")

#Average attendence
Attendence_values =  Students_grades.values()
print(f"{sum(Attendence_values)/len(Attendence_values):.2f}")
