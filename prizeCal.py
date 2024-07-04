available_parts = {
    1: "computer",
    2: "monitor",
    3: "keyboard",
    4: "mouse",
    5: "hdmi cable",
    6: "dvd drive",
    0: "to finish"
}

price_quantity ={
    "computer" : {"price": 500, "quantity" : 10},
    "monitor" : {"price": 200, "quantity" : 8},
    "keyboard" : {"price": 500, "quantity" : 5},
    "mouse" : {"price": 10, "quantity" : 0},
    "hdmi cable": {"price": 20, "quantity" : 7},
    "dvd drive" : {"price": 50, "quantity" : 5},
}

def askUser():
    print("Please select an option from the list or enter 0 to finish:")
    for key, value in available_parts.items():
        print(f"{key}: {value}")
    selected_items = []
    total = 0
    while True:
        inp = input(">> ")
        if inp == "0":
            break
        elif int(inp) in available_parts:
            selected_item = available_parts[int(inp)]
            selected_items.append(selected_item)
            if selected_item in price_quantity:
                if price_quantity[selected_item]["quantity"] > 0:
                    print(f"Added {selected_item} to your selection.")
                    total += price_quantity[selected_item]["price"]
                else:
                    print("Item out of stock")
        else:
            print("Invalid option. Please try again.")
    return total

result = askUser()
print(f"Your Total is {result}. Thank you!")





