import random

hand = ["Rock","Paper","Scissor"]

yourscore = 0
botscore = 0

while yourscore < 3 and botscore < 3:
    index = random.randrange(0,3)

    while True:
        print("1.Rock \n2.Paper \n3.Scissor")

        ch = int(input("\nEnter your choice : "))
        ch = ch-1

        if ch > 2:
            print("\nInvalid Choice!\n")
        else:
            break
        

    print("\n\nYou chosed : " + hand[ch])
    print("The computer chosed : " + hand[index])

    if ch == index:
        print("\nDraw!\n")
    elif (ch == 0 and index == 1) or (ch == 1 and index == 2) or (ch == 2 and index == 0):
        print("\nComputer wins!\n")
        botscore += 1
    else:
        print("\nYou wins!\n")
        yourscore += 1


print("\n\nYour score is : "+str(yourscore))
print("The computer score is : "+str(botscore))


if yourscore > botscore:
    print("\n\nYou win the game!")
else:
    print("\n\nYou loose the game!")