animal = "cow"
item = "moon"

print(f"The {animal} jumped  ove  the {item}")
print("The {} jumped over the {}".format(animal, item))#  index base 
print("The {0} jumoed  ove the {1}".format(animal,item))#posiotnal 
print("the {animal} jumped over the {item}".format(animal = "dog", item = "fence"))# key value pair 

text = "The  {} jumped  ove the {}"
print(text.format(animal,item))

# Second variation 
cast ="Chauhan"
print("Anmol is from {:10} cast".format(cast))# 10 spaces  alloted 
print("Anmol is from {:>10} cast".format(cast))# 10 spaces  alloted  right aligned 
print("Anmol is from {:<10} cast".format(cast))# 10 spaces  alloted  left  aligned

# third variation

number = 3.14213
print("The number is {:.2f}".format(number))# 2 decimal places 

number2 = 10000
print("The number is {:,}".format(number2))#with comma seperation
print("the number is {:b}".format(number2))# binary fromat