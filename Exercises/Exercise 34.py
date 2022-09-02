
#Even or Odd #Date 8/29/2022

'''
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.
'''

input_user = int(float(input("Please enter an integer")))
#print (input_user) # debug

if input_user % 2 == 1:
    print("That integer is odd")
else: 
    print("That integer is even")