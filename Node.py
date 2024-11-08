class Node:
    def __init__(self, id, data = None):
        self.id = id
        self.data = data
        self.neighbors = []
        self.parent = None
        self.is_analized = False