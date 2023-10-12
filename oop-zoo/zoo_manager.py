

class Animal:
    def __init__(self, name, species, sound="whazzzap"):
        self._name = name
        self._species = species
        self.sound = sound

    def __str__(self):
        return f"{self._name} is a {self._species}"


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

    def __init__(self, name):
        self.name = name
        self.total = len(Aviary.birds)

    def display_all_birds():
        for index in Aviary.birds:
            print(Aviary.birds[index])

class ReptileEnclosure:
    
    reptiles = {} 
    

    def __init__(self, name):
        self.name = name
        

    def display_all_reptiles():
        for index in ReptileEnclosure.reptiles:
            print(ReptileEnclosure.reptiles[index])
    
    def Display_Reptile_Number():
        print(len(ReptileEnclosure.reptiles))

    
    
    

        