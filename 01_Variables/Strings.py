MyName = "AnkitaParte"

#print(MyName)
#print(MyName*2)
#print(MyName+MyName)
#print(MyName+" "+MyName)

#f string; to embed values inside a string in python; takes value at that instant
MyCrush = f"Padi loves {MyName}"
print(MyCrush)
MyName = "AnkitaBhosale"
#to accomodate the dynamism include the f string directly into the print function
print(f"Padi loves {MyName}")

#Template String: Format method of the string; {} Placeholder
GreetHer = "How you doin' {}"
Her_name = GreetHer.format(MyName)
print(Her_name)

#Usually f string is used. Longer Template can be used with multiple values
First_talk = "Hey {}, Today is {}"
First_talk_val = First_talk.format(MyName,"Monday")
print(First_talk_val)





