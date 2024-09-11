class Dog:
  def __init__(self,breed):
    self.breed=breed
  def make_sound(self):
    return "Woof!"

class Cat:
  def __init__(self,breed):
    self.breed=breed

  def make_sound(self):
    return "Meow!"

class AnimalShelter:
  def __init__(self):
    self.animals=[]
  def add_animal(self,animal):
    self.animals.append(animal)
  def make_sounds(self):
    for animal in self.animals:
      print(animal.make_sound())


shelter=AnimalShelter()
shelter.add_animal(Dog("Golden Retriever"))
shelter.add_animal(Cat("Persian"))
shelter.add_animal(Dog("Poodle"))
shelter.make_sounds()