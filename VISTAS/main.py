from CLASES.Categoria import Categoria
from CLASES.Producto import Producto


class DB:
    def __init__(self, list_categorias=None, list_clientes=None, lis_productos=None, lis_facturas=None):
        self.list_categorias = list_categorias if list_categorias is not None else []
        self.list_clientes = list_clientes if list_clientes is not None else []
        self.lis_productos = lis_productos if lis_productos is not None else []
        self.lis_facturas = lis_facturas if lis_facturas is not None else []

    # Categorias
    def get_categorias(self):
        return self.list_categorias

    def addd_categorias(self, categoria):
        self.list_categorias.append(categoria)

    def get_id_categorias(self):
        categorias = self.get_categorias()
        id = 0
        for categ in categorias:
            if categ.id > id:
                id = categ.id
        return id + 1


def eliminar_categorias(db):
    for cat in db.list_categorias:
        print(cat.__str__())
    id = int(input("INGRESE EL ID DE LA CATEGORIA A ELIMINAR:"))
    for cat in db.list_categorias:
        if cat.id == id:
            db.list_categorias.remove(cat)
            print("CATEGORIA ELIMINADA")
def listar_categorias(db):
    for cat in db.list_categorias:
        print(cat.__str__())
def actualizar_categorias(db):
    for cat in db.list_categorias:
        print(cat.__str__())
    id = int(input("INGRESE EL ID DE LA CATEGORIA A ACTUALIZAR:"))
    for cat in db.list_categorias:
        if cat.id == id:
            cat.nombre = input("INGRESE EL NUEVO NOMBRE:")
            print("CATEGORIA ACTUALIZADA")
def get_clientes(self):
    return self.list_clientes

def get_productos(self):
    return self.lis_productos

def get_facturas(self):
    return self.lis_facturas


def menu():
    print("BIENVENIDO A LA BASE DE DATOS")
    print("1. Categorias")
    print("2. Clientes")
    print("3. Productos")
    print("4. Facturas")
    print("5. Salir")
    op = int(input())
    if op > 5 or op < 1:
        print("OPCION INVALIDA")
    else:
        return op


def menu_crud(nombre_tabla):
    print("CRUD %s" % nombre_tabla)
    print("1. Crear")
    print("2. Actualizar")
    print("3. Eliminar")
    print("4. Listar")
    print("5. Salir")
    op = int(input())
    if op > 6 or op < 1:
        print("OPCION INVALIDA")
    else:
        return op


def menu_crear_categoria(db):
    print("CREAR CATEGORIA")
    nombre = input("INGRESE EL NOMBRE DE LA CATEGORIA:")
    debug = db.addd_categorias(categoria=Categoria(id=db.get_id_categorias(), nombre=nombre))
    print('Categoria %s creada' % (nombre))


def menu_coontinuar(nombre_tabla):
    op = 0
    while op == 0:
        print("CONTINUAR EN %s?" % nombre_tabla)
        print("1. SI")
        print("2. NO")
        op = int(input())
        if op > 2 or op < 1:
            print("OPCION INVALIDA")
        else:
            return op


def data_inicial(db):
    db.addd_categorias(categoria=Categoria(id=1, nombre='Frutas'))
    db.addd_categorias(categoria=Categoria(id=2, nombre='Lacteos'))
    db.addd_categorias(categoria=Categoria(id=3, nombre='Limpieza'))
    db.addd_categorias(categoria=Categoria(id=4, nombre='Enlatados'))


def main():
    db = DB()
    data_inicial(db)
    op_while = 0
    while op_while == 0:
        op = menu()
        if op == 1:
            op_categ = 0
            while op_categ == 0:
                nombre_tabla = 'CATEGORIAS'
                crud = menu_crud(nombre_tabla)
                if crud == 1:  # crear
                    print(menu_crear_categoria(db))
                    cont = menu_coontinuar(nombre_tabla)
                    if cont == 1:
                        op_categ = 0
                    else:
                        op_categ = 0
                elif crud == 2:  # actualizar
                    actualizar_categorias(db)
                    op_categ = 1
                elif crud == 3:  # eliminar
                    eliminar_categorias(db)
                    op_categ = 1
                elif crud == 4:  # listar
                    listar_categorias(db)
                    op_categ = 1




        elif op == 2:
            print("CLIENTES")
        elif op == 3:
            print("PRODUCTOS")
        elif op == 4:
            print("FACTURAS")
        elif op == 5:
            print("CONTINUAR EN EL SISTEMA ")
        elif op == 6:
            print("SALIR")


main()
