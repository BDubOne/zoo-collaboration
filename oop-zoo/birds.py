from zoo_manager import Animal

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species, sound="chirp")

        self.wingspan = wingspan
    
    

    
    def give_birth(self):
        print(f'{self._name} is hatching a new {self._species}!')
