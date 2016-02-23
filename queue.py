class Queue(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        self.vals.append(e)

    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not in queue.')
