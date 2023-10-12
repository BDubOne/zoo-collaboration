from zoo_manager import Animal, ReptileEnclosure


class Reptile(Animal):
    total_reptiles = 0
    def __init__(self, name, species, sound="ggggg"):
        super().__init__(name, species, sound)
        Reptile.total_reptiles += 1
        self._id = Reptile.total_reptiles
        self.sound = sound
        ReptileEnclosure.reptiles[self._id] = self


    def __str__(self):
        return f"{self._id} : {self._name} : {self._species}"

    def bask_in_sun(self):
        print(f" {self._name} is basking in the sun")
    