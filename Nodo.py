class Nodo:
    def __init__(self, id, datos = None):
        self.id = id
        self.datos = datos
        self.vecinos = []
        self.padre = None
        self.analizado = False