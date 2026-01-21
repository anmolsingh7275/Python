#Tuples is  collections which  is ordered and unchangeable used to froup 
# together multiple items in a single varibale 

student = ("Anmol" , 21 , "male")

print(student.count("Anmol"))
print(student.index("male"))
for x in student:
    print(x)
    
if "Anmol" in student:
    print("Anmol is here")    