class Factura:
    def __init__(self, id, nombre, Cliente,Producto):
        self.id = id
        self.nombre = nombre
        self.Cliente = Cliente
        self.Producto = Producto

    def __str__(self):
        return "%s-%s" % (str(self.id), self.nombre)
