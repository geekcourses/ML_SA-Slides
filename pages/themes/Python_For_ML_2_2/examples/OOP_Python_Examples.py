# class vs onject properties
if 0:
  class A():
        a="class data"
        # def __init__(self, a):
        #       self.a = "obj data "+str(a)
        def __str__(self):
              return "self.a = {}".format(self.a)

  o1 = A()
  print("o1: ", o1)
  o1.a = 5;
  print("o1: ", o1)
  A.a = "class data changed"
  print("o1: ", o1)

# private names vs dunder names:
if 0:
  class A():
    def __test_():
      print("test")
    def __init__(self):
      self.__name="Ada"

  o1 = A()
  print( dir(A) )
  __main__._A.__test_()

# accessing private names
if 0:
  class Foo():
    def __bar(arg):
      print("I'm __bar with arg: ", arg)
    def baz(self, arg):
      self.__bar()

  print(dir(Foo))
  Foo._Foo__bar("test")

# inheritance of private names:
if 0:
  class A:
    __test = 1

  class B(A):
    def __init__(self):
      print(self._A__test)

  print(dir(B))
  b = B()

# unbound local variables:
if 0:
  def a():
    count = 0

    def b():
      # print(count)
      count += 1

    b()
  a()


# static variables:
if 0:
  class A:
    count = 0

    def __init__(self):
      self.__class__.count +=1

  o1 = A()
  o2 = A()
  print( A.count)

# special class attributes:
if 1:
  class A:
    count = 0
    def __init__(self, count):
      self.count = count
      print("init done on A object")


  print( A.__dict__)
  o1 = A(5)
  print( o1.__dict__)

  print("Class name",A.__name__)
  print("Object Class name",o1.__class__.__name__)

  print("Class module: ", A.__module__)
  print("Object module: ", o1.__module__)

  print("Class Parents:", A.__bases__)
  print("Class Parents:", o1.__class__.__bases__)




