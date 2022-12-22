﻿# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class
# SorcererStone class will be a child or subclass of the superclass Item
class SorcererStone(Item):
    # __init__ is the contructor method
    def __init__(self, amt): 
        self.amt = amt # attribute of the SorcererStone class
        super().__init__(name="SorcererStone",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)
 
class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A small Sword with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)
class Cloak(Weapon):
    def __init__(self):
        super().__init__(name="Cloak",
                         description="An invisibility cloak.",
                         value=1,
                         damage=1)

class Potion(Item):
    def __init__(self, name, description, value, heal):
        self.name = name
        self.description = description
        self.value = value
        self.heal = heal
        super().__init__(name, description, value)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nHeal: {}".format(self.name, self.description, self.value, self.heal)

class SmallPotion(Potion):
    def __init__(self):
        super().__init__(name="Small Potion",
                         description="A small potion",
                         value=5,
                         heal=20)