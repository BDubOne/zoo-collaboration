
from birds import Bird

class Animal:
    def __init__(self, name, species, sound="whazzzap"):
        self._name = name
        self._species = species
        self.sound = sound


    @property
    def get_name(self):
        return self._name
    @get_name.setter
    def set_name(self, new_name):
        self._name = new_name

    @property
    def get_species(self):
        return self._species

    def speak(self):
        print(f'{self._name} goes {self.sound}')

class Aviary:
    birds = {}

    def __init__(self, )
    
    

        