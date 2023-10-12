from zoo_manager import Animal, Aviary


class Mammal(Animal):
    def __init__(self, name, species, sound="Grr"):
        super().__init__(name, species, sound)
        self.sound = sound

    
    def give_birth(self):
        print(f'{self._name} is giving birth to a baby {self._species}!')

    
class Primate(Mammal):
    def __init__(self, name, species, sound="Ohohohoh"):
        super().__init__(name, species, sound)
        self.sound = sound

    def climb_trees(self):
        print(f"{self._name} is climbing hella trees")

class Marsupial(Mammal):
    def __init__(self, name, species, sound="knockout punch"):
        super().__init__(name, species, sound)
        self.sound = sound

    def carry_baby(self):
        print(f'{self._name} is carrying a baby {self._species}')

    


    
    
