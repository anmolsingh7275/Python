#Open the file  in read mode  and print its comtext 
try:
    with open(r"C:\Users\Lenovo\Desktop\test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("file not find ")