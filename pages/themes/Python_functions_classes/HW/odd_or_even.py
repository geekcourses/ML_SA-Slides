# ask user to enter a number and save what hi/she enters in user_input variable:
user_input = input('Please, insert a number:')
# print("user input type: ", type(user_input))

# input always give us a string, and we need a number type, so let's convert it:
user_number = int(user_input)
# print("user number type: ", type(user_number))


# if the number is 0:
if user_number == 0 :
    print("I can not say if 0 is even or odd!")
#if the number is divisible by 2
elif user_number % 2 == 0:
    print("The number {} is EVEN!".format(user_number))
# if the number is not 0 and is not divisible by 2:
else : 
    print("The number {} is ODD!".format(user_number))


