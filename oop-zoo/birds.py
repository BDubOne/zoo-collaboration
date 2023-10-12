from zoo_manager import Animal, Aviary

class Bird(Animal):
    total_birds = 0
    def __init__(self, name, species, wingspan):
        super().__init__(name, species, sound="chirp")
        Bird.total_birds += 1
        self._id = Aviary.total
        self.wingspan = wingspan
        Aviary.birds[self._id] = self

    def __str__(self):
        return f"{self._id} : {self._name} : {self._species}"

    
    

    
    def give_birth(self):
        print(f'{self._name} is hatching a new {self._species}!')
