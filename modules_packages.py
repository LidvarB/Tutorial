# ***MODULES***
# Modules in Python are simply Python files with the .py extension, which implement
# a set of functions. Modules are imported from other modules using the import command.
# To import a module, we use the import command. Check out the full list of built-in
# modules in the Python standard library here.
# The first time a module is loaded into a running Python script, it is initialized
# by executing the code in the module once. If another module in your code imports
# the same module again, it will not be loaded twice but once only - so local variables
# inside the module act as a "singleton" - they are initialized only once.

# import the library
import math

print("\nList module functions:\n",dir(math))

print("\nCall help for function 'gamma()':\n")
help(math.gamma)

# Site modules are stored under
# C:\Program Files\Python\WinPython-64bit-3.4.3.6\python-3.4.3.amd64\Lib\site-packages
from string2float_module import cast2float_module

# ***PACAKGES***
# Packages are namespaces which contain multiple packages and modules themselves.
# They are simply directories, but with a twist.
# Each package in Python is a directory which MUST contain a special file called 
# __init__.py. This file can be empty, and it indicates that the directory it
# contains is a Python package, so it can be imported the same way a module can be
# imported.

from libu_package import string2float

def example_module_import():
	#Prompt user to enter a number
	inpStr = input("\nModule: Enter your number: ")

	myCast = cast2float_module(inpStr) 
	
	#Print the result on screen
	if (myCast.flag == False):
		print("Not a valid number!\n")
	else:
		#Call function absolute() to return the absolute valute of the number
		myNum = myCast.num
		print("The value is",myNum,'\n')


def example_package_import():
	#Prompt user to enter a number
	inpStr = input("\nPackage: Enter your number: ")

	myCast = string2float.cast(inpStr) 
	
	#Print the result on screen
	if (myCast.flag == False):
		print("Not a valid number!\n")
	else:
		#Call function absolute() to return the absolute valute of the number
		myNum = myCast.num
		print("The value is",myNum,'\n')
				
def example_re():
	import re
	
	findMatch = []
	
	for member in dir(re):
		if "find" in member:
			findMatch.append(member)
	
	print("\nMembers in module 're' that includes 'find':",findMatch)

				
def main():
	#Call example of module import
	example_module_import()
		
	#Call example of package import
	example_package_import()
		
	#Call example of list search and match
	example_re()

	#Pause until the user presses enter
	input("Press <enter> to exit")

#Call the main function
main()
