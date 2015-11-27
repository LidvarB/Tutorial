#Comparison operators:
#	<	less than
#	<=	less than or equal
#	> 	greater than
#	>=	greater than or equal
#	==	equal
#	!=	not equal

#Logical operators
#	and	(A and B)
#	or	(A or B)
#	in	(A in B)
#	is	(A is B)
#	not	(A not B)

print("Check 9 < 10: ",9 < 10,'\n')
print("Check 9 <= 10: ",9 <= 10,'\n')
print("Check 9 > 10: ",9 > 10,'\n')
print("Check 9 >= 10: ",9 >= 10,'\n')
print("Check 9 == 10: ",9 == 10,'\n')
print("Check 9 != 10: ",9 != 10,'\n')
print("Check (9 < 10) and (9 != 10)): ",(9 < 10) and (9 != 10),'\n')
print("Check (9 > 10) and (9 != 10)): ",(9 > 10) and (9 != 10),'\n')
print("Check (9 < 10) or (9 != 10)): ",(9 < 10) or (9 != 10),'\n')
print("Check (9 > 10) or (9 != 10)): ",(9 > 10) or (9 != 10),'\n')

string = "abcde"
print("Check if \'c\' is present in the string \""+string+"\": ",'c' in string,'\n')
print("Check if \'ac\' is present in the string \""+string+"\": ",'ac' in string,'\n')
print("Check if \'bc\' is present in the string \""+string+"\": ",'bc' in string,'\n')

a = [1,2,3]
b = [1,2,3]
c = d = [1,2,3]
print("Check \'a is b\', a = [1,2,3], b = [1,2,3]: ",a is b,'\n')
print("Check \'c is d\', c = d = [1,2,3]: ",c is d,'\n')

print("\nnot False:",not False,'\n')

#Pause until the user presses enter
input("Press <enter> to exit")
