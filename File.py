import os 
path = r"C:\Users\Lenovo\Desktop\test.txt"
if os.path.exists(path):
    print("This file is present")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("thi is  a folder")
else:
    print("File is not present")
