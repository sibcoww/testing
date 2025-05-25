class Animal:
    def __init__(self, name, typee):
        self.name = name
        self.typee = typee    
    def speak(self, sound):
        print(f"{self.name} сказал {sound}")
    def describe(self):
        print(f"Я {self.typee}, меня зовут {self.name}")

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, "Dog")
        self.sound = sound
    def speak(self):
        super().speak(self.sound)

class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, "Cat")
        self.sound = sound
    def speak(self):
        super().speak(self.sound) 

class Parrot(Animal):
    def __init__(self, name, sound):
        super().__init__(name, "Parrot")
        self.sound = sound
    def speak(self):
        super().speak(self.sound)

dog = Dog("Bobik", "Gaf")
dog.describe()
dog.speak()
cat = Cat("Murzik", "Meow")
cat.describe()
cat.speak()
parrot = Parrot("GGG", "Pirat")
parrot.describe()
parrot.speak()