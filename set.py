class Set(object):
    def __init__(self):
        self.set = []

    def __str__(self):
        return str(self.set)

    def insert(self, e):
        if e not in self.set:
            self.set.append(e)
        else:
            print "Error: %d already in set" % e

    def member(self, e):
        if e in self.set:
            return True
        else:
            return False

    def remove(self, e):
        if self.member(e):
            self.set.remove(e)
        else:
            print 'Error: %d not in set' % e

a = Set()
a.insert(10)
a.insert(10)
print a
a.remove(10)
print a
