# # import math

# # r = int(input("Enter Radius: "))
# # area = math.pi * (r**2)
# # print(f"The area of circle is: {area:.2f}")


# # a = int(input("What is the first number? "))
# # b = int(input("What is the second number? "))
# # op = input("Pick operation from this list (+, -, *, /): ")

# # match op:
# #     case '+':
# #         print(f"{a} + {b} = {a + b}")
# #     case '-':
# #         print(f"{a} - {b} = {a - b}")
# #     case '*':
# #         print(f"{a} * {b} = {a * b}")
# #     case '/':
# #         if b != 0:
# #             print(f"{a} / {b} = {a / b}")
# #         else:
# #             print("Cannot divide by zero!")
# #     case _:
# #         print("Invalid Operator")

# # student_scores = [80, 60, 50, 65, 75, 55]

# # highest = student_scores[0]  # Initialize highest score with the first score
# # for score in student_scores:
# #     if score > highest:
# #         highest = score  # Update highest if a higher score is found
    
# # print(f"# The highest score in the class is: {highest}")


# # custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']

# # def integer(lis):
# #     for item in lis:
# #         if (isinstance(item, int)):
# #             print(f"This is an integer: {item}")
# #         if (not any(isinstance(item, int))):
# #             print(f"There are no integers in the list.")

# # integer(custom_list)

# # total =0
# # for i in range(1, 100):
# #     if(i%2 !=0):
# #         total += i

# # print(f"Sum of odd numbers is: {total}")

# # username = ""
# # while(username != 'test'):
# #     username = input("Enter username: ")

# # def numbers_divisible_byfive(p_list):
# #     for num in p_list:
# #         if num > 130:
# #             print("STOP")
# #             break
# #         if num % 5 == 0:
# #             print(num)


# # list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200] 
# # numbers_divisible_byfive(list1)

# # n = int(input( "Enter a number : "))
# # def fact(n):
# #     if n < 0:
# #         print("Factorial does not exist for negative numbers")
# #         return None
# #     elif n == 0 or n == 1:
# #         print(f"The factorial of {n} is 1")
# #     else:
# #         factorial = n * fact(n - 1)

# # fact(n)

# # for i in range(1, 101):
# #   if(i % 5 == 0):
# #     print("Fizz")
# #   if(i % 7 ==  0):
# #     print("Buzz")
# #   if(i % 5 == 0 and i % 7 == 0):
# #     print("FizzBuzz")

# # def sum_of_two_digits(a, b):
# #     return a+b
    
# # a = input("Enter two digit number: ")
# # result = sum_of_two_digits(int(a[0]), int(a[1]))
# # print(f"{a[0]} + {a[1]} = {result}")

# # string = input("Enter a string: ")
# # print(len(string))
# # i = len(string) -1
# # while i>= 0:
# #     print(string[i])
# #     i =i - 1

# # def count_letter(word, letter):
# #     for char in word:
# #         return word.count(letter)
    
# # word = input("Enter a word: ")
# # letter = input("Enter the letter: ")
# # print(count_letter(word, letter))

# # def first_last_characters(word):
# #     if len(word)<=2:
# #         return ""
# #     else:
# #         newWord = word[:2] + word[len(word)- 2 :]
# #         return newWord

# # print(first_last_characters("asdfghjkl"))

# # custom_string = 'I love Python.' 

# # custom_string = custom_string.replace(".", "!")
# # print(custom_string)

# # custom_string = 'X-MAPDS-Confidence:0.8475' 
# # after_colon = custom_string.find(":")

# # new_string = custom_string[after_colon+1:]
# # print(float(new_string))

# # def print_pattern(n):
# #     string = "*"
# #     for i in range(1, n+1):
# #         print(string*i)
    
# #     for i in range(n-1, 0, -1):
# #         print(string*i)

# # print_pattern(5)

# # def print_star_pattern(n):
# #     for i in range(1, n + 1):
# #         # Print stars for the current row
# #         stars = '*' * i
# #         # Use string formatting to center-align the stars and print
# #         print("{:^{}}".format(stars, n * 2))

# # # Test the function with n = 5
# # print_star_pattern(5)

# # custom_list = [1,2,3,4,5]
# # def square_list(p_list):
# #     for i in range(len(p_list)):
# #         p_list[i] = p_list[i] ** 2
# #     return p_list
    

# # square_list(custom_list)
# # print(custom_list)

# # custom_list = [1,2,3,4,5,6,7,8,9,10]
# # print(custom_list[-1: 0: -1])



# # list1 = [10, 10, 5, 15, 50, 50, 20]

# # index = list1.index(50)
# # list1[index] = 5
# # print(list1)



# # def count_words(p_list):
# #     count = 0
# #     for word in p_list:
# #         if len(word)>= 2:
# #             if word[0] == word[len(word)-1]:
# #                 count += 1
# #     return count
    


# # list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
# # print(count_words(list1))

# # list_one = [4, 12, 16, 21, 24, 28, 32]
# # list_two = [5, 10, 15, 20, 25, 30, 35]


# # def oddIndec(somelist):
# #     newlist = []
# #     for i in range(0,  len(somelist)):
# #         if (i % 2 != 0):
# #             newlist.append(somelist[i])
# #     return newlist
            

# # def evenIndec(somelist):
# #     newlist = []
# #     for i in range(0,  len(somelist)):
# #         if (i % 2 == 0):
# #             newlist.append(somelist[i])
# #     return newlist


# # list_one = oddIndec(list_one)
# # list_two = evenIndec(list_two)
# # list_final = list_one + list_two
# # print(list_final)


# # custom_list = [10, 44, 57, 99, 11, 33, 84]
# # for item in custom_list:
# #     index = custom_list.index(11)
# # del custom_list[index]
# # custom_list.insert(2, 11)
# # custom_list.append(11)
# # print(custom_list)

# # sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]

# # chunk1 = sample_list[:3]
# # chunk2 = sample_list[3:6]
# # chunk3 = sample_list[6:len(sample_list)]

# # print(f"Chunk-1 = {chunk1[::-1]}")
# # print(f"Chunk-2 = {chunk2[::-1]}")
# # print(f"Chunk-3 = {chunk3[::-1]}")

# # custom_list = [1, 2, 3, 4, 5]
# # custom_string = " | ".join(str(element)  for element in custom_list)
# # print(custom_string)

# # list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# # list1[2][2].insert(1, 7000)

# # print(list1)

# # list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# # sublist= ["h", "i", "j"]
# # list1[2][1][2].extend(sublist)
# # print(list1)

# # def addItem(somelist, item):
# #     newlist = somelist.copy()
# #     newlist.append(item)
# #     return newlist

# # list1 = [1,2,3,4,5]
# # list2 = addItem(list1, 6)
# # print(list1)
# # print(list2)

# # list1 = ["Hello ", "take "]
# # list2 = ["Dear", "Sir"]

# # def concatenation(list1, list2):
# #     newlist = []
# #     for items1 in list1:
# #         for items2 in list2:
# #             newlist.append(items1 + items2)
# #     return newlist


# # print(concatenation(list1, list2))

# # def generate_dictionary(n):
# #     dictionary = {}
# #     for i in range(1, n+1):
# #         dictionary[i] = i**2
# #     return dictionary

# # sample = generate_dictionary(5)
# # print(sample)

# # my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}

# # def multiply_values(dictionary):
# #     total = 1
# #     for key in dictionary:
# #         total *= dictionary[key]
# #     print(total) 
# # multiply_values(my_dict)



# # Scores 85 - 100: Grade = "Outstanding"
# # Scores 65 - 84: Grade = "Good"
# # Scores 50 - 64: Grade = "Acceptable"
# # Scores 50 lower: Grade = "Fail"

# # student_scores = {
# #   "John": 90,
# #   "Edy": 68,
# #   "Marry": 88, 
# #   "Ewan": 79,
# #   "Park": 62,
# # }

# # def convert_grade(dictionary):
# #     for key in dictionary:
# #         if dictionary[key] > 84:
# #             dictionary[key] = "Outstanding"
# #         elif 65 <= dictionary[key] <= 84:
# #             dictionary[key] = "Good"
# #         elif 50 <= dictionary[key] < 65:
# #             dictionary[key] = 'Acceptable'
# #         else:
# #             dictionary[key] = "Fail"
# #     return dictionary

# # print(convert_grade(student_scores))
    



# # my_dict = {
# #     "name": "Edy",
# #     "age":30, 
# #     "salary": 5000, 
# #     "city": "London"
# # }

# # my_dict["address"] = my_dict["city"]
# # del my_dict["city"]
# # print(my_dict)
        

# # def count_character(string):
# #     dictionary = {}
# #     for char in string:
# #         dictionary[char] = string.count(char)
# #     return dictionary

# # print(count_character("BABACDAS"))


# # programming_language = [
# #     {"user_name" : "Elshad",
# #      "favorite_languages" : ["Python", "Java", "C#"],
# #      "experience": 10 
# #     },
# #     {"user_name":"Renad",
# #      "favorite_languages" : ["Scratch","Python"],
# #      "experience" : 2
# #     },
# # ]
    


# # def add_new_user(name, list, num):
# #     dictionary = {}
# #     dictionary["user_name"] = name
# #     dictionary["favorite_languages"] = list
# #     dictionary["experience"] = num
# #     return programming_language.append(dictionary)

# # add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10)
# # print(programming_language)

# # custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
# # def group_types(somelist):
# #     dictionary = {}
# #     for items in somelist:
# #         if isinstance(items, str):
# #             dictionary[items] = "String"
# #         elif isinstance(items, int):
# #             dictionary[items] = "Integer"
# #         elif isinstance(items, bool):
# #             dictionary[items] = "Boolean"
# #         else:
# #             dictionary[items] = "Other"
# #     print(dictionary)
# # group_types(custom_list)

# # names_dict = {
# #     1: "Elshad",
# #     2: "Renad",
# #     3: "Johanna",
# #     4: "Appmillers"
# # }

# # def value_length(dictionary):
# #     new_dict = {}
# #     for key, value in dictionary.items():
# #         new_dict[key] = {value: len(value)}
# #     print(new_dict)

# # value_length(names_dict)

# # dict1={1: "one", 2: "two"}
# # dict2={3: "three", 4: "four"}
# # dict3={5: "five", 6: "six"}
 
# # def concatenate(d1, d2, d3):
# #     d1.update(d2)
# #     d1.update(d3)
# #     return d1
# # result = concatenate(dict1,dict2,dict3)
# # print(result)

# # custom_dict = {
# #     "name" : "Elshad",
# #     "age" : 28,
# #     "city" : None
# # }
# # def remove_empty_items(dictionary):
# #     new_dict = {}
# #     for key, value in dictionary.items():
# #         if value is not None:
# #             new_dict[key] = value
# #     print(new_dict)

# # remove_empty_items(custom_dict)

# # dict1 = {'One': 2, 'Two': 2, 'Three': 3}
# # dict2 = {'Three': 3, 'Four': 4, 'Five': 5}
# # def merge_dict(d1, d2):
# #     d1.update(d2)
# #     print(d1)
# # merge_dict(dict1, dict2)


# # import copy
# # original_dict = {
# #     "names" : ["Elshad", "John", "Edy"],
# #     "numbers" : [1,2,3,4,5]
# # }
# # def deep_copy(dictionary):
# #     return copy.deepcopy(dictionary)
# # copied_dict = deep_copy(original_dict)
# # copied_dict["names"].append("Jack")
# # copied_dict["numbers"].append(6)
 
# # print(original_dict)
# # print(copied_dict)

# # def even_index_items(p_tuple):
# #     list = []
# #     for index, value in enumerate(p_tuple):
# #         if index % 2 == 0:
# #             list.append(value)
# #     tupple = tuple(list)
# #     print(tupple)


# # my_tuple = ("a", "b", "c", "d", "e", "f", "g")
# # even_index_items(my_tuple)


# # my_tuple = ("a","b","c","d","e","a","c","e","b","e","c","a","f","e","r")
# # def most_frequent(p_tuple):
# #     count = []
# #     list = []
# #     for value in p_tuple:
# #         num = p_tuple.count(value)
# #         count.append(num)
# #     maxCount = max(count)
# #     index = p_tuple[maxCount]
# #     list.append(index)
# #     list.append(maxCount)
# #     return tuple(list)

# # new_tuple = most_frequent(my_tuple)
# # print(new_tuple)
    

# # clubs = (("FC Barcelona", "Spain", 1899,
# #             [
# #                 (3, "Pique"),
# #                 (5, "Busquets"),
# #                 (7, "Dembele"),
# #             ]
# #          ),
# #          ("Real Madrid CF", "Spain", 1902,
# #             [
# #                 (7, "Hazard"),
# #                 (9, "Benzema"),
# #                 (10, "Modric"),
# #             ]
# #          ),
# #          ("Manchester United FC", "England", 1878,
# #             [
# #                 (6, "Pogba"),
# #                 (7, "Ronaldo"),
# #                 (14, "Lingard"),
# #             ]
# #          ),
# #          ("Arsenal FC", "England", 1886,
# #             [
# #                 (7, "Lacazette"),
# #                 (14, "Aubameyang"),
# #                 (16, "Holding"),
# #             ]
# #          ),
# #          )

# # player = clubs[3][3][0][1]
# # print(player)

# # year = clubs[2][2]
# # print(year)

# # squad = clubs[0][3][2][0]
# # print(squad)

# # secPlayer = clubs[1][3][1]
# # print(secPlayer)

# # def adding_set(somelist):
# #     set1 = set(())
# #     set1.update(somelist)
# #     return set1

# # my_list = [3,4,5,1,1,3,4,9,8]
# # createdSet = adding_set(my_list)
# # print(createdSet)

# # my_list = ["apple", "apple", "orange", "grape", "grape", "orange", "apple"]

# # def removeDup(someList):
# #     set1 = set((someList))
# #     return set1

# # createdSet = removeDup(my_list)
# # print(createdSet)

# general_items = {
#     "Sand toys",
#     "Beach towels",
#     "Beach umbrella",
#     "Camp chair",
#     "Snacks",
#     "Hats",
#     "Camera",
#     "Sunglasses",
#     "Alcholic Drinks",
#     "Non Alcholic Drinks",
#     "Sigarettes",
#     "Sharp Objects"
# }

# restricted_items = {
#     "Alcholic Drinks",
#     "Sigarettes",
#     "Sharp Objects",
#     "Amplified Audio",
#     "Drugs"
#     }

# beachType = input("Select Beach Type (1 - Family beach, 2 - Normal Beach): ")
# if beachType == '1':
#     for items in  restricted_items:
#         general_items.discard(items)
# else:
#     general_items.discard("Drug")


# print("See below the list of items that you can take.")
# for items in general_items:
#     print(items)


# set1 = {10,20,30,40,50}
# set2 = {60,20,50,70}

# def setUnion(s1, s2):
#     s3 = set(())
#     s3 = s1.union(s1)
#     return s3


# set3 = setUnion(set1, set2)
# print(set3)


# list_of_sets = [
#     {10,20,30,40,50},
#     {"apple", "orange","limon","pear"},
#     {"London", "Berlin", "Paris"},
#     {"Python", "Java", "Swift"},
#     {10, "ten", "20", 20}
# ]

# def divisible_by_3and4(n):
#     s1 = set(())
#     s2 = set(())
#     s3 = set(())
#     for i in range(n+1):
#         if i  % 3 == 0:
#             s2.add(i)
#         if i % 4 == 0:
#             s3.add(i)
#     s1 = s2.intersection(s3)
#     print(s1)

# divisible_by_3and4(100)
        

# def convert_ls(somelist):
#     someset = set(())
#     for items in somelist:
#         for item in items:
#             someset.add(str(item))
#     print(someset)

# convert_ls(list_of_sets)


# quote = """Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do."""
# prep = {"as", "but", "by", "for", "in", "of", "on", "to", "with"}
 

# def find_prep(somequote):
#     s1 = set(())
#     words = somequote.split(" ")
#     for word in words:
#         if word.lower() in prep:
#             s1.add(word)
#     print(s1)
# find_prep(quote)


# a = {1, 2, 3, 40, 50, 300, 400}
# b = {10, 20, 30, 40, 300}
# c = {100, 200, 300, 400}

# def diff(s1, s2, s3):
#     s4 = s1 - s2- s3
#     print(s4)

# diff(a, b, c)


# def fib_recursive(n, fib):
#     if n <= 1:
#         fib.append(n)
#     else:
#         fib_recursive(n-1, fib)
#         fib_recursive(n-2, fib)

# fib = []
# fib_recursive(50, fib)
# print(fib)
  


# def sum_list(somelist):
#     total = 0
#     if len(somelist) == 1:
#         return somelist[0]
#     else:
#         total = somelist[0] + sum_list(somelist[1:])
#         return total

# print(sum_list([1, 2, 3, 4, 5]))

# def power(num, n):
#     if n <= 1:
#         return num
#     else:
#         return num * power(num, n-1)


# print(power(2, 4))

# def sum_positive(n):
#     if n <= 0:
#         return n
#     else:
#         return n + sum_positive(n-2)
    
# print(sum_positive(10))

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the solve function below.
# def solve(s):
#     w = s.split(' ')
#     for i in range(len(w)):
#         w[i] = w[i].capitalize()
#     for i in range(len(w)):
#         print(w[i] + "", end=' ')

# # Example usage:
# solve("hello world")


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = solve(s)

#     fptr.write(result + '\n')

#     fptr.close()


# string  = 'swati verma'
# def solve(s):
#     w = s.split(' ')
#     for i in range(len(w)):
#         w[i] = w[i].capitalize()
#     w = ' '.join(w)
#     print(w)


# solve(string)

# def minion_game(string):
#     VOWELS = ['A', 'E', 'I', 'O', 'U']
#     player1 = 0
#     player2 = 0
#     substrings = []
#     n = len(string)
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             substrings.append(string[i:j])
#     for sub in substrings:
#         if sub[0] in VOWELS:
#             player1 += 1
#         else:
#             player2 += 1
#     if player1 > player2:
#         print(f"Kevin {player1}")
#     elif player1 < player2:
#         print(f"Stuart {player2}")
#     else:
#         print("Draw")
#     return 

# string = input()
# winner = minion_game(string)

# def minion_game(string):
#     player1 = 0  # Kevin's score
#     player2 = 0  # Stuart's score
#     n = len(string)
#     for i in range(n):
#         # Count substrings starting from i
#         if string[i] in "AEIOU":
#             player1 += n - i  # All substrings from i to end
#         else:
#             player2 += n - i  # All substrings from i to end

#     if player1 > player2:
#         print(f"Kevin {player1}")
#     elif player1 < player2:
#         print(f"Stuart {player2}")
#     else:
#         print("Draw")

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)

import re

ro = re.compile(r'\d\d\d')

print('ro:', ro)



