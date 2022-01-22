#Consider a list of tuples

Users = [
    (0, "Padi", "30", "P@di1709"),
    (1, "Ankita", "26", "Ankit@0409"),
    (2, "Suchi", "27", "Such!45"),
    (3, "Momo", "26", "Momo@307"),
]

#To gather information about a user 
#1 Using for loop. This is rather complicated method

for user in Users:
    if user[1] == "Suchi":
        print(user)

#Using Dictionary comprehension

user_mapping_with_dictionary = {username[1]: username for username in Users}
print(user_mapping_with_dictionary)

##### Example: Login User Credentials

user_input = input("Enter user name: ")
password_input = input("Enter password: ")

#Deconstruct the tuple
_, LoginName, Age, LoginPassword = user_mapping_with_dictionary[user_input]

print(LoginName, Age, LoginPassword)


if password_input == LoginPassword:
    print("Password Matched")
else:
    print("Password is incorrect")    



