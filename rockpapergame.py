import random
Cchoice=["Rock","Paper","Sessior"]
while True:
    print("Rock paper sessior game : ")
    youwin=0
    computerwin=0
    for i in range (1,4):
        print("round",i,"start : ") 
        print("please select any option : ")
        print("1. Rock","2. Paper","3. Sessior ")     
        yourchoice=int(input())
        if yourchoice==1:
            print("you select Rock ")
            yourchoice="Rock"
        elif yourchoice==2:
            print("you select Paper ")
            yourchoice="Paper"
        elif yourchoice==3:
            print("you select Sessior ")
            yourchoice="Sessior"
        else:
            print("Invalid Choice")
        computerchoice=random.choice(Cchoice)
        print("computerselected : ",computerchoice)
        if yourchoice==computerchoice:
            print("Drawn")
        elif (yourchoice=="Rock" and computerchoice=="Sessior") or (yourchoice=="Paper" and computerchoice=="Rock") or (yourchoice=="Sessior" and computerchoice=="Paper"):
            youwin+=1
            print("you win this round")

        else:
            computerwin+=1
            print("computer win this round")
    if youwin>computerwin:
        print("you win this game ")
        print("score is : ","your score is =",youwin,"computer score is = ",computerwin)
    elif computerwin>youwin:
        print("you lose the game and computer win the game ")
        print("score is : ","your score is =",youwin,"computer score is = ",computerwin)
    else:
        print("match drawn")
        print("score is : ","your score is =",youwin,"computer score is = ",computerwin)
    user_choice=input("enter your choice : ")
    if user_choice=="yes" or user_choice=="Yes" or user_choice=="YES":
        continue
    else:
        break