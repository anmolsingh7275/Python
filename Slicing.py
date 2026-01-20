#  Slicing in Python allows you to extract a portion of a sequence such as a string, list, or tuple. The syntax for slicing is as follows:
# sequence[start:stop:step]
# Here, start is the index where the slice begins (inclusive), stop is the index where the slice ends (exclusive), and step determines the increment between each index.

# Indexing starts at 0 in Python. Negative indexing can also be used to slice from the end of the sequence.
name  = "Anmol Singh"
print(name[:5])  
print(name[6:])
print(name[6:9])
print(name[:5:2])
print(name[0:5:2])
print(name[::-1])

# Slicing
website  = "www.google.com"
slice = slice(4,-4)
print(website[slice])