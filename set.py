# Set is collection which is unordered, unindexed. No duplicate members.
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
