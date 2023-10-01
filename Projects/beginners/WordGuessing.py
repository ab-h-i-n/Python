import random

words = ["apple", "orange", "mango", "grape"]

word = random.choice(words)

guesses = word[0]
tries = len(word)

while tries > 0:
    print("You have " + str(tries) + " tries left!")
    correct_guesses = 0 

    for char in word:
        if char in guesses:
            print(char, end=' ')
            correct_guesses += 1
        else:
            print("_", end=' ')

    if correct_guesses == len(word):  
        print("\nYou won the game!")
        break

    guess = input("\nEnter a character: ")

    if guess in word:
        guesses += guess
    else:
        tries -= 1

if tries <= 0:
    print("\nYou failed the game!")
