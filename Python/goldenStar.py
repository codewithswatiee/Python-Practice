import random

star = "🌟"
crossedBox = '⌧'

def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))

map1 = [["⬜️","⬜️","⬜️"],["⬜️","⬜️","⬜️"],["⬜️","⬜️","⬜️"]]
print("This is our initial map...")
print_map(map1)

map_copy = map1.copy()


sublist_index = random.randint(0, len(map_copy)-1)
sublist = map_copy[sublist_index]
position = random.randint(0, len(sublist) - 1)

position_of_star = (sublist_index, position)



def change_to(some_list, position, item):
    row, col = position
    some_list[row][col] = item
    print_map(some_list)

position_by_user = input("Guess the position of star (2 digits - 1st for row and 2nd for col): ")

row_guess, col_guess = int(position_by_user[0]), int(position_by_user[1])

if (row_guess, col_guess) == position_of_star:
    change_to(map1, position_of_star, star)
else:
    change_to(map1, (row_guess, col_guess), crossedBox)
