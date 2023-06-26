repeat = 'Y'
while repeat == "Y":
    user_input = input("Please enter your number:\n")
    num = int(user_input)
    if num > 0:
        print("Positive")
    else:
        print("Negative")

    again = input("Do you want to go again? (Y/N)\n")
    repeat = again
