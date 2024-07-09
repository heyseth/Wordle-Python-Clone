import os
import random

# open a list of words and choose a random one to be the secret word
with open("wordlist.txt", "r") as file:
    wordlist = file.readlines()
# convert the secret word to uppercase
secret_word = random.choice(wordlist).strip().upper()

# create a list to store the guesses and a variable to store the maximum number of guesses
guesses = []
max_guesses = 6
# create a blank word to display to the user
blank_word = "_" * len(secret_word)
for i in range(max_guesses):
    guesses.append(blank_word)

# create variables to store the current guess number, whether the game has ended, and any extra output
current_guess = 0
game_end = False
extra_output = ""

# main game loop
while True:
    # clear/refresh the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # print the previous guesses along with the output from the current guess
    print("\n".join(guesses) + extra_output)

    # check if the game has ended, if it has, terminate the program
    if game_end:
        break

    # get user input and convert it to uppercase
    user_input = input("Enter guess: ").upper()
    output_guess = list(user_input)

    # keep track of the letters that have been guessed and how many times they have been guessed
    guessed_letters = []

    # check if the input is letters only
    if user_input.isalpha():
        # check if the length of the guess matches the secret word
        if len(user_input) == len(secret_word):

            # first loop through the word looking only for letters in the correct space
            for idx, letter in enumerate(user_input):
                # if letter is in the right place
                if letter == secret_word[idx]:
                    # add the letter to the list of guessed letters and highlight it in green
                    guessed_letters.append(letter)
                    output_guess[idx] = "\033[42m" + letter.upper() + "\033[0m"

            # second loop through the word looking for letters that are in the word but not in the right place
            for idx, letter in enumerate(user_input):
                # if letter is in the word but not in the right place
                if letter in secret_word and letter != secret_word[idx]:
                    # if the letter has been guessed less times than it occurs in the word
                    if guessed_letters.count(letter) < secret_word.count(letter):
                        # add the letter to the list of guessed letters and highlight it in yellow
                        guessed_letters.append(letter)
                        output_guess[idx] = "\033[43m" + letter.upper() + "\033[0m"

            # all other letters are left with no highlight

            # add the guess to the list of past guesses and increment the number of guesses made
            guesses[current_guess] = "".join(output_guess)
            current_guess += 1

            # if user has guessed the word, end the game
            if user_input == secret_word:
                extra_output = "\n\033[92mCongratulations! You have guessed the word.\033[0m"
                game_end = True
            # if user has run out of guesses, end the game
            elif current_guess == max_guesses:
                extra_output = "\n\033[91mYou have run out of guesses. The word was " + secret_word + ".\033[0m"
                game_end = True
            # otherwise, no additional output
            else:
                extra_output = ""
            
        else:
            # if the guess is not the correct length, provide an error message
            extra_output = "\n\033[91mInvalid input. Your guess must be " + str(len(secret_word)) + " letters long.\033[0m"
    else:
        # if the guess contains non-letter characters, provide an error message
        extra_output = "\n\033[91mInvalid input. Your guess must contain letters only.\033[0m"