# A dictionary is a data type similar to arrays, but works with keys and values
# instead of indexes. Each value stored in a dictionary can be accessed using a key,
# which is any type of object (a string, a number, a list, etc.) instead of using
# its index to address it.

def example1():
	# Method 1 of assiging dictionary entries, with "name" as key
	phonebook1 = {}
	phonebook1["John"] = 938477566
	phonebook1["Jack"] = 938377264
	phonebook1["Jill"] = 947662781

	# Method 2 of assiging dictionary entries, with "name" as key
	phonebook2 = {
		"John" : 938477566,
		"Jack" : 938377264,
		"Jill" : 947662781
	}

	# Dictionaries can be iterated over, just like a list. However, a dictionary,
	# unlike a list, does not keep the order of the values stored in it. To iterate 
	#over key value pairs, use the following syntax:
	print("\nExample with the use of 'items()' to iterate through the list")
	for (name, number) in phonebook1.items():
		print ("Phone number of %s is %d" % (name, number))
	
	#...or the following method:
	print("\nExample: 'for name in phonebook2'")
	for name in phonebook2:
		print("Phone number of %s is %d" % (name, phonebook2[name]))
		
	# To remove a specified index, use either one of the following notations:
	del phonebook1["John"]
	phonebook2.pop("John")

def main():
	#Call example 1:
	example1()
	
	#Pause until the user presses enter
	input("\nPress <enter> to exit")
	
#Call main function
main()
