#Function call with and without parameters, with pointer

#Declare function with default parameters defined
def studentScore(name = "Empty",score = 0):
	print(name,"scored",score,"%")


def studentMultiScore(name = "Empty",*score):
	#Print all entries in the list with a while function
	print(name,"scored [%]",*score)
	
	idx = 0
	
	while idx < len(score):
		print(name,"scored on subject no",idx+1,":",score[idx],'%')
		idx += 1

	
def main():
	#Call function without giving parameters
	print('\n')
	print("Call function without setting parameters => Default parameters will be used")
	studentScore()
	
	#Call function with parameters
	print('\n')
	print("Call function with parameters")
	studentScore("Liddus",99)
	
	#Call function with pointer
	print('\n')
	print("Call function with parameters")
	score = (99,98,100,78)
	studentMultiScore("Liddus",*score)
	
	#Pause until the user presses enter
	input("Press <enter> to exit")

#Call main function
main()