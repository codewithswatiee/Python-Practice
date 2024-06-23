import random

question_answer = {
    "A mapping from a set of keys to their corresponding values." : "Dictionary",
    "Another name for a key-value pair." : "Item",
    "An object that appears in a dictionary as the first part of a key-value pair." : "Key",
    "An object that appears in a dictionary as the second part of a key-value pair." : "Value",
    "A loop “inside” of another loop." : "Nested doop",
    "A dictionary that is an element of another dictionary." : "Nested dictionary",
}

question = list(question_answer.keys())
lives = 2


n = int(input("How many players are there? "))
for i in range(1, n+1):
    askPlayerName = input(f"Enter player {i} name: ")
# turns
for i in range(1, n+1):
    print(f"Player {i} turn: ")
    playerquestion = random.choice(question)
    print(f"And the question is -> {playerquestion}")
    while lives > 0:
        playerAns = input("Your Answer: ").capitalize()
        # for question in question_answer.items():
        if question_answer[playerquestion] == playerAns:
                print("Correct Guess")
                break
        else:
            lives = lives - 1
    if lives == 0:
        print("You lose!!")
        




