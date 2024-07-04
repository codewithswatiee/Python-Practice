import random
from hangmanStages import logo, hangman_stages

print(logo)

word_list = ['PRODUCTIVE', 'EDUCATED', 'OFFER', 'CAGEY', 'LOCK', 'WIGGLY', 'PASS', 'UNHEALTHY', 'OSSIFIED', 'BEE', 'DIFFICULT', 'LIVE', 'SNOW', 'SAFE', 'FLAME', 'WHISPER', 'OBSOLETE', 'STEP', 'USEFUL', 'CHEAP', 'LEWD', 'SPOOKY', 'BLADE', 'SUBTRACT', 'COMMON', 'DECISIVE', 'SHOE', 'EXCITING', 'PANCAKE', 'IMPARTIAL', 'SHEEP', 'NAPPY', 'AGONIZING', 'SMALL', 'MARBLE', 'HELP', 'BREATH', 'AUTOMATIC', 'LOSS', 'KITTY', 'TRUST', 'CANNON', 'PASTE', 'VOLATILE', 'MARKET', 'DROP', 'PRICEY', 'TOP', 'BRAWNY', 'REJOICE', 'JOG', 'COWS', 'PATHETIC', 'SECRET', 'PAT', 'EMPTY', 'CRAVEN', 'BLOT', 'CLASSY', 'BLOW', 'FIVE', 'STATEMENT', 'BABY', 'DIVISION', 'BOILING', 'THUNDERING', 'PROVIDE', 'MAID', 'PRESERVE', 'ASHAMED', 'STROKE', 'CROWDED', 'PIE', 'CRASH', 'GIDDY', 'SUCCEED', 'GUARDED', 'ORGANIC', 'ZEALOUS', 'TRAMP', 'CALLOUS', 'HAPPY', 'PRACTICE', 'SUCCESSFUL', 'EDUCATE', 'BOIL', 'SUDDEN', 'CAT', 'TEAM', 'COMPARISON', 'SPIKY', 'MEN', 'TIN', 'SMOGGY', 'CROWD', 'MAILBOX', 'REQUEST', 'AHEAD', 'VIVACIOUS', 'SNAKES']

secret_word = random.choice(word_list)
length_word = len(secret_word)
blanks = []
for _ in range(length_word):
    blanks.append("_")
print(" ".join(blanks))

guessedLetters = []
lives = 6
defaultStage = hangman_stages[len(hangman_stages) - 1]
print(defaultStage)
end_game = False
while not end_game:
    guess = input("Guess a letter: ").upper()
    if guess in guessedLetters:
        print("You have already guessed this letter!")
        continue
    else:
        guessedLetters.append(guess)

    for position in range(length_word):
        letter = secret_word[position]
        if guess == letter:
            blanks[position] = letter
    if guess not in secret_word:
        lives -= 1
        print(f"You now have {lives} lives left.")
        print(hangman_stages[lives])

    if lives == 0:
        end_game = True
        print("You Lose!")
        break
    print(" ".join(blanks))
    if "_" not in blanks:
        end_game = True
        print("You win!!")

    if end_game:
        ask = input("Do you wanna play again? 'Y' or 'N'")
        if ask == "Y":
            secret_word = random.choice(word_list)
            blanks.clear()
            length_word = len(secret_word)
            blanks = []
            for _ in range(length_word):
                blanks.append("_")
            print(" ".join(blanks))
            end_game = False
            guessedLetters.clear()
            lives = 6
        else:
            print("See you next Time! BBYEEEEE")






