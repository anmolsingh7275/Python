class prey():
    def __init__(self,name):
        self.name = name
    def flee(self):
        print("This " + self.name + " is fleeing")
class predator():
     def __init__(self,name):
        self.name = name
     def hunt(self):
       print("This " + self.name + " is hunting")
class Rabbit(prey):   
    pass
class hawk(predator):
    pass
class fish(prey,predator):
    pass
# rabbit1 = Rabbit("Black raabbit")
# rabbit1.flee()
fish1 = fish("saimon")
fish1.hunt()
fish1.flee()

                