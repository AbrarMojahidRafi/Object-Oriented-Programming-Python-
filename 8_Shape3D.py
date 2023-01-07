"""Given the following class, write the code for the Sphere and the Cylinder class so that
the following output is printed.

class Shape3D:
pi = 3.14159
def __init__(self, name = 'Default', radius = 0):
self._area = 0
self._name = name
self._height = 'No need'
self._radius = radius
def calc_surface_area(self):
return 2 * Shape3D.pi * self._radius
def __str__(self):
return "Radius: "+str(self._radius)

sph = Sphere('Sphere', 5)
print('----------------------------------')
sph.calc_surface_area()
print(sph)
print('==================================')
cyl = Cylinder('Cylinder', 5, 10)
print('----------------------------------')
cyl.calc_surface_area()
print(cyl)

OUTPUT:
Shape name: Sphere, Area Formula: 4 * pi * r
* r
----------------------------------
Radius: 5, Height: No need
Area: 314.159
==================================
Shape name: Cylinder, Area Formula: 2 * pi *
r * (r + h)
----------------------------------
Radius: 5, Height: 10
Area: 471.2385
"""



# solution:

class Shape3D:
  pi = 3.14159

  def __init__(self, name = 'Default', radius = 0):
    self._area = 0
    self._name = name
    self._height = 'No need'
    self._radius = radius   
  def calc_surface_area(self):
    return 2 * Shape3D.pi * self._radius

  def __str__(self):
      return "Radius: "+str(self._radius)

##############################################################################################################################

class Sphere(Shape3D):

  def __init__(self, n, r):
    super().__init__(n, r)
    self.radius = r
    self.height = 'No need'
    self.store = ""
    print(f"Shape name: {n}, Area Formula: 4 * pi * r * r")

  def calc_surface_area(self):
    a1 = super().__str__() 
    a2 = "Area: " + str(super().calc_surface_area()*2*self.radius)
    self.store = a1 + ", " + "Height: " + self.height + ", " + a2
  def __str__(self):
    return self.store


class Cylinder(Shape3D):
  def __init__(self, n, r, h):
    super().__init__(n, r)
    self.radius = r
    self.height = h
    self.store = ""
    print(f"Shape name: {n}, Area Formula: 2 * pi * r * (r + h)")

  def calc_surface_area(self):
    a1 = super().__str__() 
    a3=super().pi
    a2 = "Area: " + str(2*a3*self.radius*(self.radius+self.height))
    self.store = self.store + a1 + ", " + "Height: " + str(self.height) + ", " + a2
  def __str__(self):
    return (self.store)



sph = Sphere('Sphere', 5)
print('----------------------------------')
sph.calc_surface_area()
print(sph)
print('==================================')
cyl = Cylinder('Cylinder', 5, 10)
print('----------------------------------')
cyl.calc_surface_area()
print(cyl)