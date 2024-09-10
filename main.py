class Things:
  pass

class Animate(Things):
  def walk(self):
    print("I can walk")


class Mammals(Animate):
  pass

class Giraffes(Mammals):
  pass

joe=Giraffes()
joe.walk()