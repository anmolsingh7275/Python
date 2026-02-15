class Car:
    color = None

def change_color(car,color):
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1,"White")
change_color(car_2,"Black")        
change_color(car_3,"Blue") 

print(car_1.color) 
print(car_2.color)  
print(car_3.color)     
           