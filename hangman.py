import numpy as np
import random

incorrectGuesses = 5
currentGuesses = 0
usedLetters = []
isAlive = True

wordlist = ["wave", "playing", "vancouver", "melissa", "science"]
selectedWord = wordlist[random.randint(0,len(wordlist)-1)]
hangmanList = list("_"*len(selectedWord))

def print_list(separator, printable_list):
    print(separator.join(printable_list))

def validate_guess(letter):
    letter = letter.strip().lower()

    if len(letter) != 1:
        return False, "Please enter a single letter."
    if not letter.isalpha():
        return False, "Please enter a valid letter (A-Z)."

    return True, letter


print_list(" ", hangmanList)

while isAlive:
    if hangmanList != list(selectedWord):
        if incorrectGuesses > currentGuesses:
            print(f"You have {incorrectGuesses-currentGuesses} guesses left.")

            guess = input("Guess a letter: ")
            is_valid, result = validate_guess(guess)

            if not is_valid:
                print(f"{result}")
                continue

            guess = result

            if guess in usedLetters:
                print("You've already guessed that letter.")
                continue

            else:
                usedLetters.append(guess)

                if guess in list(selectedWord):
                    wordArray = np.array(list(selectedWord))
                    indexes = np.where(wordArray == guess)[0]

                    for i in indexes:
                        hangmanList[i] = guess
                else:
                    currentGuesses += 1
                print_list(" ", hangmanList)
                print("Guessed letters: ", ", ".join(usedLetters))
        else:
            print("You lost, the word was", selectedWord)
            isAlive = False
    else:
        print("You won!")
        break
