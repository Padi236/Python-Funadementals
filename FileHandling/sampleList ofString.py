ListOfString = ["My name is Padi", "I'm a tester by profession", "I'm 30 year old "]
for eachString in ListOfString:
    print(eachString)

ListOfString[0] = ListOfString[0].replace("Padi","Padi bhai")
print(ListOfString[0])

for eachString in ListOfString:
    print(eachString)
