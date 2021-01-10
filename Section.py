class Section:
  def __init__(self, crot_list, id):
    self.crot_list = crot_list
    self.id = id

  def __hash__(self):
    return hash(id)

  def __eq__(self, other):
    if not isinstance(other, Section):
      return False

  def __return_crot_list(self):
    return crot_list
  