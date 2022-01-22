## Type of bracket decides Data structure type
List1 = ["Padi", "Ankita", 3 , "Suchi", 5 , "Mruno", "Vai", "Ankita"]
Tuple1= ("Padi", 2 , "Adi", "Saba", "Adi")
Set1 = { 1 , "Padi", "Sharu", 4 , "Dhani", "Dhani"}
Set2 = {"Padi", "Ankita"}
print(List1)
print(Tuple1)

#Adding Element to the list
List1.append(6)
print(List1)

#List length
print(List1.__len__())

#Removing elements from the list
List1.remove("Ankita")
print(List1)

#Tuple length
print(Tuple1.count("Adi"))

#Adding elements to Set 
print(Set1)
Set1.add("Tadi")
print(Set1)

#Removing element from Set
Set1.remove("Dhani")
print(Set1)

#Differnece between two Sets: Removes element from Set1 which are in Set2: Set1 - Set2
#excludes elements which are in Set2 but not in Set1
print(Set1.difference(Set2))

#Union of sets(excludes duplicates)
print(Set1.union(Set2))

#Intersect between 2 Sets
Arts = {"Padi", "Vai", "Anki", "Deven"}
Science ={"Padi", "Suchi", "Momo", "Vai"}
Both = Arts.intersection(Science)
print(Both)

#Exercise
