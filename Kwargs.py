def hello(**kwargs):
    for key,value in kwargs.items():
        print( value , end = " ")
        
print(hello(name="John", age=30, city="New York"))        