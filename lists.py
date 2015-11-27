#List of strings
names=["Vetle","Lidvar","Nina"]

#List index 0 is the first item
print(names[0])
print(names[2])

#List index -1 is the last item in the list
print(names[-2])

#Add a new item to the end of the list
names.append("Halldis")
print(names[-1])

#Add age to list
age=[7,46,45,75]
names.extend(age)
print(names)

#Remove item
names.remove(age[0])
names.remove(age[1])
names.remove(age[2])
names.remove(age[3])

#Print name and age for all entries in the list

#Initialize the loop index
idx = 0   

#Loop through the list of name and age and print these
while (idx < len(names)):
    print(names[idx],age[idx],"år")
    idx = idx +1
    
#Pause until the user presses enter
input("Press <enter> to exit")
