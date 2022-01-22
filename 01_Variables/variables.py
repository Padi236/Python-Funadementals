x = 4
price = 9.99
discount = float(input("Enter the discount value "))
result = price *(1- discount)
print('%.2f'%result)
print("{0:.2f}".format(result))
print(round(result))
print(round(result,2))
print(f"The result is {result:.2f}")

number = 7
user_input = input("Do you want to play: ").lower()

if user_input == "y":
    user_number = int(input("Guess our number: "))
    Diff = abs(number - user_number)
    if user_number == number:
        print("You guessed it right")
        
    elif abs(number - user_number) != 0:
        print("You were off by ", Diff)
    
        


