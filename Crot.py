import random
class Crot:
  def __init__(self, crystal, liquid):
    self.crystal = crystal
    self.liquid = liquid

  def return_random(self):
    choices = [0, 1]
    if(bool(random.choice(choices))):
      return self.crystal
    else:
      return self.liquid