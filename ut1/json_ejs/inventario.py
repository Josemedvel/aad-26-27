import json
from pathlib import Path

p = Path(__file__).parent / "inventario.json"
print(p)
def printMenu():
    print("Menú tienda:")
    print("1 - Completo")
    print("2 - Crear")
    print("3 - Reponer")
    print("4 - Vender")# minimo entre stock y cantidad o fallar
    print("5 - Borrar")
    print("6 - Salir")
if not p.exists():
    with open(p, "w", encoding="utf-8") as f:
        # primera forma
        f.write("{}")
        # dicc = {}
        # segunda forma
        # json.dump(dicc, f)
        # tercera forma
        # f.write(json.dumps(dicc))

finished = False
while not finished:
    printMenu()
    entrada = input("Elige opción:\t")
    try:
        entrada = int(entrada)
    except:
        continue
    match entrada:
        case 1:
            with open(p, "r", encoding="utf-8") as f:
                #dicc = json.loads(f.read())
                dicc = json.load(f)
                for item in dicc.items():
                    print(item[0], "-->", item[1])
        case 2:
            dicc = {}
            with open(p, "r", encoding="utf-8") as f:
                dicc = json.load(f)
            producto = input("Inserte nombre de nuevo producto:\t")
            while producto.strip() == "":
                producto = input("Inserte nombre de nuevo producto:\t")
            if producto not in dicc: # no existe el producto aun
                dicc[producto] = 0
                with open(p, "w", encoding="utf-8") as f:
                    json.dump(dicc, f)
                print(f"Producto `{producto}` creado")
            else:
                print(f"El producto `{producto}` ya existe, y hay {dicc[producto]} unidades")
        case 3:
            dicc = {}
            with open(p, "r", encoding="utf-8") as f:
                dicc = json.load(f)
            producto = input("Ingrese el producto a reponer:\t")
            while producto.strip() == "":
                producto = input("Ingrese el producto a reponer:\t")
            if producto not in dicc:
                print(f"El producto `{producto}` no existe, créalo antes")
            else:
                cantidad_valida = False
                cantidad = 0
                while not cantidad_valida:
                    cantidad = input("Ingrese cantidad a reponer:\t")
                    try:
                        cantidad = int(cantidad)
                        if cantidad > 0:
                            cantidad_valida = True
                        else:
                            print("La cantidad debe ser un entero positivo")
                    except:
                        print("La cantidad debe ser un entero positivo")
                dicc[producto] += cantidad
                with open(p, "w", encoding="utf-8") as f:
                    json.dump(dicc, f)
                print(f"Reposición de `{cantidad}` `{producto}`/s completa")
        case 5:
            dicc = {}
            with open(p, "r", encoding="utf-8") as f:
                dicc = json.load(f)
            producto = input("Ingrese el producto a eliminar del inventario: \t")
            while producto.strip() == "":
                producto = input("Ingrese el producto a eliminar del inventario: \t")
            if producto in dicc:
                del(dicc[producto])
                print(f"Producto `{producto}` eliminado del inventario")
                with open(p, "w", encoding="utf-8") as f:
                    json.dump(dicc,f)
            else:
                print(f"El producto `{producto}` no existe, consulte el inventario")
        case _:
            finished = True
print("Bye")
    
