#Comparisons: ==, >, <, !=, <= , >=
print(5 == 4)
print(5 == 5)
print(5 > 4)
print(5 != 4)

Arts = ["Padi", "Vai", "Anki", "Deven"]
Science =["Padi", "Suchi", "Momo", "Vai"]
print(Arts == Science)
Arts = Science 
print(Arts == Science)

# 'is' operator; it identifies if the 2 data structur are exact same thing(vakue as well as mem loc)
Arts1 = ["Padi", "Vai", "Anki", "Deven"]
print(Arts is Arts1)
