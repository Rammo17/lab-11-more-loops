number = int(input("Gimmy a number that is greater than 100...: "))

while number <= 100:
    print(str(number) + " is not greater than 100 dummy, try again...")
    number = int(input("That's not what I asked for, I said gimmy a number that is greater than 100...: "))

# imagine that the condition has been satisfied... exited the loop...
print(str(number) + " is greater than 100! FINALLY!")