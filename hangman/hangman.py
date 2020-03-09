from pathlib import Path
import random

print("*" * 20, "\nWelcome to Hangman...\n", "*" * 20, "\n\n", sep="")
attempts = 6

# getting the wordlist
word_path = Path("Python Basics/hangman/sowpods.txt")
word_list = word_path.read_text().split("\n")


def empty_word(word, word_sofar, letters=[], user_input=""):
    if len(letters) > 0:
        for index in letters:
            word_sofar[index] = user_input.upper()
    for i in word_sofar:
        print(i, end=" ")
    return word_sofar


def word_chooser():
    word = random.choice(word_list)
    return word


def get_input():
    return input("\n\nGuess the letter in the word: \n\n").lower()[0]


def word_finder(word, user_input):
    return [index for index, letter in enumerate(word) if letter == user_input]


def progress(word, word_sofar=[]):
    return word.lower() == "".join(word_sofar).lower()


word = word_chooser().lower()
word_sofar = list("_" * len(word))
empty_word(word, word_sofar)
while True:
    if progress(word, word_sofar):
        print("\n\nGreat !!!  You Won !!!\n\n")
        break
    user_input = get_input()
    word_check = word_finder(word, user_input)
    if len(word_check) > 0:
        word_sofar = empty_word(word, word_sofar, word_check, user_input)
    else:
        attempts -= 1
        if attempts == -1:
            print("\n\nYou are out of attempts. \n\nThe game is over \n\n")
            print(f"\n\nThe word was:  {word.upper()}")
            break
        else:
            print(
                f"\n\nThe letter is not in the word... \n\nAttempt remained = {attempts}\n\n")
        empty_word(word, word_sofar)
