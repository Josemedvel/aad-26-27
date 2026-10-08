from pathlib import Path

p = Path("informe2.txt") # True
p = Path("informe3.txt") # False
p = Path("informe2.txt")

print(p.exists())
print(p.name)
print(p.suffix)

p = Path("../binario/")
print(p.exists())
print(list(p.glob("*.py"))[0].suffix)

# concatenar rutas
p = Path(".")
print(p.is_file()) # directorio actual - False
p_completa = p / "informe2.txt"

print(p_completa.is_file()) # archivo informe2.txt - True

# creacion carpetas
arbol = Path("logs")
print(arbol.exists()) # False
try:
    Path.mkdir(arbol, parents=True)
except FileExistsError:
    print("Subcarpetas ya existen, abortando creación")
finally:
    with open("logs/log.txt", "a") as log:
        log.write("hola buenas\n")

