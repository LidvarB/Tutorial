# Python's solution to errors are exceptions.
# You might want to do something special when an exception is raised.
# This is done in a try/except block.

def do_stuff_with_number(n):
    print(n)

#List index exception	
def example1():
	the_list = (1, 2, 3, 4, 5)

	for i in range(20):
		try:
			do_stuff_with_number(the_list[i])
		except IndexError: # Raised when accessing a non-existing index of a list
			do_stuff_with_number("List index exception")

#Function to modify, should return the last name of the actor - think back to previous lessons for how to get it
def get_last_name():
	try:
		return actor["last_name"]
	except KeyError:
		return (actor["name"].split()[-1])
	
def example2():
	# Handle all the exceptions!
	#Setup
	
	#Test code
	get_last_name()
	print("All exceptions caught! Good job!")
	print("The actor's last name is %s" % get_last_name())

actor = {"name": "John Cleese", "rank": "awesome"}

# The main function
def main():
	#List index exception
	example1()

	example2()
	
	#Pause until the user presses enter
	input("\nPress <enter> to exit")	
			
# Call the main function			
main()