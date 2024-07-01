from CLASES.Categoria import Categoria
from CLASES.Producto import Producto


class DB:
    def __init__(self, list_categorias=None, list_clientes=None, lis_productos=None, lis_facturas=None):
        self.list_categorias = list_categorias if list_categorias is not None else []
        self.list_clientes = list_clientes if list_clientes is not None else []
        self.lis_productos = lis_productos if lis_productos is not None else []
        self.lis_facturas = lis_facturas if lis_facturas is not None else []

    def get_categorias(self):
        return self.list_categorias

    def addd_categorias(self, categoria):
        self.list_categorias.append(categoria)

    def get_clientes(self):
        return self.list_clientes

    def get_productos(self):
        return self.lis_productos

    def get_facturas(self):
        return self.lis_facturas


def main():
    db = DB()

    db.addd_categorias(categoria=Categoria(id=1, nombre='Frutas'))
    db.addd_categorias(categoria=Categoria(id=2, nombre='Lacteos'))
    db.addd_categorias(categoria=Categoria(id=3, nombre='Limpieza'))
    db.addd_categorias(categoria=Categoria(id=4, nombre='Enlatados'))

    lista_categorias = db.get_categorias()


    for categ in lista_categorias:
        print(categ.__str__())


main()
