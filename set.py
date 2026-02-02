# Set is collection which is unordered, unindexed. No duplicate members.
# Definition:
# A set in Python is an unordered, mutable collection of unique elements used to store multiple values in a single variable.

# Facts about Python Sets:

# Written using curly braces {}

# Stores only unique values (no duplicates)

# Unordered — no fixed position or index

# Mutable — you can add or remove elements

# Does not support indexing or slicing

# Faster for membership testing (in operator)

utensils = {'fork', "spoon", "knife","Knife"}
dishes = { "bowl", "plate", "cup", "knife"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# print(dishes)

# dinner_table = utensils.union(dishes)
# dinner_table = utensils.difference(dishes)
dinner_table = dishes.difference(utensils)
print(utensils.intersection(dishes))
print(dinner_table)
