import os 

path = r"C:\Users\Lenovo\Desktop\test.txt"

try:
    os.remove(path)
    print("File deleted successfully")
    
except FileNotFoundError:
    print("File not found")