# import turtle

# #instance of the turtle class
# pen1=turtle.Turtle()
# pen2=turtle.Turtle()

# pen1.forward(100)
# pen1.circle(100)
# pen2.backward(100)
# pen2.circle(100)
# turtle.done()

#







class Person:
  #Define the class attributes
  name = ""
  age = 0
  
  #Define the class methods
  def get_name(self):
    print("Get name")
    return self.name

  def get_age(self):
    print("Get age")
    return self.age
    
  def greet(self):
    print("Hello, my name is %s, and my age is %s" % (self.name, self.age))


#creating the object
person1=Person()

#Access the object attributes
person1.name="Youssef"
person1.age=24

#Calling object methods
person1.greet()

