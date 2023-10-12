from zoo_manager import Animal


class Reptile(Animal):
    def __init__(self, name, species, sound="ggggg"):
        super().__init__(name, species, sound)
        self.sound = sound

    def bask_in_sun(self):
        print(f" {self._name} is basking in the sun")
    