class Cliente:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return "%s-%s" % (str(self.id), self.nombre)
