# File copying in Python is done by reading data from a source file and writing it into a destination file 
# using appropriate file modes. Text files use r and w modes, while binary files use rb and wb.
# Python also provides the shutil module for efficient file copying.

# 1️⃣ shutil.copyfile(src, dst)

# 📌 Copies only file contents

# Source file must exist

# Destination file is created

# Metadata is NOT copied

# shutil.copyfile("source.txt", "dest.txt")

# 2️⃣ shutil.copy(src, dst)

# 📌 Copies file contents + permissions

# Destination can be file or directory

# Returns path of copied file

# shutil.copy("source.txt", "dest.txt")

# 3️⃣ shutil.copy2(src, dst)

# 📌 Copies file contents + permissions + metadata

# Metadata = time, date, etc.

# Best for backups

# shutil.copy2("source.txt", "dest.txt")

import shutil
source_path = r"C:\Users\Lenovo\Desktop\test.txt"
destination_path = r"C:\Users\Lenovo\Desktop\destination.txt"
shutil.copyfile(source_path,destination_path) # two arguemnerts source and destination 
