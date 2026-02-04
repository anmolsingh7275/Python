class Car:
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
    def drive(self):
        print("The " + self.model +" is driving")
    def stop(self):
         print("The " + self.model + " has stopped")
         
         
car_1 = Car("toyota", "corolla","2020")
car_2 = Car("HOnda","civic","2023")
car_1.stop() 
car_2.drive()       
         
