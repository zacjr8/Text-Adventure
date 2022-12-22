class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)
 
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)

class HellHound(Enemy):
    def __init__(self):
        super().__init__(name="Hell Hound", hp=20, damage=10)

class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf", hp=25, damage=15)

class Nagini(Enemy):
    def __init__(self):
        super().__init__(name="Nagini", hp=10, damage=5)

class Reaper(Enemy):
    def __init__(self):
        super().__init__(name="Reaper", hp=15, damage=10)

class Voldemort(Enemy):
    def __init__(self):
        super().__init__(name="Voldemort", hp=20, damage=5)