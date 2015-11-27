#Absolute number calculation

from collections import namedtuple

#Define absolute function
def absolute(n):
        if (n < 0): # Check if number is negative
                return -n
        else: # Number is zero or positive
                return n
                
def string2float_cast(inpStr):
        #flagCastStatus is a boolean used to flag that an exception occurred during cast from string to float

        cast = namedtuple('cast',['num','flag'])

        #Initialize to False
        cast.flag = False
        
        #Try to cast from string to float
        try:
                cast.num = float(inpStr)
        except ValueError: #Exception due to string not being a float number
                print("ValueError:",inpStr,"is not a number\n")
                cast.num = 0
                cast.flag = True
        except : #Other exceptions
                print("Unknown exception\n")
                cast.num = 0
                cast.flag = True

        #Return result
        return cast

def main():
        #Prompt user to enter a number
        inpStr = input("Enter your number: ")

        myCast = string2float_cast(inpStr) 
        
        #Print the result on screen
        if (myCast.flag == True):
                print("Calculation of absolute value failed\n")
        else:
                #Call function absolute() to return the absolute valute of the number
                myNumAbs = absolute(myCast.num)
                print("The absolute value of",myCast.num,"is",myNumAbs,'\n')

        #Pause until the user presses enter
        input("Press <enter> to exit")

#Call the main function
main()
