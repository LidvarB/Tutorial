#Returns the sum of two arguments, num1 + num2
def add(num1=0,num2=0):
	return num1+num2

#Returns the subtraction of two arguments, num1 - num2	
def sub(num1=0,num2=0):
	return num1-num2

#Returns the multiplication of two arguments, num1 * num2
def mult(num1=0,num2=0):
	return num1*num2

#Returns the division of two arguments, num1 / num2	
def div(num1=0,num2=1):
	if(num2 != 0): #Check for division by zero
		num3 = num1/num2
	else: #Division by zero
		num3 = "Division by zero is not allowed!"
	return num3

#Main function to be executed
def main():
	#Prompt user to select operation type
	operation = input("What do you want to do (+,-,*,/): ")
	if((operation != "+") and (operation != "-") and (operation != "*") and (operation != "/")):
		#invalid operation
		print("You must enter a valid operation!")
	else:
		#Read 1st input and cast it (string) to a decimal number, float
		var1 = float(input("Enter 1st number: "))
		
		#Read 2nd input and cast it (string) to a decimal number, float
		var2 = float(input("Enter 2nd number: "))
		
		#Conditional execution
		if(operation == '+'): #Addition
			print("Addition: ",var1,operation,var2," =",add(var1,var2))
		elif(operation == '-'): #Subtraction
			print("Subtraction: ",var1,operation,var2," =",sub(var1,var2))
		elif(operation == '*'): #Multiplication
			print("Multiplication: ",var1,operation,var2," =",mult(var1,var2))
		elif(operation == '/'): #Division
			print("Division: ",var1,operation,var2," =",div(var1,var2))
		else: #Exception handling
			print("Unexpected exception")
			
	#Pause until the user presses enter
	input("Press <enter> to exit")

#Call the main function	
main()