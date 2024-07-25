#rock paper sissors game

import random

options = ['rock','paper','scissors']
while True:
    repley = input("Lets play rock paper scissors! \nWhat do you choose?")
    repley = repley.lower()
    answer = random.choice(options)

    while repley not in options:
        repley = input("rock , paper or scissors!".upper())
    
    sun = ""
    if answer == repley:
        sun = "no one"
    elif answer == "rock":
        if repley == "paper":
            sun = "you"
        else:
            sun = "I"
    elif answer == "paper":
        if repley == "scissors":
            sun = "you"
        else:
            sun = "I"
    elif answer == "sissors":
        if repley == "rock":
            sun = "you"
        else:
            sun = "I"
    print(f"I choosed {answer}.\nLooks like {sun} won")
    con = input("would you like to play again?\nYes or no?".lower())
    if con == "no":
        print("Bye! It was fun while it lasted!")
        break


    