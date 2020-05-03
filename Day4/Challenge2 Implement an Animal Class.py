class Animal:
    pass
    # write your class here
    def __init__(self , name , sound):
        self.name = name
        self.sound = sound
    
    def Animal_details(self):
        print('Name: {}'.format(self.name))
        print('Ssund: {}'.format(self.sound))


class Dog(Animal):
    def __init__(self , name , sound , family):
        super().__init__(name, sound)
        self.family = family
    def Animal_details(self):
        super().Animal_details()
        print('Family: {}'.format(self.family))

    # write your class here


class Sheep(Animal):
    pass
   # write your class here
    def __init__(self , name , sound , color):
        super().__init__(name, sound)
        self.color = color
    def Animal_details(self):
        super().Animal_details()
        print('Color: {}'.format(self.color))


print("Write your solution in the classes above.")

