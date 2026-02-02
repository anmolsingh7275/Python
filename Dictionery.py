# Dictionery   A chnagebale unordered collectiion  of Key : valeue pairs No duplicate keys 
# fast bacuse they are using  use hashing allow to  access a value qucikly 

# Definition:
# A dictionary in Python is a mutable, unordered (insertion-ordered from Python 3.7+) collection of key–value pairs, used to store data in the form of keys and values.

# Facts about Python Dictionaries:

# Written using curly braces {} with key: value

# Stores data as key → value

# Keys must be unique and immutable (int, string, tuple)

# Values can be any data type

# Mutable — you can add, update, or delete items

# Access values using keys, not index

# Very fast lookup
capitals = { "USA" : "Washington DC"
            , "India"  : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow",}
capitals.update({"germany" : "Berlin"})
capitals.update({"USA":"Las vegas"})
capitals.pop("China")
capitals.clear()
# print(capitals["India"])
# print(capitals.get("Germany"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
for key , value in capitals.items():
    print (key,value)