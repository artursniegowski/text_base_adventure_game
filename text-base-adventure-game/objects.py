# Base game object
class ObjectBase:
    """Main object of the game"""

    class_name = ""
    description = ""
    objects = {}

    def __init__(self,name) -> None:
        self.name = name
        ObjectBase.objects[self.name] = self

    def get_description(self):
        return self.class_name + ' - '+ self.name + '\n' + self.description

# Goblin - creature
class Goblin(ObjectBase):
    """Creature - type Goblin - vicious"""
    
    def __init__(self, name) -> None:
        self.class_name = "goblin"
        self._description = "A vicious creature"
        self.health = 3
        super().__init__(name)

    @property
    def description(self):
        if self.health >= 3:
            return self._description
        elif self.health == 2:
            creature_wound = "It has a wound on his left arm"
        elif self.health == 1:
            creature_wound = "It lost his right leg"
        elif self.health <= 0:
            creature_wound = "It is dead"
        return self._description + '\n' + creature_wound

    @description.setter
    def description(self,value):
        self._description = value
