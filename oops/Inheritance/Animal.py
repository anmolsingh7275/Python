class Animal:
    alive = True
    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("This animall is sleeping") 
        
class Rabbit(Animal):
    def run(self):
        print("this rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
        
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
rabbit.eat()
rabbit.sleep()
rabbit.run()
               
                           