# A story

print("You are swimming in the sea, you go further and further away from the shore. The weather is great and you feel fine. You forget yourself and lose the shore out of you sight. Suddenly the sky gets dark, and a strom starts before you know better.")
# Options for decision making & choice made


#flag=0
MovesCount=0
Direction=2

while (MovesCount<=5):
    choice=input("Where do you go? BACK/FORWARD/LEFT/RIGHT/DOWN: ")

    if choice.upper() == "FORWARD":
        MovesCount+=1
        #print("The storm gets worse and you realize it is not the right direction.")
        Direction+=0
        Direction%=4

        """
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
        """

    elif choice.upper() == "LEFT":
        MovesCount+=1
        Direction+=3
        Direction%=4

        """
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
        """

    elif choice.upper() == "RIGHT":
        MovesCount+=1
        Direction+=1
        Direction%=4
         
        """ 
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
        """

    elif choice.upper() == "BACK":
        MovesCount+=1
        Direction+=2
        Direction%=4

        """
        print("After a while you return to ths shore feeling quite well, you are good in orienting in a storm!")
        flag=1
        """
    
    elif choice.upper() == "DOWN":
        print("You drown, you idiot.")
        break
         
        
    else:
        print("Bad input, try again")
        continue

    if Direction == 2:
        print("The storm gets worse and the waves are smashing into your face. You realize it is not the right direction.")
    if Direction == 1:
        print("The storm gets worse and the wind is killing you. You realize it is not the right direction.")
    if Direction == 3:
        print("The storm gets worse and the sharks gather waiting for tasty food. You realize it is not the right direction.")
    if Direction == 0:
        print("The direction seems right. You let the waves brings you ashore. You are safe. It took you ", MovesCount, " tries to solve it.")
        break
    if MovesCount == 5:
        print("You are exhausted and drown.")
        

    
                         