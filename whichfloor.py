maximum_stories = 60
usernum = int(input("On what floor of the building is your office located?: "))

while(usernum > maximum_stories):
# statement for when the termination is NOT true which keeps the loop going...
    print("You enterred: " + str(usernum) + " but there are only " + str(maximum_stories) + " in this building. Try again...")
    usernum = int(input("On what floor of the building is your office located?: "))


print("Congrats! You work on floor number " + str(usernum))
