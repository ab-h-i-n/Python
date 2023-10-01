import random

num = random.randrange(0,100)

print("....Enter a number to start the game......")

tries = 12
while True:

    if tries <= 0:
        print("You failed...The correct answer is : "+str(num))
        break

    print("You got "+str(tries)+" tries")

    x = int(input("Enter number : "))

    tries = tries - 1

    if x < num :
        print("Your number is less than the answer")
    elif x > num:
        print("Your number is greater than the answer")
    else:
        print("You got the answer....Victory!!")
        break


