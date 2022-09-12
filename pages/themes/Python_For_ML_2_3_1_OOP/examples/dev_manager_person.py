# methods as messaging mechanism between objects:
if 1:
  class Person:
    def __init__(self,name):
      self.name = name

  class Manager(Person):
    def __init__(self, name):
      super(Manager, self).__init__(name)

    def get_report(self, dev):
      dev.report(self)

  class Developer(Person):
    def __init__(self, name):
      super(Developer, self).__init__(name)

    def report(self, manager):
      print(self.name, "is reporting to", manager.name)



  maria = Manager("Maria")
  pesho = Developer("Pesho")

  print( maria.name)
  print( pesho.name)

  pesho.report(maria)
  maria.get_report(pesho)
  # maria.get_report(pesho)