# # import turtle

# # #instance of the turtle class
# # pen1=turtle.Turtle()
# # pen2=turtle.Turtle()

# # pen1.forward(100)
# # pen1.circle(100)
# # pen2.backward(100)
# # pen2.circle(100)
# # turtle.done()

# class Person:
#   #Define the class attributes
#   name = ""
#   age = 0

#   #constructor

#   def __init__(self, name, age):
#     self.name=name
#     self.age=age

#   #Define the class methods
#   def get_name(self):
#     print("Get name")
#     return self.name

#   def get_age(self):
#     print("Get age")
#     return self.age

#   def greet(self):
#     print("Hello, my name is %s, and my age is %s" % (self.name, self.age))

# #creating the object
# # person1=Person()

# #Access the object attributes
# # person1.name="Youssef"
# # person1.age=24

# #Calling object methods
# # person1.greet()

# # person2=Person()
# # person2.name="Ahmed"
# # person2.age=22
# # person2.greet()

# person3=Person("Ali",12)
# person3.greet()


class Slices:

  def __init__(self, radius):
    self.radius = radius

  def calculate_area(self):
    return 3.14 * self.radius**2

  def calculate_circumference(self):
    return 2 * 3.14 * self.radius


# Create an instance of the Slices class with a given radius
watermelon_slice = Slices(7)
# Calculate and print the area and circumference of the watermelon slice
print("Area of the watermelon slice:", watermelon_slice.calculate_area())
print("Circumference of the watermelon slice:",
      watermelon_slice.calculate_circumference())
