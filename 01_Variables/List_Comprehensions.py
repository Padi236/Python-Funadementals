
#Allows to create new list on the fly from the given list

List1 = [1,2,3,7,5]

#To create a list with double of each element
#Method 1: For loop
#Order of operation:Step1: Iteration Step2: Append the elements(after multiplying) 
doubleList = []

for num in List1:
    doubleList.append(num * 2)

print(doubleList)

#Method2: List Comprehension: 
#Order of operation:It might look the order is reversed but it is not really
#which is what ypu wanna put in your lit for the variable you are using in list1

doubleList1 = [num * 2 for num in List1]
print(doubleList1)

#2nd utility 
Friends = ["Padi", "Suchi", "Anki", "Momo", "Sanaya", "Zaira", "Sharu"]

#Create a list of friends that start with same letter
#Method 1: For loop
Friend_s = []

for eachFriend in Friends:
    if eachFriend.startswith("S"):
        Friend_s.append(eachFriend)

print(Friend_s)

#Method2: List comprehension
Friend_s1 = [eachFriend for eachFriend in Friends if eachFriend.startswith("S") ]
print(Friend_s1)

#In Cpython id represents the mem address
print("Friends is: ", id(Friends), "Friend_s is: ", id(Friend_s))

