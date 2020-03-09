import random
import time


def computer_guess():
    return random.randrange(1, 3)


def game_engine(user, comp):
    result = user - comp
    if result == -2 or result == 1:
        return "You Won! Hurray!"
    else:
        return "Sorry! computer Won!"


def quit():
    print("alright! See you later...")
    time.sleep(2)


def entered(user):
    if user == 1:
        return "rock"
    elif user == 2:
        return "paper"
    else:
        return "scissors"


def game_itself():
    while True:
        user = int(
            input("choose \n1. Rock, \n2. Paper\n3. scissors: \n4. Quit\n"))
        if user == 4:
            quit()
            break
        comp = computer_guess()
        print(f"You entered {entered(user)}")
        print(f"Computer entered {entered(comp)}")
        print("*" * 10)
        print(game_engine(user, comp))


print("Wlecome to rock paper scisorrs : ")
print("choose Difficulty : \n 1. Easy \n 2. Medium \n 3. Hard")
difficulty = int(input("enter 1, 2 or 3: \n"))
print("alright here we go...")
time.sleep(1)
game_itself()
