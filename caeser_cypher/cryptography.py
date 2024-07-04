alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def refractor(position, cypherType):
    if cypherType == 'E':
        while position > 25:
                position = position - 26
    else:
        while position < 0:
                position = position + 26
    return position


def ceiserCypher(message, shiftNo, cypherType):
    final_text = ""
    if cypherType == 'D':
        shiftNo *= -1
    for char in  message:
        if char in alphabet:
            index = alphabet.index(char)
            position =  index + shiftNo
            position = refractor(position, cypherType)
            final_text += alphabet[position]
        else:
            final_text += char
    print(f"Here is the {'decode' if cypherType == 'D' else 'encode'} result: {final_text}")





from logo import logo
print (logo)



end_message = False
while not end_message:
    action = input("For encryption enter 'E' and for decryption  enter 'D': ")
    message = input("Enter your message:\n").upper()
    shift_number = int(input("Enter the shift number:\n"))
    ceiserCypher(message,shift_number,action)
    nextStep = input("Enter 'Y' to continue and 'N' to exit: ")
    if  nextStep == "N":
        end_message = True
        print("See you Next Time!")


