
import numpy as np
import matplotlib.pyplot as plt

def main_menu():
    print("Please select a province to analyze by inputting the corresponding number:\n1. Alberta\n2. British Columbia\n")
    user_province = input(">> ")

    if user_province == "1" or user_province == "2":
        return user_province
    else:
        return 0
    
def options_menu():
    print("Please select a biomass category to display by inputting the corresponding number:\n")
    print("\t1. Forestry Biomass\n\t2. Agricultural Biomass\n\t3. Livestock Residue\n\t4. Urban Waste")
    user_first_choice = input(">> ")

    if user_first_choice == "1" or user_first_choice == "2" or user_first_choice == "3" or user_first_choice == "4":
        return user_first_choice
    else:
        return 1

print("Welcome to the Biomass Potentials and Drivers Tool!\n")

while True:
    user_province = main_menu()
    
    while user_province == 0:
        print("Invalid input, please try again.")
        user_province = main_menu()

    user_choice_one = options_menu()
    
    while user_choice_one == 1:
        print("Invalid Input, please try again")
        user_choice_one = options_menu()
    
