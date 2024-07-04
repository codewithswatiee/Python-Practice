# import time 

# timestamp1 = '23:59:09'

# if('4'<=timestamp1[0]< '12'):
#     print("Good morning!")
# elif(timestamp1[0] == '0'):
#     print("It's midnight.")
# elif('12'<= timestamp1[0]< '16'):
#     print("Good afternoon.")
# else:
#     print("Good evening!")

print("Welcome to Burger King!")
size = input("What size Burger do you want?'M' 'N' 'L': ")
mushroom = input("Do you want Mushrooms? 'Y' 'N': ")
mushroomSize = input("Mini/Normal or Large: ")
extraCheese = input("Do you want extra cheese? 'Y' 'N': ")

bill = 0 

if size := 'M':
    bill = bill + 5
    if mushroom := 'Y':
        if mushroomSize := 'Mini/Large':
            bill = bill + 1
        else:
            bill = bill + 2
    else:
        bill = bill + 0
    
    if extraCheese := 'Y':
        bill = bill + 1
    else: 
        bill = bill + 0
    
    print(f"Your final bill is ${bill}")
elif size := 'N':
    bill = bill + 8
    if mushroom := 'Y':
        if mushroomSize := 'Mini/Large':
            bill = bill + 1
        else:
            bill = bill + 2
    else:
        bill = bill + 0
    
    if extraCheese := 'Y':
        bill = bill + 1
    else: 
        bill = bill + 0
    
    print(f"Your final bill is ${bill}")
else:
    bill = bill + 10
    if mushroom := 'Y':
        if mushroomSize := 'Mini/Large':
            bill = bill + 1
        else:
            bill = bill + 2
    else:
        bill = bill + 0
    
    if extraCheese := 'Y':
        bill = bill + 1
    else: 
        bill = bill + 0
    
    print(f"Your final bill is ${bill}")
    
    



