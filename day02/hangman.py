import random


def game():
    with open("words.txt", "r") as file:
        line = file.readlines()

    content = random.choice(line).strip().lower()
    file.close()
    lives = 6

    wrong_letters = []
    good_letters = []

    def display_word():
        displayed_word = ""

        for letter in content:
            if letter in good_letters:
                displayed_word += letter
            else:
                displayed_word += "_"

        return displayed_word

    def loop():
        current_word = display_word()
        print(f"Current word: {current_word}")
        if current_word == content:
            print("You win")
            exit()
        guess = str(input("Enter letter: "))

        found = False

        for x in content:
            if guess == x:
                print("Good Job")
                for index, letter in enumerate(content):
                    if letter == guess:
                        good_letters.append(guess)

                loop()

                found = True

        if not found:
            wrong_letters.append(guess)
            nonlocal lives
            lives -= 1
            print(f"Wrong: {wrong_letters}", f" You have {lives} lives left")
            if lives > 0:
                print("Try Again")
                loop()
            elif lives <= 0:
                print("You lose the game")
                print("-----------------------")
                restart = str(input("Would you like to play again?: "))
                restart.lower()
                if restart == "yes":
                    game()
                elif restart == "no":
                    exit()

    loop()


game()
