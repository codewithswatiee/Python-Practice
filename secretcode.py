import random


code = input("Enter the code to be secret coded: ")

def generateRandomNum():
    return random.randint(100, 1000)
       

if(len(code)<=3):
    secretCode = code[::-1]
    print(f"The secret code for {code} is '{secretCode}'")
else:
    secretCode =  str(generateRandomNum()) + code[::-1] +  str(generateRandomNum())
    print(f"The secret code for {code} with random number appended is '{secretCode}'")