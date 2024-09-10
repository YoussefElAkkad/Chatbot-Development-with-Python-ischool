# class Things:
#   pass

# class Animate(Things):
#   def eat(self):
#     print("I can eat")
#   def walk(self):
#     print("I can walk")


# class Mammals(Animate):
#   pass

# class Giraffes(Mammals):
#   def eat(self):
#     super().eat()
#     print("Eating leaves")

# class Lions(Mammals):
#   def eat(self):
#    super().eat()
#    print("Eating Meat")



# Mammal_one=Mammals()
# Mammal_one.eat()
# joe=Giraffes()
# joe.walk()
# joe.eat()
# Simba=Lions()
# Simba.eat()





class WatermelonSlice:
  def __init__(self,shape,color):
    self.shape=shape
    self.color=color
  def area(self):
    pass
    
class CircularSlice(WatermelonSlice):
  def __init__(self, color, radius):
    super().__init__("Circular", color)
    self.radius = radius
  def area(self):
    return 3.14 * self.radius ** 2
  
class RectangularSlice(WatermelonSlice):
  def __init__(self, color, length, width):
    super().__init__("Rectangular", color)
    self.length = length
    self.width = width
  def area(self):
    return self.length * self.width

circle_slice = CircularSlice("Red", 5)
rectangle_slice = RectangularSlice("Blue", 3, 4)

print("Circular Slice Area:", circle_slice.area())
print("Rectangular Slice Area:", rectangle_slice.area())
print(circle_slice.shape)
print(rectangle_slice.shape)

