import random

fiveNumbers = set(())

userInput = input("Enter 5 different numbers from 1 to 69, with spaces between each number. (For example: 5 17 23 42 50) \n")

def getRandomno():
    s2 = set()
    for i in range(5):
        rand = random.randint(1, 70)
        s2.add(rand)
    return s2

def powerballNo():
    rand = random.randint(1, 27)
    return rand

numbers = userInput.split(" ")
for num in numbers:
    fiveNumbers.add(int(num))
    if int(num) not in range(1, 70):
        print("Enter a number between 1 to 69")
        exit()

userPowerBall = int(input('Enter the powerball number from 1 to 26.\n'))
if userPowerBall not in range(1, 27):
    print("Enter a number between 1 to 26")
    exit()

lives = int(input("How many times do you want to play? (Max: 1000000)"))
print(f"It costs ${2*lives} to play {lives} times, but don't worry. I'm sure you'll win it all back.")
print("Press Enter to start...")
input()

def winorlose():
    global win
    win = 0
    for num in fiveNumbers:
        if num in getRandomno():
            win += 1
    if powerballNo() == userPowerBall:
        win += 1

while lives > 0:
    print(f"The winning numbers are: {getRandomno()} and {powerballNo()}")
    winorlose()
    if win == 2:
        print("You win!")
    else:
        print("Better luck next time.")
    lives -= 1
    
