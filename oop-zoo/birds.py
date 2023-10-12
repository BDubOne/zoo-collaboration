from zoo_manager import Animal, Aviary

class Bird(Animal):
    total_birds = 0
    def __init__(self, id, name, species, wingspan):
        super().__init__(name, species, sound="chirp")
        Bird.total_birds += 1
        self._id = Bird.total_birds
        self.wingspan = wingspan
        Aviary.birds[self._id] = self
    
    

    
    def give_birth(self):
        print(f'{self._name} is hatching a new {self._species}!')
