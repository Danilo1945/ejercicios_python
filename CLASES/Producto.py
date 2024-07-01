class Producto:
    def __init__(self, id, nombre, cantidad, Categoria):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.Categoria = Categoria

    def __str__(self):
        return "%s-%s" % (str(self.id), self.nombre)

    def get_cantidades(self):
        return self.cantidad

    def add_cantidad(self, canidad):
        self.cantidad = self.cantidad + canidad
