# Generators are very easy to implement, but a bit difficult to understand.
# Generators are used to create iterators, but with a different approach.
# Generators are simple functions which return an iterable set of items,
# one at a time, in a special way.
# When an iteration over a set of item starts using the for statement,
# the generator is run. Once the generator's function code reaches a "yield"
# statement, the generator yields its execution back to the for loop, returning
# a new value from the set. The generator function can generate as many values
# (possibly infinite) as it wants, yielding each one in its turn.

import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(100,150)


def fibonacci():
	# Initialize start value
	last = 1
	next = 0
	# Returns the sum of the last two numbers
	while next+last < 1000:
		# Assign the new values
		last, next = next, last+next
		#Yield the sum of the last two values
		yield next

		
def example1():
	print("\nExample 1: 7 random numbers")
	for random_number in lottery():
		print("And the next number is... %d!" % random_number)

def example2():
	print("\nExample 2: Fibonacci series up to 1000")
	
	# Get and print next fibonacci series value with help of generator function
	for sum in fibonacci():
		print("The fibonacci number is:",sum)
	

# Main function
def main():
	# Run example 1: Generator funtion used to yield random numbers
	example1()
	
	# Run example 2: Generate and print fibonacci series
	example2()
		
	#Pause until the user presses enter
	input("\nPress <enter> to exit")	
	
	
# Call main function
main()