#Loop is a piece of code to repeate code multiple times

from collections import namedtuple

def string2float_cast(inpStr):
	#flagCastStatus is a boolean used to flag that an exception occurred during cast from string to float
	cast = namedtuple('cast',['num','flag'])
	
	#Initialize to False
	cast.flag = False
	
	#Try to cast from string to float
	try:
		cast.num = float(inpStr)
	except ValueError: #Exception due to string not being a float number
		print("ValueError:",inpStr,"is not a number\n")
		cast.num = 0
		cast.flag = True
	except : #Other exceptions
		print("Unknown exception\n")
		cast.num = 0
		cast.flag = True

	#Return result
	return cast


def example1():
	# While loop, example 1
	print("Example 1: While loop")

	#Initialize the counter variable
	counter = 1
	
	while counter <= 5:
		#Print the counter value
		print("The index is :",counter)
		#Increase the counter: counter = counter +1
		counter += 1
		#Example: Add numbers until 0 is entered
	print('\n')


def example2():
	#While loop, example 2
	print("Example 2: While loop")
	
	#Initialize variables
	a = 1
	sum = 0

	print('Enter numbers to sum. Enter zero to quit.')
	
	#Loop while the input is different from 0
	while a != 0:
		#Read number from keyboard
		inp = input('Number ?')

		#Cast the numner to float
		myCast = string2float_cast(inp)

		#Print the result on screen
		if (myCast.flag == True): #Invalid number entered
			print("You did not enter a valid number\n")
			a = 0
		else: #Valid number, add it to the sum
			a = myCast.num
			sum += a
	print("The sum is:",sum,'\n')
		

def example3():
	#For loop example
	print("Example 3: For loop:")
	
	#Initialize variables
	myList = [3,4,5,2,3,7,6,5,4,3,2]
	idx = 0
	print("The list:",myList,'\n')
	
	#For loop: Loop through the list and print the values
	for num in myList:
		print("The number at index",idx,"is :",num)
		idx += 1

		
def example4():
	#use range function
	print("\nExample 4: Use the 'range(4,10,2)' function to print every second value from 4 to 10 (not including):")
	for x in range(4,10,2):
		print(x)	


def example56():
	# Prints out 0,1,2,3,4
	print("\nExample 5: Print from 0 until loop 'break' at 'count >=5'")
	count = 0
	while True:
		print(count)
		count += 1
		if count >= 5:
			break

	# Prints out only odd numbers - 1,3,5,7,9
	print("\nExample 6: Print odd numbers in the range 0 to 10, using 'continue' at 'x % 2 == 0'")
	for x in range(10):
		# Check if x is even
		if x % 2 == 0:
			continue
		print(x)
			
		
def main():
	#Launch example 1
	example1()
	
	#Launch example 2       
	example2()

	#Launch example 3       
	example3()

	#Launch example 4       
	example4()
	
	#Launch example 5       
	example56()
	
	#Pause until the user presses enter
	input("Press <enter> to exit")


#Call main function
main()
