# Decorators allow you to make simple modifications to callable objects
# like functions, methods, or classes. 

def repeater(old_function):
    def new_function(*args, **kwds): #See learnpython.org/page/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwds) #we run the old function
        old_function(*args, **kwds) #we do it twice
    return new_function #we have to return the new_function, or it wouldn't reassign it to the value

	
def Double_Out(old_function):
    def new_function(*args, **kwds):
        return 2*old_function(*args, **kwds) #modify the return value
    return new_function

def Check(old_function):
    def new_function(arg):
        if arg<0: raise ValueError("Negative Argument") #This causes an error, which is better than it doing the wrong thing
        elif arg==0: return ("Newly born") #This causes an error, which is better than it doing the wrong thing
        old_function(arg)
    return new_function

def type_check(correct_type):
	def check_arg(old_function):
		def new_function (arg):
			if isinstance(arg,correct_type):
				return old_function(arg)
			else:
				return "Bad type"
		return new_function
	return check_arg

@type_check(int)
def times2(num):
	return num*2

@type_check(str)
def first_letter(word):
	return word[0]

	
	
@Double_Out
def MultiplyDouble(num1, num2):
	print ("Use decorator to change the function output 2x3:",num1*num2)
	return num1*num2
	
@repeater
def Multiply(num1, num2):
    print ("Use decorator to execute the function twice:",num1*num2)

@Check
def Age(num1):
    print ("Use decorator to validate the age:",num1)
	
def main():
	#Call example 1:
	Multiply(2,3)
	
	#Call example 2:
	print("The modified value is:",MultiplyDouble(2,3))
	
	#Call example 2:
	print(Age(7))
	print(Age(0))
	#print(Age(-46))
	
	print("Call times2(10) =",times2(10))
	print("Call times2('Not a number')=",times2('Not a number'))
	print("Call first_letter('Yo, soon finished') =",first_letter('Yo, soon finished'))
	print("Call first_letter(['Not', 'A', 'String']) =",first_letter(['Not', 'A', 'String']))
	
	
	
	#Pause until the user presses enter
	input("\nPress <enter> to exit")
	
#Call main function
main()
