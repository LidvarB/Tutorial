#Inheritance allows us to define a class in terms of another class,
#which makes is easier to create and maintain and application

#Superclass
class Parent1:
	value1 = "This is value 1, inherited from parent1"
	value2 = "This is value 2, inherited from parent1"
	
#Superclass
class Parent2:
	value2 = "This is value 2, inherited from parent2"
	value3 = "This is value 3, inherited from parent2"
	value4 = "This is value 4, inherited from parent2"
	
#Inheriting class
class Child (Parent1,Parent2):
	pass	#pass is a place holder in order to avoid error
	
#Create instance of superclass
parent_ = Parent1()
#Print values of the class
print("Parent class:")
print(parent_.value1)
print(parent_.value2)

#Create instance of inheriting class
child_ = Child()
#Print values of the class
print('\n')
print("Child class:")
print(child_.value1)
#value 2 (ambiguous) is taken from Parent1
print(child_.value2)
print(child_.value3)
print(child_.value4)