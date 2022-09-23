'''
-----------------------------------------------
Python Project
Name:        Randomizer
License:     Free Version
Version:     1.0
Author:      Sayam Pradhan
Author Email: Sayampradhan07@outlook.com
----------------------------------------------- 
'''

# importing necessary modules
from random import choice

# take input to append the list of choices
List_of_Choices = []
num_of_elements = int(input("Write the number of choices you have: "))

for i in range(num_of_elements):
    UserInput = input("Write the choice: ")
    List_of_Choices.append(UserInput)

print("Your Choices are: ", List_of_Choices)

# print a random choice from the list
print("Let's go for", choice(List_of_Choices).upper())