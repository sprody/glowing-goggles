class Queue(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        self.vals.append(e)

    def remove(self):
        try:
            return self.vals.remove(self.vals[0])
        except:
            raise ValueError(str(e) + ' not in queue.')
