from zoo_manager import Aviary
from mammals import Mammal
from birds import Bird
kai = Mammal("Kai", "dog", "woof")

polly = Bird("Polly", "Parrot", "6 ft")
polly = Bird("Polly", "Parrot", "6 ft")
polly = Bird("Polly", "Parrot", "6 ft")
polly = Bird("Polly", "Parrot", "6 ft")
print(polly.wingspan)
print(Aviary.birds)
#print(Aviary.total)
kai.speak()
Aviary.display_all_birds()