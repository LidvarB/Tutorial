#Implementation of class
#Class has attributes
#Class has methods

#Define class for Person
# 'self' is a pointer to the class object
class Person:
	#Constructor is used to initialize the value
	def __init__(self,id):
		self.id = id
		print(self.id,"class instance is created")
		
		
	#Destructor is used to remove the object when out of scope
	def __del__(self):
		print(self.id,"class instance is destroyed")
		
	#Method to set name
	def setFullName(self,firstName,lastName):
		self.firstName = firstName
		self.lastName = lastName

	#Method to print the name
	def printFullName(self):
		print("The name is:",self.lastName+",",self.firstName,'\n')

		
class vehicle:
	# Method for setting the vehicle attributes
	def setAttributes(self,color,type,value,name):
		self.color = color
		self.type = type
		self.value = value
		self.name = name
	
	# Method for printing the vehicle attributes
	def doPrint(self):
		print(self.name,"is a",self.color,self.type,"worth $%d" %self.value)
		
def main():
	#Create instance of class
	personName = Person("007")

	#Enter name from keyboard
	firstName = input("Enter first name: ")
	lastName = input("Enter last name: ")
	
	#Set name
	personName.setFullName(firstName,lastName)

	#Print name
	personName.printFullName()

	#Destroy the instance
	personName.__del__()

	#Print name
	personName.printFullName()
	
	#Create instances of vehicle
	car1 = vehicle()
	car2 = vehicle()
	
	#Set vehicle attributes
	car1.setAttributes("red","convertible",60000,"Fer")
	car2.setAttributes("blue","van",10000,"Jump")
	
	#Print the vehicle object information
	print('\nThis is an example of class Vehicle:')
	car1.doPrint()
	car2.doPrint()
	
	#Pause until the user presses enter
	input("Press <enter> to exit")


#Call main function
main()
