class Set(object):
    def __init__(self):
        self.set = []

    def __str__(self):
        self.set.sort()
        return '{' + ', '.join([str(e) for e in self.set]) + '}'

    def insert(self, e):
        if e not in self.set:
            self.set.append(e)

    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.set.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

a = Set()
a.insert(0)
a.insert(1)
a.insert(2)
print a
a.remove(3)


