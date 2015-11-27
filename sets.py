# Sets are lists with no duplicate entries.
# Sets are a powerful tool in Python since they have the ability to
# calculate differences and intersections between other sets.

# Example 1
def example1():
	a = set(["Jake", "John", "Eric"])
	print("The set a is:",a)
	b = set(["John", "Jill"])
	print("The set b is:",b)
	
	# To find out common elements, use the "intersection" method
	print("The common intersection between set a and b is:",
	a.intersection(b))

	# To find out all elements only present in one or the other,
	# use the "symmetric_difference" method
	print("The symmetric difference between set a and b is:",
	a.symmetric_difference(b))
	
	# To find out all elements only present in one,
	# use the "difference" method
	print("The difference between set a and b is:",
	a.difference(b))
	print("The difference between set b and a is:",
	b.difference(a))
	
	# To find out all elements present in one or the other,
	# use the "union" method
	print("The union between set a and b is:",
	a.union(b))
	
def example2():
	pass
	
# The main function
def main():
	#List index exception
	example1()

	example2()
	
	#Pause until the user presses enter
	input("\nPress <enter> to exit")	
			
# Call the main function			
main()