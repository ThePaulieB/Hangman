!pip install random-word
import random
from random_word import RandomWords

score = {"win": 0, "lost": 0}

def getword():
  global secret_word
  r = RandomWords()
  secret_word = r.get_random_word()

def intro():
    print("\nH A N G M A N")


def show_menu():
    while True:
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        action = input()
        if action == "play":
            play_game()
        elif action == "results":
            show_results()
        elif action == "exit":
            break
        else:
            continue


def get_word_to_guess():
    return list(random.choice(words))


def validate_input(user_input, input_letters):
    if len(user_input) != 1:
        print("Please, input a single letter.")
        return False
    elif not user_input.isalpha() or user_input.isupper():
        print("Please, enter a lowercase letter from the English alphabet.")
        return False
    elif user_input in input_letters:
        print("You've already guessed this letter.")
        return False
    else:
        input_letters.append(user_input)
        return True


def show_guessed_letters(letter, word_to_guess, guessed):
    for i in range(len(word_to_guess)):
        if word_to_guess[i] == letter:
            guessed[i] = letter

    return guessed


def evaluate_result(guessed):
    global secret_word
    if "-" in guessed:
        score["lost"] += 1
        print()
        print(f"You lost! The word was {secret_word}")
        getword()
    else:
        score["win"] += 1
        result = "".join(guessed)
        print()
        print(f"You guessed the word {result}!")
        print("You survived!")
        getword()


def play_game():
    global secret_word
    input_letters = []
    word_to_guess = secret_word
    guessed = ["-"] * len(word_to_guess)
    allowed_mistakes = 8
    while allowed_mistakes > 0:
        print()
        print("".join(guessed))
        print(f"{allowed_mistakes} tries left! Input a letter:")
        letter = input()
        if not validate_input(letter, input_letters):
            continue
        elif letter in word_to_guess:
            guessed = show_guessed_letters(letter, word_to_guess, guessed)
            if "-" not in guessed:
                break
        else:
            allowed_mistakes -= 1
            print(f"That letter doesn't appear in the word.")

    evaluate_result(guessed)


def show_results():
    print(f'\nYou won: {score["win"]} times')
    print(f'You lost: {score["lost"]} times\n')


intro()
show_menu()