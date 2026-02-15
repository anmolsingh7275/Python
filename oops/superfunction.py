class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)   # Calls Animal's constructor

    def speak(self):
        super().speak()          # Calls parent method
        print("Dog barks")
dog1 = Dog("Buddy")
dog1.speak()
