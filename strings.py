#A string can be single quote, 'string'
#Use \ in front of single quote that is part of the string itself
a='I am a single quoted string. Use \\ in front of a singel-quote, \', to make it part of the string'

#A string can be double quote, "string"
#Use \ in front of double quote that is part of the string itself
b="I am a double quoted string. Use \\ in front of a double-quote, \". Don't worry about single quotes. \n"

#A string can be triple quote, """string"""
c="""I am a triple quoted string. Don't worry about double quotes" \n"""

print(a)
print("The length of the string is:",len(a),'\n')
print(b)
print(c)
print('Use \\n to create a line shift \n')

a = "Hello"
b = 5

print(a,b)
print(a+str(b))
print(' ')

#Print list several times
print("The list [1,2,3] is multiplied 3 times:",[1,2,3]*3,'\n')

#Use string formatting:
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is %s$."
print("Using string formatting:",format_string % data)

#String class methods
astring = "Hello world"
print("\nSome string classs methods:")
print("'"+astring+"' is",len(astring),"characters long")
print("'o' is character",astring.index("o"),"of the string")
print("There are",astring.count("l"),"'l' characters in the string")
print("'"+astring[3:7]+"' is slice [3:7] of the string")
print("Upper case:",astring.upper())
print("Lower case:",astring.lower())
print("string.startswith('Hello'):",astring.startswith("Hello"))
print("string.endswith('asfafaf'):",astring.endswith("asfafaf"))
print("string.split(' ' ):",astring.split(" "))

#Pause until the user presses enter
input("Press <enter> to exit")


