# Dictionery   A chnagebale unordered collectiion  of Key : valeue pairs No duplicate keys 
# fast bacuse they are using  use hashing allow to  access a value qucikly 
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