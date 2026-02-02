path = r"C:\Users\Lenovo\Desktop\test.txt"

text ="Th is appended text \n"
with open(path,'w') as file:
    file.write(text)
# appended code 
with open(path,'a') as file:
    file.write(text)    