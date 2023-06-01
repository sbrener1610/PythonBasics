# A story

print("You are swimming in the sea, you go further and further away from the shore. The weather is great and you feel fine. You forget yourself and lose the shore out of you sight. Suddenly the sky gets dark, and a strom starts before you know better.")
# Options for decision making & choice made


flag=0
while (flag == 0):
    choice=input("Where do you go? BACK/FORWARD/LEFT/RIGHT/DOWN: ")

    if choice == "FORWARD":
        print("The storm gets worse and you realize it is not the right direction.")
        
        flag1=0
        while (flag1 == 0):
            choice1 = input("Turn back? YES/NO: ")
            if choice1 == "YES":
                print("After a while you return to ths shore exhausted but alive. Well done")
                flag1=1
            elif (choice1 == "NO"):
                print("You die. Don't go swimming any more!")
                flag1=1 
            else:
                print("Bad input, try again")
        flag=1

    elif choice == "LEFT":

        flag1=0
        while (flag1 == 0):
            choice1 = input("Turn left? YES/NO: ")
            if choice1 == "YES":
                print("After a while you return to ths shore exhausted but alive. Well done, you did not lose your sense of orientation completely.")
                flag1=1
            elif (choice1 == "NO"):
                print("You die. Don't go swimming any more! Or at least take a compass, dude!")
                flag1=1 
            else:
                print("Bad input, try again")
        flag=1

    elif choice == "RIGHT":

        flag1=0
        while (flag1 == 0):
            choice1 = input("Turn right? YES/NO: ")
            if choice1 == "YES":
                print("After a while you return to ths shore exhausted but alive. Well done, you did not lose your sense of orientation completely.")
                flag1=1
            elif (choice1 == "NO"):
                print("You die. Don't go swimming any more! Or at least take a compass, dude!")
                flag1=1 
            else:
                print("Bad input, try again")
        flag=1

    elif choice == "BACK":

        
        print("After a while you return to ths shore feeling quite well, you are good in orienting in a storm!")
        flag=1
    
    elif choice == "DOWN":
        print("You drown, you idiot.")
        flag=1

    else:
        print("Bad input, try again")

    
                         