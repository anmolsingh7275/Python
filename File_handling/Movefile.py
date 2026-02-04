
import os 
source = r"C:\Users\Lenovo\Desktop\test"
destination = r"C:\Users\Lenovo\Downloads\destination"
try:
     if os.path.exists(destination):
           print("Destination file already exists")
     else:
         os.replace(source,destination)
         print(source + " Moved to destination")
except FileNotFoundError:  
    print("File not found")