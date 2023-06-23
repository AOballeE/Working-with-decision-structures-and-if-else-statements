# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 00:17:40 2022

@author: Aldo
"""

# declare the varibales and accumulator 
pizzas = "cheese, pepperoni, and supreme"
keep_going = 'y' or 'Y'
pizza_number = 0

# Prompt the user to ask their name.
name = input("Enter your name here: ")


# Print the users name along with "Hello [insert name]. Welcome to the 
# python pizza chooser.
print("Hello", name,"Welcome to the python pizza chooser.")


# Print another statement ask the user which type of pizza they want.
pizza_choice = input('What type of pizza would you like, we have cheese,' +
                     ' pepperoni, and supreme? ')
pizza_number += 1
# Enter while loop
while keep_going.lower() == input("Okay! Would you like to order another " +
                                  "pizza? Enter y for yes and n for no: "):
    # Enter conditioal statement
    if keep_going.lower() == 'y':
        pizza_number += 1
        pizza_choice = input('What type of pizza would you like,' +
                             'we have cheese, pepperoni and supreme? ')
        if keep_going.lower() == 'no':
            break
print("Thank you",name,".The", pizza_number, "pizza(s) you ordered will" +
      " be ready in 30 minutes.")
        
# End of program 

# I'm going to be honest, I tried for so long to use the .lower from examples 
# and from my notes but I could not get it to work no matter
# how much I tried but the 'y' does work if you enter it in lowercase when 
# answering.
        

        
        