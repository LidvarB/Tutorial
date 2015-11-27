# 1. Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# 2. Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"
# 3. Run and see all the functions work together!

# Function 1
def list_benefits():
	strings = []
	strings.append("More organized code")
	strings.append("More readable code")
	strings.append("Easier code reuse")
	strings.append("Allowing programmers to share and connect code together")
	return strings

# Function 2	
def build_sentence(info):
	return (info + " is a benefit of functions!")


# Function with optional extra arguments
def funct_opt_arg(first, second, third, *therest):
	print("\nExample of optional arguments:")
	print("First: %s" % first)
	print("Second: %s" % second)
	print("Third: %s" % third)
	print("And all the rest... %s" % list(therest))
	
# Function where order of arguments does not matter
def funct_kwd_arg(first, second, third, **options):
    print("\nExample of keyword arguments:")
    if options.get("action") == "sum":
        print("""'action = "sum"' => The sum is: %d""" % (first + second + third))

    if options.get("number") == "first":
        return first

	
# Main function
def main():
	#Assign benefits
	benefits = list_benefits()

	#Loop throug all entries in benefits list and print complete sentence
	for benefit in benefits:
		print(build_sentence(benefit))
	
	#Call with optional arguments
	funct_opt_arg(1,2,3,4,5,6,7,8)
	
	#Call with keyword arguments
	result = funct_kwd_arg(1, 2, 3, action = "sum", number = "first")
	print("""'number = "first"' => Result: %d""" % result)
	
	#Pause until the user presses enter
	input("\nPress <enter> to exit")	
	
	
# Call main function
main()
