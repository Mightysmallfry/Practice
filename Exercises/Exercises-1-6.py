

'''
==================== ATTENTION ====================

Each function will be counted as a seperate exercise for this file

'''


def mailing(): #Date: 8/29/2022
	'''
	Exercise 1: Mailing Address 
	Create a program that displays your name and complete mailing address formatted in
	the manner that you would usually see it on the outside of an envelope. Your program
	does not need to read any input from the user.
	'''
	
	print("Jonathan Marien")
	print("1750 211th PL NE")


def hello(): #Date: 8/29/2022
	'''
	Write a program that asks the user to enter his or her name. The program should
	respond with a message that says hello to the user, using his or her name.
	'''
	
	name = input("Hi, what is your name? Name:")
	print("Hello", name, "!")

def area_of_a_room(): #Date: 8/29/2022
	'''
	Write a program that asks the user to enter the width and length of a room. Once
	the values have been read, your program should compute and display the area of the
	room. The length and the width will be entered as floating point numbers. Include
	units in your prompt and output message; either feet or meters, depending on which
	unit you are more comfortable working with.
	'''

	width = float(input("Please enter the width of the room in Meters."))
	length = float(input("Please enter the length of the room in Meters."))

	area = width * length
	print(f"The area of the room is {area} Meters squared")

def area_of_a_field(): #Date: 8/29/2022
	'''
	Create a program that reads the length and width of a farmer’s field from the user in
	feet. Display the area of the field in acres.
	Hint: There are 43,560 square feet in an acre.
	'''

	width = input("How wide is the field in feet?")
	length = input("How long is the field in feet?")
	conversion = 43560


	area = width * length
	area = area/conversion
	print(f"The area of the field is {area} acre(s)")


def bottle_deposits(): #Date: 8/29/2022
	'''
	In many jurisdictions a small deposit is added to drink containers to encourage people
	to recycle them. In one particular jurisdiction, drink containers holding one liter or
	less have a $0.10 deposit, and drink containers holding more than one liter have a
	$0.25 deposit.
	Write a program that reads the number of containers of each size from the user.
	Your program should continue by computing and displaying the refund that will be
	received for returning those containers. Format the output so that it includes a dollar
	sign and always displays exactly two decimal places.
	'''

	small = float(input("Please input how many one litre or less bottles you are depositing"))
	large = float(input("Please input how many bottles that are more than one litre that you are depositing"))

	small += small * 0.10
	large += large * 0.25

	refund += small + large
	refund = "{:.3g}".format(refund)

	print(f"You refund is ${refund}.")


def tax_tip(): #Date 8/29/2022
	'''
	The program that you create for this exercise will begin by reading the cost of a meal
	ordered at a restaurant from the user. Then your program will compute the tax and
	tip for the meal. Use your local tax rate when computing the amount of tax owing.
	Compute the tip as 18 percent of the meal amount (without the tax). The output from
	your program should include the tax amount, the tip amount, and the grand total for
	the meal including both the tax and the tip. Format the output so that all of the values
	are displayed using two decimal places
	'''

	total = float(input("Cost:"))
	tip = total * 0.18
	taxConst = 0.075
	tax = total * taxConst 
	totalFin = total + tip + tax

	tip = '{0:.3g}'.format(tip)
	taxConst = '{0:.3g}'.format(taxConst)
	tax = '{0:.3g}'.format(tax)
	totalFin ='{0:.3g}'.format(totalFin)

	print(f"Cost: {total}")
	print(f"Tip: {tip}")
	print(f"Tax: {tax}")
	print(f"Total: {totalFin}")


def main_loop():
	tax_tip()


if __name__ == "__main__":
	main_loop()