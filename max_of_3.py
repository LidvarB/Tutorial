#The function max() is contained in the math library, which must be imported.
import math

#Calculate the maximum of 3 values
def maxOf3(var1,var2,var3):
    largest = max(var1,var2,var3)
    return largest    


#Main fuction to be called
def main():
    #Read 3 numbers from keyboard. These must be cast from string to integer type.
    x=int(input("Enter 1st number: "))
    y=int(input("Enter 2nd number: "))
    z=int(input("Enter 3rd number: "))

    #Output the maximum value on screen
    print("The largest number is :",maxOf3(x,y,z))

    #Pause until the user presses enter
    input("Press <enter> to exit")

#Call the main function
main()
