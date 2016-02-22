class Coordinate(object):
    foobar = 5

    def __init__(self, x, y):
        try:
            self.x = x
            self.y = y
            assert type(self.x) == int and type(self.y) == int
        except AssertionError:
            print '__init()__ only accepts integer arguments.'

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

    def get_displacement(self, coordinate):
        return ((coordinate.x - self.x)**2+(coordinate.x - self.x)**2)**0.5

    def get_magnitude(self):
        return (self.x**2 + self.y**2)**0.5

p1 = Coordinate(1, 1)
p2 = Coordinate(10, 11)
print p1
print p2
print p1.get_displacement(p2)
