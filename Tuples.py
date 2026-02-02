#Tuples is  collections which  is ordered and unchangeable used to froup 
# together multiple items in a single varibale 

# A tuple in Python is an ordered, immutable collection of items used to store multiple values in a single variable.

# Facts about Python Tuples:

# Written using parentheses ()

# Can store different data types

# Order is preserved

# Immutable — values cannot be changed after creation

# Allows duplicate values

# Indexed (index starts from 0)

# Faster than lists (because they are immutable)

student = ("Anmol" , 21 , "male")

print(student.count("Anmol"))
print(student.index("male"))
for x in student:
    print(x)
    
if "Anmol" in student:
    print("Anmol is here")    