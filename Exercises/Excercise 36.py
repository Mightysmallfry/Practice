
# Vowel or Consonant #Date 8/29/2022
'''
In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.
'''


Vowels = ["a", "e", "i", "o", "u"]

user_input = input("Please enter a letter of the alphabet and I will tell you if they are a consonant or vowel.").casefold().strip()


for letter in Vowels:
    if user_input == letter:
        print("This letter is a vowel.")
    if user_input == "y":
        print("Sometimes y is a vowel, and sometimes y is a consonant.")
    else:
        print("This letter is a consonant.")
