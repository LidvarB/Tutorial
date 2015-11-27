#Exploring the slice function

#Define list with 10 numbers
myList = [0,1,2,3,4,5,6,7,8,9]
print("The full list: ",myList)
#Print list entries from index 4 to 8 (not including 8)
print("List from (but not including) index 4 to 8, myList[4:8] :",myList[4:8])

#Print list entries from entry 5 to end
print("List from entry 5 to end, myList[4:] :",myList[4:])

#List of characters
names=['a','b','c','d']
print("The full list: ",names)

#Print from start to 3rd entry
print("List from start to 3rd entry, names[:3] :",names[:3])

#Print every 2nd value of the list
print("List from start, every 2nd entry, myList[0::2] :",myList[0::2])

#Print the list in reverse order
print("List in reverse order, myList[::-1] :",myList[::-1])

#Pause until the user presses enter
input("Press <enter> to exit")
