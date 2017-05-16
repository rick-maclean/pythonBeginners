import random
import sys
import os

class Animal:
    __name = None
    __height = 0  # __ means private
    __weight = 0
    __sound = 0

#constructor
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def get_type(self):
        print("Animal")     # demostrate polymorphism

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)
    def set_name(self, name):
        self.__name = name  #setter

    def get_name(self):
        return self.__name  #getter

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound


cat = Animal('Whiskers', 33, 10, 'meow')
print(cat.toString())


# Inheritance
class Dog(Animal):
    __owner = ""

#constructor
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        self.__animal_type = None
        # How to call the super class constructor
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")     # demostrate polymorphism

    # We can overwrite functions in the super class
    # NOTE:  need to call get_name()  and cannot directly refence __name
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.get_name(), 
                                                                                       self.get_height(), 
                                                                                       self.get_weight(), 
                                                                                       self.get_sound(), 
                                                                                       self.__owner)

    #method overloading
    #different tasks based on attributes sent in
    #NOTE:  how_many=None allows for no attribute to be sent in
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

spot = Dog('Spot', 53, 27, ' ruff ', 'Rick')
print(spot.toString())

# Polymorphism allows use to refer to objects as their super class
# and the correct functions are called automatically
 
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()
 
test_animals = AnimalTesting()
 
test_animals.get_type(cat)
test_animals.get_type(spot)
 
spot.multiple_sounds(4)