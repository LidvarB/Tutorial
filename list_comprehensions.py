# List Comprehensions is a very powerful tool, which creates a new list based on
# another list, in a single, readable line.

def example1():
#	sentence = "the quick brown fox jumps over the lazy dog"
#	words = sentence.split()
#	word_lengths = []
#	
#	for word in words:
#		if word != "the":
#			word_lengths.append(len(word))
	print("Example 1: List comprehension")
	sentence = "the quick brown fox jumps over the lazy dog"
	words = sentence.split()
	word_lengths = [len(word) for word in words if word != "the"]
	print(sentence)
	print(words)
	print(word_lengths)

	
def example2():
	numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
	
	newList = [(int(num)) for num in numbers if (num > 0)] 
	
	print("The positive numbers as integers:",newList)

# Main function
def main():
	# Run example 1: Generator funtion used to yield random numbers
	example1()
	
	# Run example 2: Create a list called "newlist" out of the list "numbers", 
	# which contains only the positive numbers from the list, as integers.
	example2()
	
	#Pause until the user presses enter
	input("\nPress <enter> to exit")	
	
	
# Call main function
main()