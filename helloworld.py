#Define the function helloWorld
def helloWorld(myString = 'Empty'):
	
	#Print the function argument on screen
	print(myString)
	
	#Prompt the user to enter his name
	myName = input("What is your name? ")
	
	#Prompt the user to enter a numer, and then cast that to integer since input is of type string
	myVar = int(input("Enter a number: "))

	#Example of conditional exectution
	if(myName == "Lidvar" or myVar != 0):
		print(myName," is great!")
	elif(myName == "Liddus"):
		print(myName," is ok")
	else:
		print("Hello")

#Execute the function helloWorld
helloWorld("Hello function world")

#Pause until the user presses enter
input("Press <enter> to exit")